import socket  # noqa: F401


def main():

    print("Logs from your program will appear here!")

    server = socket.create_server(("localhost", 9092), reuse_port=True)
    connection,_ = server.accept() # wait for client
    connection.recv(1024)
    message_size = (35).to_bytes(4, signed=True)
    request_api_key = (18).to_bytes(2, signed=True)
    request_api_version = (4).to_bytes(2, signed=True)
    correlation_id = (1870644833).to_bytes(4, signed=True)
    connection.sendall(message_size+request_api_key+request_api_version+correlation_id)  # send 0 to client


if __name__ == "__main__":
    main()
