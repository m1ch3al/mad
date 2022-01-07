from mad.drone.utils.blackboard import BlackBoard
from mad.drone.utils.fileystem import read_yaml_configuration
import importlib


def instantiate_class(class_name, module_name, constructor_parameters):
    try:
        module = importlib.import_module(module_name)
        class_ = getattr(module, class_name)
        class_instantiated = class_(*constructor_parameters)
        return class_instantiated
    except Exception as ex:
        message = (
            f"Introspection Exception : try to create {class_name} from {module_name}, with parameters ["
            + ", ".join(map(str, constructor_parameters))
            + "]\n"
        )
        message += "Cannot instantiate the requested object class : " + str(ex)
        raise Exception(message)


def read_multiple_file_configuration(config_dir):
    blackboard = BlackBoard()
    drone_configuration = blackboard.get_value("configuration")

    for sensor_name in drone_configuration["sensors-configuration"]:
        sensor_filename = drone_configuration["sensors-configuration"][sensor_name]
        if sensor_filename is not None:
            sensor_configuration = read_yaml_configuration("{}/{}".format(config_dir, sensor_filename))
            drone_configuration["sensors-configuration"][sensor_name] = sensor_configuration
        else:
            drone_configuration["sensors-configuration"][sensor_name] = None

    blackboard.insert_value("configuration", drone_configuration, 0)
    return drone_configuration
