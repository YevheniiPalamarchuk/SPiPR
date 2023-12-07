import grpc
import minitwitter_pb2
import minitwitter_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = minitwitter_pb2_grpc.MiniTwitterStub(channel)

        # Original message
        original_message = minitwitter_pb2.Message(content="Hello, MiniTwitter!")
        print("Original Message:", original_message.content)

        # Send the original message to the server
        send_response = stub.sendMessage(original_message)
        print("Response from server:", send_response.content)

        # Modify the message content
        modified_message = minitwitter_pb2.Message(content="#cats Hello this is my custom message from Yevhenii123!")

        # Send the modified message to the server
        modified_response = stub.sendMessage(modified_message)
        print("Response from server:", modified_response.content)

        # Retrieve and print the last 3 messages from the server
        messages = stub.getMessages(minitwitter_pb2.GetMessagesRequest(n=3))
        print("Received messages from server:")
        for message in messages:
            print(message.content)

if __name__ == '__main__':
    run()
