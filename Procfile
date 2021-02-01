web: python -m grpc_tools.protoc -I ./grpc-transformer/  --python_out=. --grpc_python_out=.  ./grpc-transformer/info.proto && gunicorn app:app --log-file=-
