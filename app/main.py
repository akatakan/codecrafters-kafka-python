import socket  # noqa: F401
import threading  # noqa: F401

def send_message(connection):
    connection,_ = connection
    while True:
        received_message = connection.recv(1024)
        if not received_message:
            break
        corr_id = int.from_bytes(received_message[8:12]).to_bytes(4)
        error_code = (3).to_bytes(2, signed=True)
        desc = int.from_bytes(received_message[24:30]).to_bytes(4)
        print(f"Description: {desc}")
        message = (
            corr_id
            +error_code
        )
        
        connection.sendall(
            len(message).to_bytes(4, signed=False)
            +message
        )
        
def main():

    print("Logs from your program will appear here!")

    server = socket.create_server(("localhost", 9092), reuse_port=True)
    while True:
        connection = server.accept()
        threading.Thread(target=send_message, args=(connection,),daemon=True).start()

    
    
if __name__ == "__main__":
    main()
