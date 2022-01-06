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

from mad.drone.sensors.sensor import Sensor
import random
import json
from mad.drone.utils.date_time import from_str


class DummySensorGPS(Sensor):
    def __init__(self):
        Sensor.__init__(self)
        self._gps_time = None
        self._altitude = None
        self._latitude = None
        self._longitude = None
        self._speed = None
        self._satellites = None
        self._hdop = None
        self._mode = None
        self._data = {"time": None, "latitude": None, "longitude": None, "altitude": None, "speed": None,
                      "satellites": None, "hdop": None, "mode": None}

    def initialize_sensor(self):
        pass

    def read_from_sensor(self):
        self._prepare_dummy_data()
        return self._data

    def _prepare_dummy_data(self):
        self._altitude = round(random.uniform(2, 3), 2)    # meters
        self._latitude = round(random.uniform(44.078756, 44.078841), 6)    # wgs84
        self._longitude = round(random.uniform(10.011701, 10.012065), 6)   # wgs84
        self._speed = 0
        self._hdop = round(random.uniform(0.8, 1.5), 1)
        self._mode = 1
        self._satellites = random.randint(9, 14)
        self._gps_time = from_str("now", is_utc=True)

        self._data["time"] = self._gps_time
        self._data["latitude"] = self._latitude
        self._data["longitude"] = self._longitude
        self._data["altitude"] = self._altitude
        self._data["speed"] = self._speed
        self._data["satellites"] = self._satellites
        self._data["hdop"] = self._hdop
        self._data["mode"] = self._mode


class DummySensorEnvironment(Sensor):
    def __init__(self):
        Sensor.__init__(self)
        self._pressure = None
        self._temperature = None
        self._humidity = None
        self._data = {"humidity": None, "pressure": None, "temperature": None}

    def initialize_sensor(self):
        pass

    def read_from_sensor(self):
        self._prepare_dummy_data()
        return self._data

    def _prepare_dummy_data(self):
        self._pressure = round(random.uniform(1015.20, 1015.30), 6)     # hPa (hectopascals)
        self._temperature = round(random.uniform(24.1, 24.7), 2)        # degrees
        self._humidity = round(random.uniform(38, 40), 3)               # percentage
        self._data["pressure"] = self._pressure
        self._data["temperature"] = self._temperature
        self._data["humidity"] = self._humidity


class DummySensorSonar(Sensor):
    def __init__(self):
        Sensor.__init__(self)
        self._distance = None
        self._data = {"distance": None}

    def initialize_sensor(self):
        pass

    def read_from_sensor(self):
        self._prepare_dummy_data()
        return self._data

    def _prepare_dummy_data(self):
        self._distance = round(random.uniform(150, 152), 6)           # centimeters
        self._data["distance"] = self._distance


class DummySensorAccelGyro(Sensor):
    def __init__(self):
        Sensor.__init__(self)
        self._acc_x = None
        self._acc_y = None
        self._acc_z = None
        self._gyro_x = None
        self._gyro_y = None
        self._gyro_z = None
        self._euler_x = None
        self._euler_y = None
        self._euler_z = None
        self._quaternion_a = None
        self._quaternion_b = None
        self._quaternion_c = None
        self._quaternion_d = None
        self._linear_acc_x = None
        self._linear_acc_y = None
        self._linear_acc_z = None
        self._data = {"acc_x": None, "acc_y": None, "acc_z": None,
                      "gyro_x": None, "gyro_y": None, "gyro_z": None,
                      "euler_x": None, "euler_y": None, "euler_z": None,
                      "quaternion_a": None, "quaternion_b": None, "quaternion_c": None, "quaternion_d": None,
                      "linear_acc_x": None, "linear_acc_y": None, "linear_acc_z": None}

    def initialize_sensor(self):
        pass

    def read_from_sensor(self):
        self._prepare_dummy_data()
        return self._data

    def _prepare_dummy_data(self):
        self._acc_x = round(random.uniform(-0.01, 0.04), 2)
        self._acc_y = round(random.uniform(-0.01, 0.04), 2)
        self._acc_z = round(random.uniform(-9, -10), 2)
        self._data["acc_x"] = self._acc_x
        self._data["acc_y"] = self._acc_y
        self._data["acc_z"] = self._acc_z

        self._gyro_x = round(random.uniform(-0.01, 0.04), 10)
        self._gyro_y = round(random.uniform(-0.01, 0.04), 10)
        self._gyro_z = round(random.uniform(-0.01, 0.04), 10)
        self._data["gyro_x"] = self._gyro_x
        self._data["gyro_y"] = self._gyro_y
        self._data["gyro_z"] = self._gyro_z

        self._euler_x = round(random.uniform(-0.01, 0.04), 4)
        self._euler_y = round(random.uniform(-0.01, 0.04), 4)
        self._euler_z = round(random.uniform(-0.01, 0.04), 4)
        self._data["euler_x"] = self._euler_x
        self._data["euler_y"] = self._euler_y
        self._data["euler_z"] = self._euler_z

        self._quaternion_a = round(random.uniform(-0.01, 0.4), 10)
        self._quaternion_b = round(random.uniform(-0.01, 0.4), 10)
        self._quaternion_c = round(random.uniform(-0.01, 0.4), 10)
        self._quaternion_d = round(random.uniform(-0.01, 0.4), 10)
        self._data["quaternion_a"] = self._quaternion_a
        self._data["quaternion_b"] = self._quaternion_b
        self._data["quaternion_c"] = self._quaternion_c
        self._data["quaternion_d"] = self._quaternion_d

        self._linear_acc_x = round(random.uniform(-0.01, 0.04), 2)
        self._linear_acc_y = round(random.uniform(-0.01, 0.04), 2)
        self._linear_acc_z = round(random.uniform(-0.01, 0.04), 2)
        self._data["linear_acc_x"] = self._linear_acc_x
        self._data["linear_acc_y"] = self._linear_acc_y
        self._data["linear_acc_z"] = self._linear_acc_z



