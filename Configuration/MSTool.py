from Crypto.Cipher import AES
import wmi
import base64
import os
import configparser
import requests

class AutoConfigParser(configparser.ConfigParser):
    def optionxform(self, optionstr):
        return optionstr

    def remove_note(self):
        section_list = self.sections()
        for section in section_list:
            for k, v in self.items(section):
                self.set(section, k, v.split('#', 1)[0].strip())