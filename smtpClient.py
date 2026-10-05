from socket import *

def smtpClient():
    try:
        msg = "\r\n I love computer networks!"
        endmsg = "\r\n.\r\n"

        mailserver = "localhost"
        port = 1025

        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((mailserver, port))

        recv = clientSocket.recv(1024).decode()
        print(recv)
        if recv[:3] != '220':
            print('220 reply not received from server.')

        heloCommand = 'HELO Alice\r\n'
        clientSocket.send(heloCommand.encode())
        recv1 = clientSocket.recv(1024).decode()
        print(recv1)
        if recv1[:3] != '250':
            print('250 reply not received from server.')

        mailFrom = 'MAIL FROM: <sender@example.com>\r\n'
        clientSocket.send(mailFrom.encode())
        recv2 = clientSocket.recv(1024).decode()
        print(recv2)
        if recv2[:3] != '250':
            print('250 reply not received from server.')

        rcptTo = 'RCPT TO: <recipient@example.com>\r\n'
        clientSocket.send(rcptTo.encode())
        recv3 = clientSocket.recv(1024).decode()
        print(recv3)
        if recv3[:3] != '250':
            print('250 reply not received from server.')

        dataCommand = 'DATA\r\n'
        clientSocket.send(dataCommand.encode())
        recv4 = clientSocket.recv(1024).decode()
        print(recv4)
        if recv4[:3] != '354':
            print('354 reply not received from server.')

        clientSocket.send(msg.encode())
        clientSocket.send(endmsg.encode())
        recv5 = clientSocket.recv(1024).decode()
        print(recv5)
        if recv5[:3] != '250':
            print('250 reply not received from server.')

        quitCommand = 'QUIT\r\n'
        clientSocket.send(quitCommand.encode())
        recv6 = clientSocket.recv(1024).decode()
        print(recv6)
        if recv6[:3] != '221':
            print('221 reply not received from server.')

        clientSocket.close()
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    smtpClient()
