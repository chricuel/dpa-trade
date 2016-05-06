from sshtunnel import SSHTunnelForwarder
from time import sleep

with SSHTunnelForwarder(
    ('96.126.98.33', 22),
    ssh_username="root",
    ssh_password="J*1n!d_$W0",
    remote_bind_address=('127.0.0.1', 5432)
) as server:

    print(server.local_bind_port)
    print dir(server)
    while True:
        # press Ctrl-C for stopping
        sleep(1)

print('FINISH!')