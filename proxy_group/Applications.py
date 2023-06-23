from ProxyGroups import ProxyGroup


class Application:
    def __init__(self, name, *countries: ProxyGroup):
        self.name = name
        self.countries = countries
