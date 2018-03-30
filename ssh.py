import paramiko
import cryptography
def main():
	print("""
\033[0;31m	██████╗ ██╗   ██╗    ███████╗███████╗██╗  ██╗
	██╔══██╗╚██╗ ██╔╝    ██╔════╝██╔════╝██║  ██║
	██████╔╝ ╚████╔╝     ███████╗███████╗███████║
	██╔═══╝   ╚██╔╝      ╚════██║╚════██║██╔══██║
	██║        ██║       ███████║███████║██║  ██║
	╚═╝        ╚═╝       ╚══════╝╚══════╝╚═╝  ╚═╝
\033[0m	    SSH Client written by @Wardriving         """)
	server = input("Server: ")
	port = int(input("Port: "))
	username = input("User: ")
	password = input("Password: ")
	while True:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(server, port=port, username=username, password=password)
		ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(input(username + "@" + server + "# "))
		print(ssh_stdout.read().decode('utf-8'))
		ssh.close
try:
	main()
except KeyboardInterrupt:
	print("\nInterrupted")
