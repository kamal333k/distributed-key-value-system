#!/usr/bin/env python3

import sys
import os
import socket
import pickle
import time
from threading import Thread
import re
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

sys.path.append('/home/yaoliu/src_code/protobuf-3.7.0/python')
import keyValue_pb2

replicaList, timestamp, nodeName = {} , 1 , []
firstreplica, secondreplica, thirdreplica, fourthreplica, value = 0, 0, 0, 0, 0

class replica:
    def __init__(self):
        self.KeyValueDict, self.logfilename, self.minkeyvalue, self.maxkeyvalue = {}, "", 0, 255

    def setDictionary(self, key , newvalue , newtimestamp , WriteLog = True):
        if  self.minkeyvalue > key > self.maxkeyvalue:
            logger.debug('Please enter a key in range 0-255')
            return False

        if self.get(key) != None and self.get(key) != False:
            if self.KeyValueDict[key][timestamp] > newtimestamp:
                return True

        if WriteLog:
            try:
                logfilehandle = open(self.logfilename, "a")
                logfilehandle.write(str(key) + "::" + newvalue+ "::" + str(newtimestamp) + "\n")
                logfilehandle.close()
            except IOError:
                logger.error("log file named" + self.logfilename + " not found!")
                return False

        self.KeyValueDict[key] = []
        self.KeyValueDict[key].insert(value,newvalue)
        self.KeyValueDict[key].insert(timestamp, newtimestamp)
        return True
    def sendMessageService(self, data, replica, time = int(time.time())):
        if 1 in replica:
            self.sendMessage(data,firstreplica, time)
        if 2 in replica:
            self.sendMessage(data,secondreplica, time)
        if 3 in replica:
            self.sendMessage(data,thirdreplica, time)
        if 4 in replica:
            self.sendMessage(data,fourthreplica, time)

    def sendMessage(self,data,replicaname,replicatimestamp):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host, port = replicaList[replicaname][1], int(replicaList[replicaname][2])
            sock.connect((host, port))
            putrequestmessage = keyValue_pb2.ReplicaPutRequest()
            putrequestmessage.key, putrequestmessage.id = data.clientputrequest.key, int(nodeName[0])
            putrequestmessage.value, putrequestmessage.timestamp = data.clientputrequest.value, replicatimestamp
            message = keyValue_pb2.KeyValueMessage()
            message.replicaputrequest.CopyFrom(putrequestmessage)
            sock.sendall(pickle.dumps(message))
            sock.close()
            return False
        except:
            return None
    def get(self, key):
        if key not in self.KeyValueDict:
            return False

        return self.KeyValueDict[key]

    def sendupdaterequestreplica(self,originalreplicaname,originalkey,originalvalue,sendupdatetimestamp):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host = replicaList[originalreplicaname][1]
            port = int(replicaList[originalreplicaname][2])
            sock.connect((host, port ))
            putrequestmessage = keyValue_pb2.ReplicaPutRequest()
            logger.debug("Read Repair done on ->" + replicaList[originalreplicaname][0])
            #logger.debug(originalreplicaname)
            putrequestmessage.id, putrequestmessage.key, putrequestmessage.value, putrequestmessage.timestamp = int(nodeName[0]), originalkey, originalvalue, sendupdatetimestamp
            message = keyValue_pb2.KeyValueMessage()
            message.replicaputrequest.CopyFrom(putrequestmessage)
            sock.sendall(pickle.dumps(message))
            sock.close()
        except:
            return None

    def sendgetrequestreplica(self,getrequestreplicaname,key):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host , port = replicaList[getrequestreplicaname][1], int(replicaList[getrequestreplicaname][2])
            sock.connect((host , port))
            getrequestmessage = keyValue_pb2.ReplicaGetRequest()
            getrequestmessage.id, getrequestmessage.key, getrequestmessage.timestamp, message = 1, key, 1, keyValue_pb2.KeyValueMessage()
            message.replicagetrequest.CopyFrom(getrequestmessage)
            sock.sendall(pickle.dumps(message))
            data = pickle.loads(sock.recv(10000))
            sock.close()
            return data
        except:
            logger.debug("")

    def checkts(self,data1,data2,data3):
        if(data1.replicaresponse.timestamp >= data2.replicaresponse.timestamp and data1.replicaresponse.timestamp >= data3.replicaresponse.timestamp):
            return 1
        if(data2.replicaresponse.timestamp >= data1.replicaresponse.timestamp and data2.replicaresponse.timestamp >= data3.replicaresponse.timestamp):
            return 2
        if(data3.replicaresponse.timestamp >= data2.replicaresponse.timestamp and data3.replicaresponse.timestamp >= data1.replicaresponse.timestamp):
            return 3
    
    def readrepairhandle(self,data,clientkey):
        logger.debug( "inside read repair replica handle")
        #first replica functioning
        if(int(firstreplica) == int(nodeName[0])):
            return self.firstreadrepairreplicahandler(data,clientkey)
        #second replica functioning
        elif(int(secondreplica) == int(nodeName[0])):
            return self.secondreadrepairreplicahandler(data,clientkey)
        #third replica functioning
        elif(int(thirdreplica) == int(nodeName[0])):
            return self.thirdreadrepairreplicahandler(data,clientkey)
        #fourth replica functioning
        elif(int(fourthreplica) == int(nodeName[0])):
            return self.fourthreadrepairreplicahandler(data,clientkey)

    def firstreadrepairreplicahandler(self,data,clientkey):    
        logger.debug( "inside first read repair replica handler")    
        if(0 <= clientkey <= 63) :
            return self.handleputreplica(0,secondreplica,thirdreplica,clientkey)
        elif(64 <= clientkey <= 127) :
            return self.handleputreplica(secondreplica,thirdreplica,fourthreplica,clientkey)
        elif(128 <= clientkey <= 191) :
            return self.handleputreplica(0,thirdreplica,fourthreplica,clientkey)
        elif(192 <= clientkey <= 255) :
            return self.handleputreplica(0,secondreplica,fourthreplica,clientkey)
        
    def secondreadrepairreplicahandler(self,data,clientkey):
        logger.debug( "inside second read repair replica handler")
        if(0 <= clientkey <= 63) :
            return self.handleputreplica(0,firstreplica,thirdreplica,clientkey)
        elif(64 <= clientkey <= 127) :
            return self.handleputreplica(0,thirdreplica,fourthreplica,clientkey)
        elif(128 <= clientkey <= 191) :
            return self.handleputreplica(firstreplica,thirdreplica,fourthreplica,clientkey)
        elif(192 <= clientkey <= 255) :
            return self.handleputreplica(0,firstreplica,fourthreplica,clientkey)
        
    def thirdreadrepairreplicahandler(self,data,clientkey):
        logger.debug( "inside third read repair replica handler")
        if(0 <= clientkey <= 63) :
            return self.handleputreplica(0,firstreplica,secondreplica,clientkey)
        elif(64 <= clientkey <= 127) :
            return self.handleputreplica(0,firstreplica,thirdreplica,clientkey)
        elif(128 <= clientkey <= 191) :
            return self.handleputreplica(0,firstreplica,fourthreplica,clientkey)
        elif(192 <= clientkey <= 255) :
            return self.handleputreplica(firstreplica,secondreplica,fourthreplica,clientkey)

    def fourthreadrepairreplicahandler(self,data,clientkey):
        logger.debug( "inside fourth read repair replica handler")
        if(0 <= clientkey <= 63) :
            return self.handleputreplica(firstreplica,secondreplica,thirdreplica,clientkey)
        elif(64 <= clientkey <= 127) :
            return self.handleputreplica(0,secondreplica,thirdreplica,clientkey)
        elif(128 <= clientkey <= 191) :
            return self.handleputreplica(0,firstreplica,thirdreplica,clientkey)
        elif(192 <= clientkey <= 255) :
            return self.handleputreplica(0,firstreplica,secondreplica,clientkey)

    def handleputreplica(self,replica1,replica2,replica3,clientkey):
        if(replica1 == 0):
            if clientkey not in self.KeyValueDict:
                logger.debug('Exception: Key do not exists on any replica')
                return
            responce1ts = self.KeyValueDict[clientkey][timestamp]
            logger.debug( self.KeyValueDict[clientkey][value])
            readrepairlist = {}
            data2 = self.sendgetrequestreplica(replica2,clientkey)
            logger.debug( data2)
            data3 = self.sendgetrequestreplica(replica3,clientkey)
            #logger.debug( data3.replicaresponse.value)
            check = ""
            if(data2 is None and data3 is None):
                logger.debug('Exception: Cannot connect to any Replica')
                return
            
            #logger.debug( data3.replicaresponse.timestamp)
            if data2 is not None:
                if data2.replicaresponse.timestamp > self.KeyValueDict[clientkey][timestamp]:
                    self.setDictionary(clientkey,data2.replicaresponse.value,data2.replicaresponse.timestamp)
                if self.KeyValueDict[clientkey][timestamp] > data2.replicaresponse.timestamp:
                    self.sendupdaterequestreplica(replica2,clientkey,self.KeyValueDict[clientkey][value] ,self.KeyValueDict[clientkey][timestamp])
            if data3 is not None:
                if data3.replicaresponse.timestamp > self.KeyValueDict[clientkey][timestamp]:
                    self.setDictionary(clientkey,data3.replicaresponse.value,data3.replicaresponse.timestamp)
                if self.KeyValueDict[clientkey][timestamp] > data3.replicaresponse.timestamp:
                    self.sendupdaterequestreplica(replica3,clientkey,self.KeyValueDict[clientkey][value] ,self.KeyValueDict[clientkey][timestamp])
            return self.KeyValueDict[clientkey][value]
           
        elif replica1 != 0 :
            data1 = self.sendgetrequestreplica(replica1,clientkey)
            logger.debug( data1)
           
            data2 = self.sendgetrequestreplica(replica2,clientkey)
            logger.debug( data2)
            
            data3 = self.sendgetrequestreplica(replica3,clientkey)
            logger.debug( data3)
            checkvalue = self.checkts(data1,data2,data3)
            logger.debug( checkvalue)
            if(checkvalue == 1):
                logger.debug( "inside check value")
                self.sendupdaterequestreplica(replica2,clientkey,data1.replicaresponse.value,data1.replicaresponse.timestamp)
                self.sendupdaterequestreplica(replica3,clientkey,data1.replicaresponse.value,data1.replicaresponse.timestamp)
            if(checkvalue == 2):
                self.sendupdaterequestreplica(replica1,clientkey,data2.replicaresponse.value,data2.replicaresponse.timestamp)
                self.sendupdaterequestreplica(replica3,clientkey,data2.replicaresponse.value,data2.replicaresponse.timestamp)
            if(checkvalue == 3):
                self.sendupdaterequestreplica(replica1,clientkey,data3.replicaresponse.value,data3.replicaresponse.timestamp)
                self.sendupdaterequestreplica(replica2,clientkey,data3.replicaresponse.value,data3.replicaresponse.timestamp)      
            return data1.replicaresponse.value

    def getvaluefromowner(self,data,clientkey):
        logger.debug( "inside getvaluefromowner")
        return self.readrepairhandle(data,clientkey)

    
    def clientputrequesthandler(self,data,clientsocket):
        logger.debug( "inside client put request handle")
        #first replica functioning
        if(int(firstreplica) == int(nodeName[0])):
            return self.firstclientputrequesthandler(data,clientsocket)
        #second replica functioning
        elif(int(secondreplica) == int(nodeName[0])):
            return self.secondclientputrequesthandler(data,clientsocket)
        #third replica functioning
        elif(int(thirdreplica) == int(nodeName[0])):
            return self.thirdclientputrequesthandler(data,clientsocket)
        #fourth replica functioning
        elif(int(fourthreplica) == int(nodeName[0])):
            return self.fourthclientputrequesthandler(data,clientsocket)

    def firstclientputrequesthandler(self,data,clientsocket):
        logger.debug("inside first client put request handler")
        if(0 <= data.clientputrequest.key <= 63) :
            self.setDictionary(data.clientputrequest.key,data.clientputrequest.value,int(time.time()))
            self.sendMessageService(data,[2,3],self.KeyValueDict[data.clientputrequest.key][1])
            logger.debug( "a")
        elif(64 <= data.clientputrequest.key <= 127) :
            self.sendMessageService(data,[2,3,4],int(time.time()))

        elif(128 <= data.clientputrequest.key <= 191) :
            self.setDictionary(data.clientputrequest.key,data.clientputrequest.value,int(time.time()))
            self.sendMessageService(data,[3,4],self.KeyValueDict[data.clientputrequest.key][1])

        elif(192 <= data.clientputrequest.key <= 255) :
            self.setDictionary(data.clientputrequest.key,data.clientputrequest.value,int(time.time()))
            self.sendMessageService(data,[2,4],self.KeyValueDict[data.clientputrequest.key][1])


    def secondclientputrequesthandler(self,data,clientsocket):
        logger.debug("inside second client put request handler")
        if(0 <= data.clientputrequest.key <= 63) :
            self.setDictionary(data.clientputrequest.key,data.clientputrequest.value,int(time.time()))
            self.sendMessageService(data,[1,3],self.KeyValueDict[data.clientputrequest.key][1])

            logger.debug( "a")
        elif(64 <= data.clientputrequest.key <= 127) :
            self.setDictionary(data.clientputrequest.key,data.clientputrequest.value,int(time.time()))
            self.sendMessageService(data,[3,4],self.KeyValueDict[data.clientputrequest.key][1])

        elif(128 <= data.clientputrequest.key <= 191) :
            self.sendMessageService(data,[1,3,4],int(time.time()))

        elif(192 <= data.clientputrequest.key <= 255) :
            self.setDictionary(data.clientputrequest.key,data.clientputrequest.value,int(time.time()))
            self.sendMessageService(data,[1,4],self.KeyValueDict[data.clientputrequest.key][1])


    def thirdclientputrequesthandler(self,data,clientsocket):
        logger.debug("inside third client put request handler")
        if(0 <= data.clientputrequest.key <= 63) :
            self.setDictionary(data.clientputrequest.key,data.clientputrequest.value,int(time.time()))
            self.sendMessageService(data,[1,2],self.KeyValueDict[data.clientputrequest.key][1])

            logger.debug( "a")
        elif(64 <= data.clientputrequest.key <= 127) :
            self.setDictionary(data.clientputrequest.key,data.clientputrequest.value,int(time.time()))
            self.sendMessageService(data,[2,4],self.KeyValueDict[data.clientputrequest.key][1])

        elif(128 <= data.clientputrequest.key <= 191) :
            self.setDictionary(data.clientputrequest.key,data.clientputrequest.value,int(time.time()))
            self.sendMessageService(data,[1,4],self.KeyValueDict[data.clientputrequest.key][1])

        elif(192 <= data.clientputrequest.key <= 255) :
            self.sendMessageService(data,[1,2,4],int(time.time()))


    def fourthclientputrequesthandler(self,data,clientsocket):
        logger.debug("inside fourth client put request handler")
        if(0 <= data.clientputrequest.key <= 63) :
            self.sendMessageService(data,[1,2,3],int(time.time()))

        elif(64 <= data.clientputrequest.key <= 127) :
            self.setDictionary(data.clientputrequest.key,data.clientputrequest.value,int(time.time()))
            self.sendMessageService(data,[2,3],self.KeyValueDict[data.clientputrequest.key][1])

        elif(128 <= data.clientputrequest.key <= 191) :
            self.setDictionary(data.clientputrequest.key,data.clientputrequest.value,int(time.time()))
            self.sendMessageService(data,[1,3],self.KeyValueDict[data.clientputrequest.key][1])

        elif(192 <= data.clientputrequest.key <= 255) :
            self.setDictionary(data.clientputrequest.key,data.clientputrequest.value,int(time.time()))
            self.sendMessageService(data,[1,2],self.KeyValueDict[data.clientputrequest.key][1])

       
    def replicahandle(self,data,clientsocket):
        self.logfilename = "writelog"+"-"+ str(nodeName[0])
        logger.debug( self.logfilename)
        if not os.path.exists(self.logfilename):
            logfilehandle = open(self.logfilename, "w+")
        else:
            logfilehandle = open(self.logfilename, "r")
            for line in logfilehandle:
                split = line.split('::')
                a,b, c = int(split[0]), split[1], int(split[2])
                self.setDictionary(a,b,c, False)
        
        if data.HasField("clientputrequest") :
            logger.debug( "inside client put")
            logger.debug( self.KeyValueDict)
            thread = Thread(target = self.clientputrequesthandler(data,clientsocket))
            thread.daemon = True
            thread.start()

        if data.HasField("replicaputrequest") :
            logger.debug( data)
            self.setDictionary(data.replicaputrequest.key,data.replicaputrequest.value,data.replicaputrequest.timestamp)
            logger.debug( self.KeyValueDict)

        if data.HasField("clientgetrequest") :
            clientkey, clientid = data.clientgetrequest.key, data.clientgetrequest.id
           
            #return value for particular key
            returnval = self.getvaluefromowner(data,clientkey)

            # Start packing response to client
            ownerResponcemsg = keyValue_pb2.ClientResponse()
            ownerResponcemsg.key, ownerResponcemsg.id = clientkey, clientid

            if returnval is None or returnval == "None" :
                ownerResponcemsg.status, ownerResponcemsg.value = False, "None"
            else:
                ownerResponcemsg.status, ownerResponcemsg.value = True, returnval
    
            clientResponcemsg = keyValue_pb2.KeyValueMessage()
            clientResponcemsg.clientresponse.CopyFrom(ownerResponcemsg)
            try:
                clientsocket.sendall(pickle.dumps(clientResponcemsg))
            except:
                logger.error( "ERROR ! socket exception while sending get val response to client")

        if data.HasField("replicagetrequest") :
            
            resp_mesg = keyValue_pb2.ReplicaResponse()
            replicaResponcemsg = keyValue_pb2.KeyValueMessage()
            resp_mesg.nodeid = nodeName[0]
            resp_mesg.key, resp_mesg.id = data.replicagetrequest.key, data.replicagetrequest.id
            if data.replicagetrequest.key in self.KeyValueDict:
                resp_mesg.timestamp = self.KeyValueDict[data.replicagetrequest.key][timestamp]
                resp_mesg.value = self.KeyValueDict[data.replicagetrequest.key][value]
                resp_mesg.status = True
            else:
                resp_mesg.value = "None"
                resp_mesg.status = False

            replicaResponcemsg.replicaresponse.CopyFrom(resp_mesg)

            try:
                clientsocket.sendall(pickle.dumps(replicaResponcemsg))
            except:
                logger.error( "Exception: socker error while sending get val response to client")

