import json
import time

import mma845x
from madis.sensors.sensor import Sensor


class MMA845XSensor(Sensor):
    def __init__(self):
        Sensor.__init__(self)
        self._mma845x = None
        self._data = {"time": None, "acceleration_x": None, "acceleration_y": None, "acceleration_z": None}

    def initialize_sensor(self):
        self._mma845x = mma845x.MMA845X(0x1C)
        self._read_from_sensor()

    def read_from_sensor(self):
        self._read_from_sensor()
        return self._data

    def _read_from_sensor(self):
        self._data["time"] = self.get_utc_time()
        self._mma845x.read()
        self._data["acceleration_x"] = self._mma845x.x
        self._data["acceleration_y"] = self._mma845x.y
        self._data["acceleration_z"] = self._mma845x.z
