import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(s)

server = 'google.com'
port = 80

server_ip = socket.gethostbyname(server)
print(server_ip)

request = "GET / HTTP/1.1\nHost: " + server + "\n\n"

s.connect((server, port))
s.send(request.encode())
result = s.recv(4096)

#print(result)

while (len(result) > 0):
    print(result)
    result = s.recv(1024)
