import json
import socket

def save_to_file(data, filename="user_info.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

HOST = "evender.co"
PORT = 3000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server is listening on {HOST}:{PORT}...")

while True:
    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")

    data = b""
    while True:
        chunk = conn.recv(1024)
        if not chunk:
            break
        data += chunk

    if not data:
        continue

    try:
        json_data = json.loads(data.decode('utf-8'))
        save_to_file(json_data)  # Save JSON for Ticketmaster

        print("Received and saved JSON:", json_data)

        conn.sendall(b"JSON saved!")  

    except json.JSONDecodeError:
        print("Invalid JSON received")
        conn.sendall(b"Invalid JSON")

    conn.close()
