import re
from pathlib import Path

file = open(Path.cwd()/Path('madlibs'))
text = file.read()
file.close()
regex = re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)')
for i in regex.findall(text):
    for txt in i:
        if txt != '':
            reg = re.compile(r'{}'.format(txt))
            addtext = input('Enter the substitute for %s: ' %txt)
            text = reg.sub(addtext, text, 1)
print(text)
file = open(Path.cwd()/Path('addmadlibs'), 'w')
file.write(text)
file.close()
