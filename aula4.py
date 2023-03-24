# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou 1
# .* qualquer coisa obs.: menos quebra de linha
import re

texto = '''
<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div> 
'''
texto1 = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div> 
'''

print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdvi]{1,3}>', texto)) 
print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdvi]{1,3}>', texto1)) #grid(guloso) continua checando até o fim da string
print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdvi]{1,3}>', texto1)) #lazy(guloso) NÃO continua checando até o fim da string
 