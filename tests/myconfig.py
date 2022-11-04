
import configparser

class ConfigForTest:
    sibyl_url: str = ''
    sibyl_token: str = ''
    
    def __init__(self):
        file = open('tests/config.ini', 'r')
        config = configparser.ConfigParser()
        config.read_file(file)

        self.sibyl_url = config.get('main', 'sibyl_url')
        self.sibyl_token = config.get('main', 'sibyl_token')

the_config = ConfigForTest()
