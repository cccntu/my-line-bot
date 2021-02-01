import os
import grpc
import info_pb2
import info_pb2_grpc


class Host():
    def __init__(self, address, name=''):
        self.name = name
        self.channel = grpc.insecure_channel(address)
        self.TextGenerationServiceStub = info_pb2_grpc.TextGenerationServiceStub(self.channel)
    def generate_text(self, text: str):
        response = self.TextGenerationServiceStub.GenerateText(info_pb2.Message(text=text))
        return response.text
    def close(self):
        self.channel.close()

host_address = os.getenv("GRPC_TRANSFORMER_HOST", 'localhost:50051')

host = Host(address=host_address)
def generate_text(text):
    return host.generate_text(text)
