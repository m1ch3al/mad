from time import sleep

from pubsub import pub

from mad.drone.utils.configuration_reader import instantiate_class


class SensorPublisher(object):
    def __init__(self, configuration):
        self._configuration = configuration
        self._topic = configuration["configuration-name"]
        self._sensor = None
        self._create_sensor()
        self._sleep_interval = 1/configuration["frequency"]
        self._stop = False

    def _create_sensor(self):
        sensor_class = self._configuration["sensor-class"]
        sensor_module = self._configuration["sensor-module"]
        sensor_parameters = self._configuration["sensor-parameters"]
        self._sensor = instantiate_class(sensor_class, sensor_module, sensor_parameters)
        self._sensor.initialize_sensor()

    def start_publishing(self):
        while not self._stop:
            data = self._sensor.read_from_sensor()
            pub.sendMessage(self._topic, sensor_data=data)
            sleep(self._sleep_interval)

    def stop_publish(self):
        self._stop = True
