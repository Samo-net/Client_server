# server.py
import socket
import threading

def handle_client(client_socket, client_address):
    """Handles communication with a single client."""
    try:
        print(f"Accepted connection from {client_address}")
        request = client_socket.recv(1024).decode('utf-8')
        print(f"Received: {request}")

        response = "Server says: Message received!"
        client_socket.send(response.encode('utf-8'))

    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()
        print(f"Connection with {client_address} closed.")

def start_server(host='127.0.0.1', port=12345):
    """Starts the server and listens for client connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Listen for up to 5 connections
    print(f"Server listening on {host}:{port}")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()

    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()

