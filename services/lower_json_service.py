#conver to json letters in lowercases 

# data ={'codigo_maestro': 'PCIslCEN'}

def data_lower(json_data):
    json_lower = dict((k.lower(), v.lower()) for k, v in json_data.items())
    return json_lower



# print(data_lower(data))

