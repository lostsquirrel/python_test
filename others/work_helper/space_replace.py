import re

fh = open("structure")

p = re.compile("`.*`")
content = ''
for line in fh.readlines():
    if '`' in line:
        second = line.rindex('`')
        first = line.index('`')
        content += line[:first] + '-' * (second - first) + line[second + 1:]
    else:
        content += line
print(content)
