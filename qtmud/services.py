import select
import socket

import qtmud
from qtmud import txt
from qtmud.builders import build_client



class MUDSocket(object):
    """ Handles a socket service. """
    def __init__(self):
        self.logging_in = set()
        self.clients = dict()
        self.connections = list()
        self.ip4_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip4_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.ip6_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.ip6_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    def start(self, ip4_address=None, ip6_address=None):
        qtmud.log.info('start()ing MUDsocket')
        if not ip4_address and hasattr(qtmud, 'IP4_ADDRESS'):
                ip4_address = qtmud.IP4_ADDRESS
        if not ip6_address and hasattr(qtmud, 'IP6_ADDRESS'):
                ip6_address = qtmud.IP6_ADDRESS
        if not ip4_address and not ip6_address:
            qtmud.log.error('No address set, make sure either IP6_ADDRESS '
                            'or IP4_ADDRESS is not None.')
            return False
        if ip4_address:
            qtmud.log.debug('trying to bind() MUDSocket to address %s',
                           ip4_address)
            try:
                self.ip4_socket.bind(ip4_address)
                self.ip4_socket.listen(5)
                self.connections.append(self.ip4_socket)
                qtmud.log.info('MUDSocket successfully bound to %s', ip4_address)
            except OSError as err:
                qtmud.log.error('MUDSocket failed to bind to %s, error: %s',
                                ip4_address, err)
        if ip6_address:
            qtmud.log.debug('trying to bind() MUDSocket to address %s',
                           ip6_address)
            try:
                self.ip6_socket.bind(ip6_address)
                self.ip6_socket.listen(5)
                self.connections.append(self.ip6_socket)
                qtmud.log.info('MUDSocket successfully bound to %s',
                               ip6_address)
            except OSError as err:
                qtmud.log.error('MUDSocket failed to bind to %s, error: %s',
                                ip6_address, err)
        if len(self.connections) == 0:
            return False
        return True

    def tick(self):
        read, write, error = select.select(self.connections,
                                           [conn for conn,
                                            client in self.clients.items() if
                                            client.send_buffer != ''],
                                           [],
                                           0)
        if read:
            for conn in read:
                if conn is self.ip4_socket or conn is self.ip6_socket:
                    new_conn, addr = conn.accept()
                    qtmud.log.debug('new connection accepted from %s', format(addr))
                    client = build_client()
                    client.update({'addr': addr,
                                   'send_buffer': '',
                                   'recv_buffer': ''})
                    self.connections.append(new_conn)
                    self.clients[new_conn] = client
                    client.input_parser = 'client_login_parser'
                    qtmud.schedule('send',
                                   recipient=client,
                                   text=qtmud.SPLASH)
                else:
                    data = conn.recv(1024)
                    if data == b'':
                        self.connections.remove(conn)
                        qtmud.log.debug('lost connection from %s',
                                        format(self.clients[conn].addr))
                        qtmud.schedule('client_disconnect',client=self.clients[
                            conn])
                    else:
                        client = self.clients[conn]
                        client.recv_buffer += data.decode('utf8', 'ignore')
                        if '\n' in client.recv_buffer:
                            split = client.recv_buffer.rstrip().split('\n', 1)
                            if len(split) == 2:
                                line, client.recv_buffer = split
                            else:
                                line, client.recv_buffer = split[0], ''
                            qtmud.schedule('client_input_parser',
                                           client=client, line=line)
        if write:
            for conn in write:
                conn.send(self.clients[conn].send_buffer.encode('utf8'))
                self.clients[conn].send_buffer = ''
        return True


class Talker(object):
    """ The Talker service handles the global chat channels. """
    def __init__(self):
        self.channels = {'one': list()}
        self.history = {'one': list()}

    def tune_in(self, client, channel):
        self.channels[channel].append(client)
        client.channels.append(channel)

    def start(self):
        return

    def tick(self):
        return