import socket

def main():
    # 2번 PC의 IP 주소 및 포트 번호 (2번 PC의 IP 주소로 변경해주세요!)
    HOST = '192.168.1.131'
    PORT = 65432
   
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            message = "Hello"
            if message.lower() == 'exit':
                break
            s.sendall(message.encode())

if __name__ == "__main__":
    main()

