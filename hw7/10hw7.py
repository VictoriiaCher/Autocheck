def make_request(keys, values):
    if len(keys)==len(values):
        return {key:value for key, value in zip(keys, values)}
    else:
        return {}


keys = ['name', 'age', 'email']
values = ['Nick', '23']
print(make_request(keys, values))