def startTheServer(serversocket):
    while True:
        (clientsocket, address) = serversocket.accept()
        data = pickle.loads(clientsocket.recv(1024))
        replica().replicahandle(data,clientsocket)
def readFromTheBlog():
    try:
        logger.debug(sys.argv[3])
        with open(str(sys.argv[3])) as file:
            for line in file:
                replicadata = line.strip().split(" ")
                nodeNumber = re.findall('\d+',replicadata[0].strip())
                replicalisttemp[int(nodeNumber[0])] = [replicadata[0].strip(), replicadata[1].strip() , replicadata[2].strip() ]
    except:
        logger.error("ERROR ! Not able to read input file, please check the format")
        sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        logger.debug("Arguments Error: Try entering <node> <port> <filename>")
        sys.exit(0)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    hostname = socket.gethostbyname(socket.gethostname())
    port = int(sys.argv[2])
    sock.bind((hostname, port))
    sock.listen(5)
    replicalisttemp = {}
    logger.debug("\nListening on "+str(hostname)+":"+ str(port))
    if not os.path.exists(sys.argv[3]):
        logger.error("ERROR: Input file isn't available")
        sys.exit(0)
    else:
       readFromTheBlog()

    for key in sorted(replicalisttemp.keys()):
        replicaList[key] = replicalisttemp[key]
    firstreplica, secondreplica, thirdreplica, fourthreplica = list(replicaList.keys())[0], list(replicaList.keys())[1], list(replicaList.keys())[2], list(replicaList.keys())[3]
    print("replica list ->", replicaList)
    nodeName = re.findall('\d+',sys.argv[1].strip())
    startTheServer(sock)