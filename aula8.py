# re.A -> ASCII
# re.I -> IGNORECASE
# re.M -> Multiline -> ^ $ linha por linha
# re.S -> Dotall \n reconhece as quebras de linha
import re

texto = '''
131.768.460-53
055.123.060-50 ABC
955.123.060-90
'''

# print(re.findall(r'(^(?:\d{3}\.){2}\d{3}\-\d{2}$)', texto, flags=re.M))

texto2 = '''O João gosta de folia 
E adora ser amado'''
print(re.findall(r'^o.*o$', texto2, flags=re.I | re.S))