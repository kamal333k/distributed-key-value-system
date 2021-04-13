# Steps to compile and execute:
1. bash 
2. export PATH=/home/yaoliu/src_code/local/bin:$PATH 
3. export PKG_CONFIG_PATH=/home/yaoliu/src_code/local/lib/pkgconfig
4. To create a protobuf: make init
5. To start a client: make client ip=<ip_addr> port=<port_num>
6. vi replicas.txt (add content as:  node_name ip_address port_number) 
7. cat replicas.txt (to view created replicas file)
8. To start a coordinator: make replica node=<node_number> port=<port_numer> replicas.txt

# Tasks Distribution:
1. Made a client program, Set up sockets between replicas, Implemented file logging and loggers, Handled write requests, Handled read requests, Handled read repair, Implemented Paritioner function, Handled how timestamps are implemented. 
