import grpc
import minitwitter_pb2
import minitwitter_pb2_grpc

def retrieve_messages(stub, n_messages_to_retrieve):
    # Retrieve and print the last n messages from the server
    messages = stub.getMessages(minitwitter_pb2.GetMessagesRequest(n=n_messages_to_retrieve))
    print(f"Received the last {n_messages_to_retrieve} messages from server:")
    for message in messages:
        print(message.content)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = minitwitter_pb2_grpc.MiniTwitterStub(channel)

        # Take user input for the modified message content
        modified_message_content = input("Enter your message here!: ")

        # Create the modified message with user input content
        modified_message = minitwitter_pb2.Message(content=modified_message_content)

        # Send the modified message to the server
        modified_response = stub.sendMessage(modified_message)
        print("Response from server:", modified_response.content)

        # Retrieve and print the last n messages from the server
        n_messages_to_retrieve = int(input("Enter the number of messages to retrieve: "))
        retrieve_messages(stub, n_messages_to_retrieve)

if __name__ == '__main__':
    run()
