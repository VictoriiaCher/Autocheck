def to_indexed(source_file, output_file):
    with open(source_file, "r") as s, open(output_file, "w") as out:
        count = 0
        for line in s.readlines():
            out.write(f'{count}: {line}')
            count +=1



source_file = 'source_14hw7.txt'
output_file = 'output_14hw7.txt'
print(to_indexed(source_file, output_file))