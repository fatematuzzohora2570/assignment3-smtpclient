from socket import *

def smtpClient():
    mailserver = "localhost"
    port = 1025
    
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    
    recv = clientSocket.recv(1024).decode()
    print(recv)
    if not recv.startswith('220'):
        print('220 reply not received from server.')

    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if not recv1.startswith('250'):
        print('250 reply not received from server.')

    mailFrom = 'MAIL FROM: <sender@example.com>\r\n'
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    print(recv2)
    if not recv2.startswith('250'):
        print('250 reply not received from server.')

    rcptTo = 'RCPT TO: <recipient@example.com>\r\n'
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024).decode()
    print(recv3)
    if not recv3.startswith('250'):
        print('250 reply not received from server.')

    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    print(recv4)
    if not recv4.startswith('354'):
        print('354 reply not received from server.')

    msg = 'Subject: Test Message\r\n\r\nThis is a test email message sent from my Python SMTP client.\r\n.\r\n'
    clientSocket.send(msg.encode())
    recv5 = clientSocket.recv(1024).decode()
    print(recv5)
    if not recv5.startswith('250'):
        print('250 reply not received from server.')

    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()
    print(recv6)
    if not recv6.startswith('221'):
        print('221 reply not received from server.')

    clientSocket.close()

if __name__ == "__main__":
    smtpClient()
