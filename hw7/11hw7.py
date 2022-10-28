def sequence_buttons(string):
    combination =''
    keys=[1,2,3,4,5,6,7,8,9,0]
    values = [['.',',','?','!', ':'],['A', 'B', 'C'],['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R','S'],['T', 'U', 'V'], ['W', 'X', 'Y','Z'],[' ']]
    DICTIONARY = {key:value for key, value in zip(keys, values)}
    for ch in string.upper():
        for key, val in DICTIONARY.items():
            for i in val:
                if ch == i:
                    combination += (val.index(i)+1)*str(key)
    return combination

strings= ['Hello, World!', 'Hi there!']
for data in strings:
    print(sequence_buttons(data))