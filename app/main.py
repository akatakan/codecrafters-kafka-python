import socket  # noqa: F401


def main():

    print("Logs from your program will appear here!")

    server = socket.create_server(("localhost", 9092), reuse_port=True)
    connection,_ = server.accept() # wait for client
    received_message = connection.recv(1024)
    api_key = int.from_bytes(received_message[4:6], signed=True)
    api_version = int.from_bytes(received_message[6:8])
    corr_id = int.from_bytes(received_message[8:12])
    print(f"Corr_id: {corr_id}, Api_key: {api_key}, Api_version: {api_version}")
    error_code = (0 if 0 <= api_version < 4 else 35).to_bytes(2, signed=True)  # 35 is the error code for "Unsupported version"
    message_size = len(received_message).to_bytes(4, signed=True)
    api_keys = len([api_key]).to_bytes(2, signed=True)
    connection.sendall(message_size+corr_id.to_bytes(4, signed=True)+(0).to_bytes(2, signed=True)+api_keys+api_key.to_bytes(2, signed=True)+(0).to_bytes(2, signed=True)+ (4).to_bytes(2, signed=True))
    
if __name__ == "__main__":
    main()
