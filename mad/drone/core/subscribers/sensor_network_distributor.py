from pubsub import pub
import json
from mad.drone.utils.network import UDPClient


class SensorNetworkDistributor(object):
    def __init__(self, topic, destination, port):
        self._topic = topic
        self._destination = destination
        self._port = port
        self._udp_client = UDPClient(self._destination, self._port)
        self._udp_client.initialize_socket()
        pub.subscribe(self._receive_sensor_data, self._topic)

    def _receive_sensor_data(self, sensor_data):
        data = "{}\r\n".format(json.dumps(sensor_data))
        self._udp_client.send_data(data)

