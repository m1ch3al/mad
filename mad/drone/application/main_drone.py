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

import threading

from mad.drone.utils.blackboard import BlackBoard
from mad.drone.utils.configuration_reader import read_multiple_file_configuration, instantiate_class
from mad.drone.utils.fileystem import *
from mad.drone.utils.logger import *

CONFIG_FOLDER = ".mad"
CONFIGURATION_FILENAME = "default.configuration.yaml"
LOGGER_FILENAME = "logger.configuration.yaml"


def main():
    blackboard = BlackBoard()
    config_dir = "{}/{}".format(os.path.expanduser("~"), CONFIG_FOLDER)
    logger_configuration_fullpath = "{}/{}".format(config_dir, LOGGER_FILENAME)
    logger = create_logger("mad.drone.application.main_drone.main()", logger_configuration_fullpath)
    configuration_fullpath = "{}/{}".format(config_dir, CONFIGURATION_FILENAME)
    drone_configuration = read_yaml_configuration(configuration_fullpath)
    if drone_configuration is not None:
        blackboard.insert_value("configuration", drone_configuration, 0)
    else:
        logger.fatal("The configuration was not loaded....exiting")
        return -1
    logger.debug("Start parsing configuration")

    drone_configuration = read_multiple_file_configuration(config_dir)

    # Lists of network subscribers
    for element in drone_configuration["network-configuration"]:
        module_name = element["udp-client-configuration"]["distributor-module"]
        class_name = element["udp-client-configuration"]["distributor-class"]
        parameters = element["udp-client-configuration"]["parameters"]
        distributor = instantiate_class(class_name, module_name, parameters)
        blackboard.insert_value(element["udp-client-configuration"]["name"], distributor, 0)

    # start publishers
    for element in drone_configuration["sensors-configuration"].copy():
        sensor_config = drone_configuration["sensors-configuration"][element]
        try:
            publisher_module = sensor_config["publisher-module"]
            publisher_class = sensor_config["publisher-class"]
            publisher_instance = instantiate_class(publisher_class, publisher_module, [sensor_config])
            drone_configuration["sensors-configuration"]["publisher"] = publisher_instance
            publisher_thread = threading.Thread(target=publisher_instance.start_publishing, args=())
            publisher_thread.setDaemon(True)
            publisher_thread.start()
        except Exception as ex:
            pass

    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
