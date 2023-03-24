import re

string = 'Esse é um teste de strings teste'

#count só troca a primeira que achar
print(re.sub(r'teste', 'ABCD', string, count=1))

regexp = re.compile(r'teste')

print(regexp.search(string))
print(regexp.findall(string))

