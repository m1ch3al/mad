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

from mad.drone.utils.fileystem import *
from mad.drone.utils.logger import *
from mad.drone.utils.blackboard import BlackBoard


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


if __name__ == "__main__":
    main()
