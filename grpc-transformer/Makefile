all: requirements proto serve

requirements: requirements.txt
	pip install -U -r requirements.txt

proto: info_pb2_grpc.py info_pb2.py
info_pb2_grpc.py info_pb2.py: info.proto
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./info.proto


serve: proto server.py
	python server.py
