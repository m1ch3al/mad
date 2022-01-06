import json
import time
from gps import *
from madis.sensors.sensor import Sensor


class BN880Sensor(Sensor):
    def __init__(self):
        Sensor.__init__(self)
        self._bn880 = None
        self._data = {"time": None, "device": None, "status": None, "mode": None, "gps-time": None,
                      "ept": None, "latitude": None, "longitude": None, "altitude": None,
                      "epx": None, "epy": None, "epv": None, "eps": None, "speed": None}

    def initialize_sensor(self):
        self._bn880 = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
        self._read_from_sensor()

    def read_from_sensor(self):
        self._read_from_sensor()
        return self._data

    def _read_from_sensor(self):
        self._data["time"] = self.get_utc_time()
        requested_data = False
        nx = self._bn880.next()
        # https://gpsd.gitlab.io/gpsd/gpsd_json.html
        if nx["class"] == "TPV":
            self._data["device"] = getattr(nx, "device", None)      # GPS connected serial device

            # GPS fix status: %d, 2=DGPS fix, 3=RTK Fixed point, 4=RTK Floating point, 5=DR fix,
            # 6=GNSSDR fix, 7=Time (surveyed) fix, 8=Simulated, 9=P(Y) fix, otherwise not present.
            # Similar to FAA Quality Indicator in NMEA.
            self._data["status"] = getattr(nx, "status", None)
            self._data["mode"] = getattr(nx, "mode", None)          # NMEA mode: %d, 0=no mode value yet seen, 1=no fix, 2=2D, 3=3D.
            self._data["gps-time"] = getattr(nx, "time", None)
            self._data["ept"] = getattr(nx, "ept", None)            # estimated error for time
            self._data["latitude"] = getattr(nx, "lat", None)
            self._data["longitude"] = getattr(nx, "lon", None)
            self._data["altitude"] = getattr(nx, "alt", None)       # meters
            self._data["epx"] = getattr(nx, "epx", None)            # estimated error for longitude
            self._data["epy"] = getattr(nx, "epy", None)            # estimated error for latitude
            self._data["epv"] = getattr(nx, "epv", None)            # estimated error for altitude
            self._data["speed"] = getattr(nx, "speed", None)        # m/sec
            self._data["eps"] = getattr(nx, "eps", None)            # estimated error for speed
