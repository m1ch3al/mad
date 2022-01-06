import json
import time

import adafruit_bme280
import board
import busio
from madis.sensors.sensor import Sensor


class BME280Sensor(Sensor):
    def __init__(self):
        Sensor.__init__(self)
        self._i2c = None
        self._bme280 = None

        self._altitude = None
        self._pressure = None
        self._temperature = None
        self._humidity = None
        self._data = {"time": None, "altitude": None, "pressure": None, "temperature": None, "humidity": None}

    def initialize_sensor(self):
        # Create library object using our Bus I2C port
        self._i2c = busio.I2C(board.SCL, board.SDA)
        self._bme280 = adafruit_bme280.Adafruit_BME280_I2C(self._i2c)
        # Change this to match the location's pressure (hPa) at sea level
        self._bme280.sea_level_pressure = 1013.25
        self._bme280.mode = adafruit_bme280.MODE_NORMAL
        self._bme280.standby_period = adafruit_bme280.STANDBY_TC_500
        self._bme280.iir_filter = adafruit_bme280.IIR_FILTER_X16
        self._bme280.overscan_pressure = adafruit_bme280.OVERSCAN_X16
        self._bme280.overscan_humidity = adafruit_bme280.OVERSCAN_X1
        self._bme280.overscan_temperature = adafruit_bme280.OVERSCAN_X2
        # The sensor will need a moment to gather initial readings
        time.sleep(2)
        self._altitude = self._bme280.altitude          # meters
        self._pressure = self._bme280.pressure          # hPa (hectopascals)
        self._temperature = self._bme280.temperature    # celsius
        self._humidity = self._bme280.humidity          # Percentage

    def read_from_sensor(self):
        self._altitude = self._bme280.altitude          # meters
        self._pressure = self._bme280.pressure          # hPa (hectopascals)
        self._temperature = self._bme280.temperature    # celsius
        self._humidity = self._bme280.humidity          # Percentage
        self._data["time"] = self.get_utc_time()
        self._data["altitude"] = round(self._altitude, 3)
        self._data["pressure"] = round(self._pressure, 3)
        self._data["temperature"] = round(self._temperature, 3)
        self._data["humidity"] = round(self._humidity, 3)
        return self._data

