"""
----------------------------------------------------------------------------
    ##     ##        ###        ########
    ###   ###       ## ##       ##     ##
    #### ####      ##   ##      ##     ##
    ## ### ##     ##     ##     ##     ##
    ##     ##     #########     ##     ##
    ##     ## ### ##     ## ### ##     ## ###
    ##     ## ### ##     ## ### ########  ###

MAD - M1ch3al Autonomous Drone

Author: SIROLA RENATO
 Email: renato.sirola@gmail.com
----------------------------------------------------------------------------
"""

import socket


class UDPClient(object):
    def __init__(self, destination, port):
        self._destination = destination
        self._port = port
        self._udp_client_socket = None
        self._target = None

    def initialize_socket(self):
        self._udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self._target = (self._destination, self._port)

    def send_data(self, data_to_send):
        encoded_data = str.encode(data_to_send)
        self._udp_client_socket.sendto(encoded_data, self._target)
