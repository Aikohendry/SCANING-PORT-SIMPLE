import socket
import pyfiglet

ascii_banner = pyfiglet.figlet_format("SIMPLE SCANING PORT ")
print(ascii_banner)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = input(str("Masukan IP yang akan dicek portnya : ")) 

def pscan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

for x in range(79,81):
    if pscan(x):
        print('Port',x,'is open')
    else:
        print ('port',x,'is closed') 