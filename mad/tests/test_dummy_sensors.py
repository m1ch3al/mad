import unittest
from mad.drone.sensors.dummy import *


class TestDummySensors(unittest.TestCase):

    def test_dummy_gps(self):
        dummy_gps = DummySensorGPS()
        dummy_gps.initialize_sensor()
        data = dummy_gps.read_from_sensor()
        self.assertIsNotNone(data)
        print(data)

    def test_dummy_environment(self):
        dummy_environment = DummySensorEnvironment()
        dummy_environment.initialize_sensor()
        data = dummy_environment.read_from_sensor()
        self.assertIsNotNone(data)
        print(data)

    def test_dummy_sonar(self):
        dummy_sonar = DummySensorSonar()
        dummy_sonar.initialize_sensor()
        data = dummy_sonar.read_from_sensor()
        self.assertIsNotNone(data)
        print(data)

    def test_dummy_gyro_sensor(self):
        dummy_gyro = DummySensorAccelGyro()
        dummy_gyro.initialize_sensor()
        stop = False
        counter = 0
        while not stop:
            data = dummy_gyro.read_from_sensor()
            self.assertIsNotNone(data)
            print(data)
            counter += 1
            if counter >= 200:
                stop = True

if __name__ == '__main__':
    unittest.main()
