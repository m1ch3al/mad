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

import yaml
import logging
import logging.config
import os
import time


def create_logger(logger_name, logger_config_file):
    if os.path.exists(logger_config_file):
        with open(logger_config_file, "rt") as f:
            try:
                config = yaml.safe_load(f.read())
                config["handlers"]["file_handler"]["filename"] = time.strftime(config["handlers"]["file_handler"]["filename"])
                prepare_logging_directory(config["handlers"]["file_handler"]["filename"])
                logging.config.dictConfig(config)
                logger = logging.getLogger(logger_name)
                logger.debug("Logger initialized with this CONFIG-FILE:" + str(logger_config_file))
                return logger
            except Exception as ex:
                print(ex)
                print('Error in Logging Configuration. Using default configs')
                return create_default_file_logger()
    else:
        raise Exception("The logger configuration file, '{}' does not exist".format(logger_config_file))


def create_default_file_logger(filename):
    import time
    import logging
    from logging import FileHandler
    log_filename = "/tmp/" + time.strftime("%Y%m%dT%H%M%S_") + "_" + filename
    file_handler = FileHandler(log_filename)
    formatter = logging.Formatter("%(asctime)s - [%(levelname)s] : %(message)s", "%Y-%m-%d %H:%M:%S")
    file_handler.setFormatter(formatter)
    logger = logging.getLogger("default_file_logger")
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    return logger


def prepare_logging_directory(filepath):
    abs_path = os.path.abspath(filepath)
    logging_directory = os.path.dirname(abs_path)
    check_result = os.path.exists(logging_directory) and os.path.isdir(logging_directory)
    if not check_result and not os.path.exists(logging_directory):
        os.makedirs(logging_directory)


def get_logger(logger_name):
    return logging.getLogger(logger_name)