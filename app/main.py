import socket  # noqa: F401
import threading  # noqa: F401
     
        
def main():

    print("Logs from your program will appear here!")

    server = socket.create_server(("localhost", 9092), reuse_port=True)
    connection , _ = server.accept()
    received_message = connection.recv(1024)
    corr_id = int.from_bytes(received_message[8:12]).to_bytes(4,signed=True)
    topic = int.from_bytes(received_message[35:40]).to_bytes(6,signed=True)
    print(f"Description: {topic}")
    message = (
        corr_id
        +topic
    )
        
    connection.sendall(
        len(message).to_bytes(4, signed=False)
        +message
    )

    
    
if __name__ == "__main__":
    main()
