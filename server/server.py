import logging
import socket

logging.basicConfig(
    filename="logs/server.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)


class Server:
    """
    This script is seperate from the entire client-end project
    and is not intended for the client to use this script.
    """

    def __init__(self):
        # Declaring server IP and port
        self.SERVER_IP: str = "10.0.0.162"
        self.SERVER_PORT: int = 4000

        self.start_server()

    def start_server(self):
        try:
            # Starting server
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.s.bind((self.SERVER_IP, self.SERVER_PORT))
            print(f"Server Started succesfully on {self.SERVER_IP}:{self.SERVER_PORT}")
            logging.info("server started succesfully")
        except Exception as e:
            print(f"Server could not start.\n\nReason:\n{e}")
            logging.exception("Exception occured")
            return
        while True:
            # Wait for message from client
            data, client_address = self.s.recvfrom(1024)
            data = data.decode("utf-8")
            logging.info("got data")
            print(f"Message received from: {str(client_address)}")

            if "sent" in data:
                text = data.split("|")[-1]
                with open("data/database.json", "w") as database:
                    database.write(text)
                    logging.info("downloaded data")
                self.s.sendto("Success".encode("utf-8"), client_address)
                logging.info("sent response")
            elif data == "download":
                self.send_databse(client=client_address)

    def send_database(self, client):
        with open("data/database.json", "r") as database:
            text = database.readall()
            self.s.sendto(text.encode("utf-8"), client)
            logging.info("sent data")


if __name__ == "__main__":
    Server()
