class Oui(object):
    def __init__(self, mac_address=None):
        self.mac = mac_address.lower()

    def get_vendor(self, mac_address=None):
        if mac_address:
            return vendors[mac_address]
        else:
            return vendors[self.mac]
