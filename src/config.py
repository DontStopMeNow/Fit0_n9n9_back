import os
from os.path import abspath, join, dirname


class Config:
    def __init__(self):
        self.config = {}

    def write_from_env(self):
        for key in self.config:
            if key in os.environ:
                self.config[key] = os.environ[key]


class DevConfig(Config):
    def __init__(self):
        super()
        self.config = {
            "APP_PORT": 8080,
            "APP_HOST": "0.0.0.0",
            "HINT": "В питере пить",
            "SECRET": "cider"
        }
        self.write_from_env()
