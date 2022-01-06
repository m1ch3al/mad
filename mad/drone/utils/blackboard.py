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

from mad.drone.utils.date_time import *


class BlackBoardItem:
    def __init__(self, value_name, value, validity):
        self._value_name = value_name
        self._value = value
        self._validity = validity
        self._registering_time = date2epoch(from_str("now"))

    def get_value(self):
        if self._is_valid():
            return self._value
        return None

    def _is_valid(self):
        if self._validity == 0:
            return True
        if date2epoch(from_str("now")) - self._registering_time > self._validity:
            return False
        return True


class BlackBoard:
    class __BlackBoard:
        def __init__(self):
            self._content = dict()

        def insert_value(self, value_name, value, validity):
            self._content[value_name] = BlackBoardItem(value_name, value, validity)

        def get_value(self, value_name):
            try:
                result = self._content[value_name].get_value()
            except Exception as ex:
                result = None
            return result

        def remove_value(self, value_name):
            if value_name in self._content.keys():
                del self._content[value_name]
                return True
            else:
                return False

    instance = None

    def __init__(self):
        if not BlackBoard.instance:
            BlackBoard.instance = BlackBoard.__BlackBoard()

    @staticmethod
    def insert_value(value_name, value, validity):
        BlackBoard.instance.insert_value(value_name, value, validity)

    @staticmethod
    def get_value(value_name):
        return BlackBoard.instance.get_value(value_name)

    @staticmethod
    def is_present(value_name):
        return value_name in BlackBoard.instance._content

    @staticmethod
    def __getitem__(self, value_name):
        return BlackBoard.instance.get_value(value_name)

    @staticmethod
    def remove_value(value_name):
        return BlackBoard.instance.remove_value(value_name)
