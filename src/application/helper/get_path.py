import configparser
import os


class Helper(object):
    @staticmethod
    def get_key(key) -> str:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
        conf_path = rf"{base_path}\src\application\helper\variables.ini"
        environment = os.environ.get("ENVIRONMENT", "LOCAL").upper()
        _config = configparser.ConfigParser()
        _config.read(conf_path)
        env_value = os.environ.get(key.upper())
        if env_value:
            return env_value
        else:
            return _config[environment.upper()][key.upper()]
