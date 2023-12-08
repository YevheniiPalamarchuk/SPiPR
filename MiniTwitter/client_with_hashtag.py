# client_with_hashtag.py

import grpc
import minitwitter_pb2
import minitwitter_pb2_grpc

def run_with_hashtag():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = minitwitter_pb2_grpc.MiniTwitterStub(channel)

        # Retrieve and print messages with the hashtag 
        hashtag_messages = stub.getMessagesWithHashtag(minitwitter_pb2.GetMessagesWithHashtagRequest(hashtag="LAL"))
        print(f"Messages with hashtag #LAL:")
        for message in hashtag_messages:
            print(message.content)

if __name__ == '__main__':
    run_with_hashtag()
