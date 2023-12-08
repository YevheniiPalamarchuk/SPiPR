import grpc
from concurrent import futures
import minitwitter_pb2
import minitwitter_pb2_grpc

class MiniTwitterServicer(minitwitter_pb2_grpc.MiniTwitterServicer):
    def __init__(self):
        self.messages = []

    def sendMessage(self, request, context):
        trimmed_content = request.content[:80]
        new_message = minitwitter_pb2.Message(content=f"Received: {trimmed_content}")
        self.messages.append(new_message)
        return new_message

    def getMessages(self, request, context):
        for message in self.messages[-request.n:]:
            yield message

    def getMessagesWithHashtag(self, request, context):
        hashtag = request.hashtag
        filtered_messages = [message for message in self.messages if f"#{hashtag}" in message.content]
        for message in filtered_messages:
            yield message



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mini_twitter_servicer = MiniTwitterServicer()
    minitwitter_pb2_grpc.add_MiniTwitterServicer_to_server(mini_twitter_servicer, server)
    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        # Display last 5 messages when the server is terminated with Ctrl+C
        mini_twitter_servicer.displayLastNMessages(5)

if __name__ == '__main__':
    serve()
