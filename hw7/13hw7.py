def get_employees_by_profession(path, profession):
    with open(path, "r") as file:
        list_profession=[]
        lines = file.readlines()
        for line in lines:
            if line.find(profession)!=-1:
                list_profession.append(line)

        s = ''.join(list_profession).replace('\n','')
        result = s.replace(profession,'')
        return result.rstrip()

path = 'source_13hw7.txt'

print(get_employees_by_profession(path, 'courier'))
print(get_employees_by_profession(path, 'cook'))