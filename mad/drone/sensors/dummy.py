"""

##     ##        ###        ########
###   ###       ## ##       ##     ##
#### ####      ##   ##      ##     ##
## ### ##     ##     ##     ##     ##
##     ##     #########     ##     ##
##     ## ### ##     ## ### ##     ## ###
##     ## ### ##     ## ### ########  ###

MAD - M1ch3al Autonomous Drone
This class belong to MADIS (M1ch3al Autonomous Drone Internal System)

       Author: SIROLA RENATO
Creation Date: 2020-06-02
       E-mail: renato.sirola@gmail.com

Content:
A dummy set of sensors for simulate data inside the DRONE.

"""

from madis.sensors.sensor import Sensor
import json
import random


class DummySensorGPS(Sensor):
    def __init__(self):
        Sensor.__init__(self)
        self._altitude = None
        self._latitude = None
        self._longitude = None
        self._heading = None
        self._speed = None
        self._status = None
        self._mode = None
        self._gps_time = None
        self._data = {"time": None, "latitude": None, "longitude": None, "altitude": None, "heading": None}

    def initialize_sensor(self):
        self._altitude = 2.5    # meters
        self._latitude = 44     # wgs84
        self._longitude = 10    # wgs84
        self._heading = 23.4    # degrees
        self._speed = 0
        self._status = "X"
        self._mode = 2
        self._gps_time = "test test"

    def read_from_sensor(self):
        self._prepare_dummy_data()
        return self._data

    def _prepare_dummy_data(self):
        self._data["latitude"] = round((self._latitude + random.random()), 6)
        self._data["longitude"] = round((self._longitude + random.random()), 6)
        self._data["altitude"] = self._altitude
        self._data["speed"] = self._speed
        self._data["status"] = self._status
        self._data["mode"] = self._mode
        self._data["heading"] = round((self._heading + random.random()), 2)
        self._data["time"] = self.get_utc_time()
        self._data["gps-time"] = self._gps_time


class DummySensorTempPressureAltitude(Sensor):
    def __init__(self):
        Sensor.__init__(self)
        self._altitude = None
        self._pressure = None
        self._temperature = None
        self._humidity = None
        self._data = {"time": None, "altitude": None, "pressure": None, "temperature": None}

    def initialize_sensor(self):
        self._altitude = 2.3           # meters
        self._pressure = 1000          # hPa (hectopascals)
        self._temperature = 27.4       # degrees
        self._humidity = random.randrange(20, 25)

    def read_from_sensor(self):
        self._prepare_dummy_data()
        return self._data

    def _prepare_dummy_data(self):
        self._data["altitude"] = self._altitude

        self._pressure = random.randrange(997, 1020)
        self._data["pressure"] = self._pressure

        self._temperature = random.randrange(28, 31)
        self._data["temperature"] = self._temperature

        self._humidity = random.randrange(20, 25)
        self._data["humidity"] = self._humidity
        self._data["time"] = self.get_utc_time()


class DummySensorSonar(Sensor):
    def __init__(self):
        Sensor.__init__(self)
        self._distance = None
        self._data = {"time": None, "distance": None}

    def initialize_sensor(self):
        self._distance = 150           # centimeters

    def read_from_sensor(self):
        self._prepare_dummy_data()
        json_data = json.dumps(self._data)
        return json_data

    def _prepare_dummy_data(self):
        self._data["distance"] = self._distance
        self._data["time"] = self.get_utc_time()


class DummySensorAccelGyro(Sensor):
    def __init__(self):
        Sensor.__init__(self)
        self._acc_x = None
        self._acc_y = None
        self._acc_z = None
        self._gyro_x = None
        self._gyro_y = None
        self._gyro_z = None
        self._data = {"time": None, "acceleration_x": None, "acceleration_y": None, "acceleration_z": None,
                      "gyroscope_x": None, "gyroscope_y": None, "gyroscope_z": None}

    def initialize_sensor(self):
        self._acc_x = random.random()
        self._acc_y = random.random()
        self._acc_z = random.random()
        self._gyro_x = random.random()
        self._gyro_y = random.random()
        self._gyro_z = random.random()

    def read_from_sensor(self):
        self._prepare_dummy_data()
        return self._data

    def _prepare_dummy_data(self):
        self._data["acceleration_x"] = random.random()
        self._data["acceleration_y"] = random.random()
        self._data["acceleration_z"] = random.random()
        self._data["gyroscope_x"] = random.random()
        self._data["gyroscope_y"] = random.random()
        self._data["gyroscope_z"] = random.random()
        self._data["time"] = self.get_utc_time()
