
# Meta caracteres: ^ $
# () grupo 
# [] conjunto 
# ()     \1 
# () ()  \1 \2
# (())()   \1 \2 \3

import re
from pprint import pprint

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
'''

tags = re.findall(r'<([dpiv]{1,3})>(.+?)<\/\1>', texto)
tags = re.findall(r'<(?P<tag>[dpiv]{1,3})>(.+?)<\/(?P=tag)>', texto)
# ?P<nomeGrupo> para dar nomes aos grupos

pprint(tags) #equivalente ou println

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 MAIS \3 COISAS \4', texto))
# .+? qualquer coisa não guloso

# # for tag in tags:
# #     um, dois, tres = tag
# #     print(tres)

# cpf = 'a 147.852.963-12 a'
# print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))
# ?: para eliminar o grupo do findall
# sem ele o print seria uma tupla com o grupo completo e com o grupo
