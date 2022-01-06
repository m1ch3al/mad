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

import os
import os.path
import yaml
from mad.drone.utils.logger import get_logger


def read_yaml_configuration(filename):
    logger = get_logger("mad.drone.utils.filesystem.read_yaml_configuration()")
    if file_exist(filename):
        logger.info("File exist....start reading configuration [{}]".format(filename))
        with open(filename, "r") as file_descriptor:
            yaml_data = yaml.load(file_descriptor, Loader=yaml.FullLoader)
            logger.info("Configuration read successfully")
            return yaml_data
    logger.error("[{}] not found - unable to load drone configuration".format(filename))
    return None


def read_full_text_file(file_name):
    if not os.path.exists(file_name):
        raise Exception("File specified doesn't exist - : " + file_name)
    else:
        stop = False
        file_descriptor = open(file_name, "r")
        sentences = []
        while not stop:
            line = file_descriptor.readline()
            if len(line) == 0:
                stop = True
            else:
                sentences.append(line)
        file_descriptor.close()
        return sentences


def create_folder(folder_to_create):
    if not os.path.exists(folder_to_create):
        os.makedirs(folder_to_create)


def file_exist(file_path):
    return os.path.exists(file_path) and os.path.isfile(file_path)


def directory_exist(path):
    return os.path.exists(path) and os.path.isdir(path)


def get_directory_from_filepath(file_path):
    absolute_path = os.path.abspath(file_path)
    return os.path.dirname(absolute_path)


def is_absolute_filepath(filepath):
    absolute_file_path = os.path.abspath(filepath)
    if file_exist(absolute_file_path):
        return True, absolute_file_path
    return False, None




