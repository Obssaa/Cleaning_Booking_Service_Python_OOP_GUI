class CleaningServices:
    '''Class to represent the parent for the services'''

    # constructor
    def __init__(self, price=0.0, name=''):
        self.price = price
        self.serviceName = name

    #setters and getters

    def setprice(self, price):
        self.price = price
    def getprice(self):
        return self.price
    def setservicename(self,nam):
        self.serviceName = nam
    def getservicename(self):
        return self.serviceName

class RegularCleaning (CleaningServices):

    def __init__(self, price=0.0, name='', desc = ""):
        CleaningServices.__init__(self, price, name)
        self.description = desc

    def setdiscription(self, desc):
        self.description = desc
    def getdiscription(self):
        return self.description


class DeepCleaning (CleaningServices):

    def __init__(self, price=0.0, name='', desc = ""):
        CleaningServices.__init__(self, price, name)
        self.description = desc

    def setdiscription(self, desc):
        self.description = desc
    def getdiscription(self):
        return self.description

class WeeklyCleaning (CleaningServices):

    def __init__(self, price=0.0, name='', desc = ""):
        CleaningServices.__init__(self, price, name)
        self.description = desc

    def setdiscription(self, desc):
        self.description = desc
    def getdiscription(self):
        return self.description

class SteamCleaning (CleaningServices):

    def __init__(self, price=0.0, name='', desc = ""):
        CleaningServices.__init__(self, price, name)
        self.description = desc

    def setdiscription(self, desc):
        self.description = desc
    def getdiscription(self):
        return self.description

class Sanitization (CleaningServices):

    def __init__(self, price=0.0, name='', desc = ""):
        CleaningServices.__init__(self, price, name)
        self.description = desc

    def setdiscription(self, desc):
        self.description = desc
    def getdiscription(self):
        return self.description

class Vacuuming (CleaningServices):

    def __init__(self, price=0.0, name='', desc = ""):
        CleaningServices.__init__(self, price, name)
        self.description = desc

    def setdiscription(self, desc):
        self.description = desc
    def getdiscription(self):
        return self.description

class MonthlyCleaning (CleaningServices):

    def __init__(self, price=0.0, name='', desc = ""):
        CleaningServices.__init__(self, price, name)
        self.description = desc

    def setdiscription(self, desc):
        self.description = desc
    def getdiscription(self):
        return self.description


