all: init

init: keyValue.proto
	protoc --python_out=./ keyValue.proto

client: client.py
	chmod +x client.py
	./client.py ${ip} ${port}

replica: coordinator.py
	chmod +x coordinator.py
	./coordinator.py ${node} ${port} replicas.txt
