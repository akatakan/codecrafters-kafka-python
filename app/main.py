import socket  # noqa: F401


def main():

    print("Logs from your program will appear here!")

    server = socket.create_server(("localhost", 9092), reuse_port=True)
    connection,_ = server.accept() # wait for client
    connection.sendall((0).to_bytes(4, signed=True) + (7).to_bytes(4, signed=True))  # send 0 to client


if __name__ == "__main__":
    main()
