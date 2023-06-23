import re

class ProxyGroup:
    def get_match_rules(self,match_rules,proxy_list):
        match_rules = [re.compile(r) for r in match_rules]
        return [p for p in proxy_list if any(r.match(p) for r in match_rules)]

    def __init__(self,name,match_rules,proxy_list):
        self.name = name
        self.proxy_list = self.get_match_rules(match_rules,proxy_list)