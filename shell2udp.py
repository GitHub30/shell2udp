import socket
from subprocess import Popen
from argparse import ArgumentParser


def serve():
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8080, type=int)
    parser.add_argument('command', nargs='+')
    args = parser.parse_args()

    if len(args.command) % 2:
        args.command = [''] + args.command

    routes = {}
    for path, command in zip(args.command[0::2], args.command[1::2]):
        print(f'echo {path} > /dev/udp/localhost/{args.port}', command)
        routes[path.encode('UTF-8')] = command
        routes[f'{path}\n'.encode('UTF-8')] = command

    with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as s:
        s.bind(('', args.port))

        while(True):
            bytes, addr = s.recvfrom(1024)
            print(bytes, addr)
            if bytes in routes:
                Popen(routes[bytes], shell=True)


if __name__ == '__main__':
    serve()
