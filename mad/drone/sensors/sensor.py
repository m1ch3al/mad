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

from abc import ABC, abstractmethod
from mad.drone.utils.date_time import from_str, date2epoch


class Sensor(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def initialize_sensor(self):
        pass

    @abstractmethod
    def read_from_sensor(self):
        pass

    def get_utc_time(self):
        return date2epoch(from_str("now", is_utc=True))
