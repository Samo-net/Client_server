# client.py
import socket

def send_request(host='127.0.0.1', port=12345, message="Hello from client!"):
    """Sends a request to the server and receives the response."""
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        client_socket.send(message.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Received from server: {response}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'client_socket' in locals():
            client_socket.close()

if __name__ == "__main__":
    send_request()