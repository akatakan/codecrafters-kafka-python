import socket  # noqa: F401


def main():

    print("Logs from your program will appear here!")

    server = socket.create_server(("localhost", 9092), reuse_port=True)
    connection,_ = server.accept() # wait for client
    received_message = connection.recv(1024)
    corr_id = int.from_bytes(received_message[8:12])
    api_version = int.from_bytes(received_message[6:8])
    message_size = len(received_message).to_bytes(4, signed=True)
    connection.sendall(message_size+corr_id.to_bytes(4, signed=True)+(35).to_bytes(2,signed=True))
if __name__ == "__main__":
    main()
