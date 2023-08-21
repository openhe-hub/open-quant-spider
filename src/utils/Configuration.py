import toml


class Configuration:
    def __init__(self, config_path: str = "../config/config.toml"):
        self.config_dict = toml.load(config_path)
        print(self.config_dict)
