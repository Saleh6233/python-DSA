import socket
import threading
from typing import Tuple


class TCPServer:
    def __init__(self, host: str = "localhost", port: int = 6379) -> None:

        # Create a TCP/IP Socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Reuse the address/port quickly after restart
        self.server_socket.setsockopt(
            socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))  # Bind the socket
        # Handle 5 connections at a time
        self.server_socket.listen(5)  # Now listen

        print(f"Server listening on {host}:{port}")

    def handle_client(self, conn: socket.socket, addr: Tuple[str, int]) -> None:
        print(f"Connected by {addr}")
        buffer = b""
        try:
            while True:
                # data = conn.recv(1024).decode().strip()

                # if not data:
                #     break

                # if data.upper() == "PING":
                #     conn.send(b"+PONG\r\n")

                # else:
                #     conn.send("-ERR Unknown command\r\n")
                chunk = conn.recv(1024)
                if not chunk:
                    break
                buffer += chunk

                # Process full lines only (line ends with '\n')
                while b"\n" in buffer:
                    line, buffer = buffer.split(b"\n", 1)
                    cmd = line.rstrip(b"\r").decode(
                        "utf-8", errors="replace").strip()
                    if not cmd:
                        continue

                    print(f"Received from {addr}: {cmd!r}")
                    if cmd.upper() == "PING":
                        conn.sendall(b"+PONG\r\n")
                    else:
                        conn.sendall(b"-ERR Unknown command\r\n")
        except Exception as e:
            conn.send(f"-ERR {str(e)}\r\n".encode())
            # try:
            #     conn.sendall(f"-ERR {e}\r\n".encode())
            # except Exception:
            #     pass
        finally:
            conn.close()
            print(f"Disconnected: {addr}")

    def run(self) -> None:
        """Accept incoming client connections and spin up new threads to handle them """
        try:  # In case there is unforeseen error
            while True:  # Listen for every connection

                conn, addr = self.server_socket.accept()
                thread = threading.Thread(
                    target=self.handle_client, args=(conn, addr), daemon=True)
                thread.start()

        except KeyboardInterrupt:
            print("\nShutting down server....")
        finally:
            self.server_socket.close()
            print("Server socket closed.")


if __name__ == "__main__":
    server = TCPServer()
    server.run()
