import sys
import re

pattern = re.compile('[0-9]')
split = '-'
with open(sys.argv[1], 'r+') as inf:
    with open(sys.argv[2], 'w+') as outf:
        for line in list(map(lambda x: ''.join(re.findall(pattern, x)), list(inf))):
            if outf.tell() != 0:
                outf.write('\n')
            outf.write(f'{line[:3]}-{line[3:6]}-{line[6:]}')
