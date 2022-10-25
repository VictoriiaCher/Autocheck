def save_applicant_data(source, output):
    with open(output, "w") as out:
        for i in source:
            line = list(i.values())
            string = ",".join(map(str,line))
            out.write(string+ '\n')  


data_list= [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

save_applicant_data(data_list, '8hw6_output.txt')

