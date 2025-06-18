import socket  # noqa: F401
import threading  # noqa: F401

def send_message(connection):
    connection,_ = connection
    received_message = connection.recv(1024)
    while received_message:
        api_key = int.from_bytes(received_message[4:6], signed=True)
        api_version = int.from_bytes(received_message[6:8])
        corr_id = int.from_bytes(received_message[8:12]).to_bytes(4, signed=True)
        api_key_2 = int.from_bytes(received_message[12:14], signed=True)
        error_code = (0 if 0 <= api_version <= 4 else 35).to_bytes(2, signed=True)
        num_of_apikeys = (3).to_bytes(1, signed=False)
        message = (
            corr_id
            +error_code
            +num_of_apikeys
            +api_key.to_bytes(2, signed=True)
            +(0).to_bytes(2, signed=True)
            +(4).to_bytes(2, signed=True)
            +(0).to_bytes(1, signed=False)
            +(75).to_bytes(2, signed=True)
            +(0).to_bytes(2, signed=True)
            +(0).to_bytes(2, signed=True)
            +(0).to_bytes(1, signed=False)
            +(0).to_bytes(4,signed=True)
            +(0).to_bytes(1,signed=False))
        
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
