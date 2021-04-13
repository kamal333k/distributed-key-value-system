#!/usr/bin/env python3

import sys, socket, pickle, re, logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

sys.path.append('/home/yaoliu/src_code/protobuf-3.7.0/python')
import keyValue_pb2

class Client:
    def __init__(self):
        self.ip_addr, self.port, self.key,self.value = None, None, None, None
        
    def gethandler(self):
        get_msg = keyValue_pb2.ClientGetRequest()
        get_msg.id, get_msg.key = 1000, self.key
        message = keyValue_pb2.KeyValueMessage()
        message.clientgetrequest.CopyFrom(get_msg)

        self.connectionhandler("GET", message)
	
    def puthandler(self):
        put_msg = keyValue_pb2.ClientPutRequest()
        put_msg.id, put_msg.key, put_msg.value  = 1000, self.key, self.value 
        message = keyValue_pb2.KeyValueMessage()
        message.clientputrequest.CopyFrom(put_msg)
		
        self.connectionhandler(None, message)
		
    def connectionhandler(self, mode, message):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.ip_addr, int(self.port)))
        sock.sendall(pickle.dumps(message))

        if mode == 'GET':
            data = pickle.loads(sock.recv(4000))
            if(not data.clientresponse.status):
                logger.debug("Exception: There's no key found on the replicas or the replicas are down")
                return
            # if(not data.clientresponse.key_status):
            #     logger.debug('Exception: No key found on any of the replicas')
            #     return
            # elif(not data.key_status):
            #     logger.debug('Exception: No matching key found on replica')
            #     return

            logger.debug(data)

        sock.close()     
    
    def jobs(self, input_array):
        command = input_array[0]
        if command == "GET":
            self.key, self.value = int(input_array[1]), None
            self.gethandler()
        elif command == "PUT":
            self.key, self.value = int(input_array[1]), input_array[2] 
            logger.debug(self.value)
            self.puthandler()
        elif command == "Q":
            logger.debug("Exit console.")
            sys.exit(0)
        else:
            logger.error("Arguments are invalid.")

    def main(self):
        if len(sys.argv) != 3:
            logger.error("Try using: make client ip=<ip_addr> port=<port_number>")
            sys.exit(0)

        self.ip_addr = sys.argv[1]
        self.port = int(sys.argv[2])
        logger.info("Connected: Ip:: " + self.ip_addr +" Port::" + str(self.port))
        logger.info("Opening Console....")
        logger.info("--------------Available Requests--------------")
        logger.info("GET <key>")
        logger.info("PUT <key> <value>")
        logger.info("Q <To exit console>")
        logger.info("----------------------------------------------")

        while True:
            user_input = input("Console: ")
            if len(user_input) == 0:
                continue
            
            input_array = user_input.split()
            logger.debug(input_array)
            self.jobs(input_array)

if __name__ == "__main__":
	Client().main()
