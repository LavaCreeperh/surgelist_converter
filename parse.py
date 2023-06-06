def parse_info(info_string):
    fields = info_string.split(',')
    result_dict = {}
    # 处理特殊字段
    server_info = fields[0].split('=')
    result_dict['name'] = server_info[0].strip()
    result_dict['method'] = server_info[1].strip()
    result_dict['address'] = fields[1].strip()
    result_dict['port'] = fields[2].strip()
    # 对于每一个字段，我们将它拆分为键和值
    for field in fields[3:]:
        key_value = field.strip().split('=')
        if len(key_value) == 2:
            result_dict[key_value[0]] = key_value[1]
    return result_dict
