import re


class ProxyGroup:

    def get_match_rules(self, match_rules, proxy_list):
        result = []
        for rule in match_rules:
            if rule.startswith('!'):
                result = [proxy for proxy in proxy_list if not re.search(rule[1:], proxy.name)]
            else:
                result = [proxy for proxy in proxy_list if re.search(rule, proxy.name)]
        return result

    def __init__(self, name, match_rules, proxy_dict:dict):
        self.name = name
        self.proxy_list = self.get_match_rules(match_rules, proxy_dict)
