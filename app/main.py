import socket  # noqa: F401


def main():

    print("Logs from your program will appear here!")

    server = socket.create_server(("localhost", 9092), reuse_port=True)
    connection,_ = server.accept() # wait for client
    received_message = connection.recv(1024).decode()
    api_key = int.from_bytes(received_message[4:6], signed=True)
    api_version = int.from_bytes(received_message[6:8])
    corr_id = int.from_bytes(received_message[8:12]).to_bytes(4, signed=True)
    api_key_2 = int.from_bytes(received_message[12:14], signed=True)
    api_version_2 = int.from_bytes(received_message[14:16])
    error_code = (0 if 0 <= api_version <= 4 else 35).to_bytes(2, signed=True)  # 35 is the error code for "Unsupported version"
    num_of_apikeys = (3).to_bytes(1, signed=False)
    message = (
        corr_id
        +error_code
        +num_of_apikeys
        +api_key.to_bytes(2, signed=True)
        +(0).to_bytes(2, signed=True)
        +(4).to_bytes(2, signed=True)
        +(0).to_bytes(1, signed=False)
        +(api_key).to_bytes(2, signed=True)
        +(api_version).to_bytes(2, signed=True)
        +(0).to_bytes(2, signed=True)
        +(0).to_bytes(1, signed=False)
        +(0).to_bytes(4,signed=True)
        +(0).to_bytes(1,signed=False))
    
    connection.sendall(
        len(message).to_bytes(4, signed=False)
        +message
    )
    
if __name__ == "__main__":
    main()
