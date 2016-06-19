from infoset.toolbox import FILE_LOCATION
import yaml


class Oui(object):
    def __init__(self, mac_address=None):
        self.vendors = {}
        with open(FILE_LOCATION, 'r') as file:
            self.vendors = yaml.load(file)
        self.mac = mac_address.lower()

    def get_vendor(self, mac_address=None):
        if mac_address:
            return self.vendors[mac_address]
        elif self.mac:
            return self.vendors[self.mac]
        else:
            print('No MAC address specified')
