from socket import *
from time import sleep
import random
import json

serverName = '255.255.255.255'
serverPort = 12000
sensorName = "MySensor"

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:
    RoomNo = "O1.21"
    temp_C = random.randint(0, 30)
    day = "Monday"
    message = {"RoomNo": RoomNo, "temp_C": temp_C, "day": day}
    clientSocket.sendto(json.dumps(message).encode(), (serverName, serverPort))
    print("Sent message: " + json.dumps(message))
    sleep(0.5)
clientSocket.close()