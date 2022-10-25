import re
def sanitize_file(source, output):
        with open(source, "r") as s, open(output, "w") as out:
            data = re.sub(r'\d+','',s.read())
            out.write(data)


sanitize_file('7hw6_source.txt', '7hw6_output.txt')