import grpc
import minitwitter_pb2
import minitwitter_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = minitwitter_pb2_grpc.MiniTwitterStub(channel)

        # Modify the message content
        modified_message = minitwitter_pb2.Message(content="Hello all this is my first message!")

        # Send the modified message to the server
        modified_response = stub.sendMessage(modified_message)
        print("Response from server:", modified_response.content)

        modified_message = minitwitter_pb2.Message(content="I really like #cats!")

        # Send the modified message to the server
        modified_response = stub.sendMessage(modified_message)
        print("Response from server:", modified_response.content)

        modified_message = minitwitter_pb2.Message(content="Let's go #Lakers #LAL")

        # Send the modified message to the server
        modified_response = stub.sendMessage(modified_message)
        print("Response from server:", modified_response.content)

        modified_message = minitwitter_pb2.Message(content="Can't wait to see improvements of MiniTwitter")

        # Send the modified message to the server
        modified_response = stub.sendMessage(modified_message)
        print("Response from server:", modified_response.content)

        modified_message = minitwitter_pb2.Message(content="123 Hello")

        # Send the modified message to the server
        modified_response = stub.sendMessage(modified_message)
        print("Response from server:", modified_response.content)

        modified_message = minitwitter_pb2.Message(content="What is better: #Ford or #Ferrari")

        # Send the modified message to the server
        modified_response = stub.sendMessage(modified_message)
        print("Response from server:", modified_response.content)

        modified_message = minitwitter_pb2.Message(content="Let's go to a #cinema together!")

        # Send the modified message to the server
        modified_response = stub.sendMessage(modified_message)
        print("Response from server:", modified_response.content)

if __name__ == '__main__':
    run()
