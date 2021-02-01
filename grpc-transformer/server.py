import argparse
import logging
from concurrent import futures

import grpc
import info_pb2
import info_pb2_grpc
from transformers import pipeline, set_seed


class TextGenerationServiceServicer(info_pb2_grpc.TextGenerationServiceServicer):
    def __init__(self):
        set_seed(42)
        self.generator = pipeline("text-generation", model="gpt2")

    def GenerateText(self, request, context):
        text =  self.generator(request.text, max_length=30, num_return_sequences=1)[0][
            "generated_text"
        ]
        return info_pb2.Message(text=text)

def serve(args):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    info_pb2_grpc.add_TextGenerationServiceServicer_to_server(
        TextGenerationServiceServicer(), server)
    address = f'{args.ip}:{args.port}'
    port = server.add_insecure_port(address)
    print(f'serving on port {port}')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()

    parser = argparse.ArgumentParser(description="Parse arguments")
    parser.add_argument("--ip", type = str, default="[::]", help="port")
    parser.add_argument("--port", type = str, default="50051", help="port")
    args = parser.parse_args()

    serve(args)
