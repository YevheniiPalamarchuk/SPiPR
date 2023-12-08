import grpc
from concurrent import futures
import minitwitter_pb2
import minitwitter_pb2_grpc

class MiniTwitterServicer(minitwitter_pb2_grpc.MiniTwitterServicer):
    def __init__(self):
        self.messages = []

    def sendMessage(self, request, context):
        new_message = minitwitter_pb2.Message(content=f"Received: {request.content}")
        self.messages.append(new_message)
        return new_message

    def getMessages(self, request, context):
        for message in self.messages[-request.n:]:
            yield message

    def getMessagesWithHashtag(self, request, context):
        hashtag = request.hashtag
        # Filter messages containing the specified hashtag
        matching_messages = [message for message in self.messages if f"#{hashtag}" in message.content]
        for message in matching_messages:
            yield message

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    minitwitter_pb2_grpc.add_MiniTwitterServicer_to_server(MiniTwitterServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

