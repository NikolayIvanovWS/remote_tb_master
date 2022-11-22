import time
import paramiko
from scp import SCPClient

def install_to_one_tb(host, username, passwd):

    print("Connecting to {}".format(host))

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.load_system_host_keys()
    client.connect(hostname=host, username=username, password=passwd,
                     look_for_keys=False, allow_agent=False)

    print("\n sending bash-file to {}".format(host))

    scp = SCPClient(client.get_transport()) 

    bash_file_name=  'test.bash' #вводим название bash-файла

    scp.put('./bin/test.bash', bash_file_name) #указываем путь к файлу

    scp.close()

    print("\n finish sending bash-file to {}".format(host))

    print("\n Running bash-file \n")

    stdin, stdout, stderr = client.exec_command("bash test.bash"
                                                , timeout=15, get_pty=True) #вводим команды для выполнения на роботе
    print(str(stdout.read() + stderr.read(), 'utf-8'))

    stdin.flush()
    time.sleep(10)

    print("Finish with {}".format(host))

    client.close()

if __name__ == "__main__":

    username = 'pi'
    passwd = 'brobro'

    robots = ['turtlebro01.local', 'turtlebro15.local'] #можно указать одного робота, либо же несколько роботов

    for host in robots:
        install_to_one_tb(host, username, passwd)