import os
from file_reader import YamlReader

BAES_PATH = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '\..')
CONFIG_FILE = BAES_PATH + '\\config\\conf.yml'
DATA_PATH = BAES_PATH + '\\data\\'
DRIVER_PATH = BAES_PATH + '\\drivers\\'
LOG_PATH = BAES_PATH + '\\report\\'


class Config:
    '''读取配置'''
    def __init__(self, config=CONFIG_FILE):
        self.config = YamlReader(config).data

    def get(self, element, index=0):
        return self.config[index].get(element)
