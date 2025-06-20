import socket  # noqa: F401
import threading  # noqa: F401
     
        
def main():

    print("Logs from your program will appear here!")

    server = socket.create_server(("localhost", 9092), reuse_port=True)
    connection , _ = server.accept()
    received_message = connection.recv(1024)
    corr_id = int.from_bytes(received_message[8:12]).to_bytes(4,signed=True)
    client_len = int.from_bytes(received_message[12:14], signed=True)
    topic__name_len = int.from_bytes(received_message[15+client_len:15+client_len+1])
    topic_name = int.from_bytes(received_message[15+client_len+1:topic__name_len], signed=True).to_bytes(topic__name_len, signed=True)
    print("---->",topic_name)
    message = (
        corr_id
        +(3).to_bytes(2, signed=True)
        +topic_name
        +(0).to_bytes(16, signed=True)
    )
        
    connection.sendall(
        len(message).to_bytes(4, signed=False)
        +message
    )

    
    
if __name__ == "__main__":
    main()
