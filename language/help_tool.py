import re
import json

print('o_name : ', end = '')
o_name = input()
o_json = json.loads(open(o_name + '.json', encoding='utf-8').read())

print('n_name : ', end = '')
n_name = input()
n_json = json.loads(open(n_name + '.json', encoding='utf-8').read())

for i in n_json:
    if not i in o_json:
        del n_json[i]

for i in o_json:
    if not re.search('^_', i[0]):
        if not i in n_json:
            print('o_title : ' + i)
            print('o_text : ' + o_json[i])

            print('n_text : ', end = '')
            n_text = input()

            n_json = {**n_json, **{i : n_text}}

n_data = json.dumps(n_json, indent = 4, ensure_ascii = False)

f = open(n_name + '.json', "w", encoding='utf-8')
f.write(n_data)
f.close()