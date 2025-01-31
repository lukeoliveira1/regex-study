import re
# 0.0.0.0 255.255.255.255
# 025.258.963-10 02525896310

#re.X para poder comentar dentro da expressão regular

# Teste essa expressão
# em https://regex101.com/r/lWVPOr/1
cpf = """
ALL VALID
125.852.369-20
123.465.798-10
112.131.415-16
ALL INVALID
1.1.1-2
10.20.30-40
100.100.100.10
100.100.100.100
100.100.100-100

"""
cpf_reg_exp = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', flags=0)
print(re.findall(r'(^(?:\d{3}\.){2}\d{3}-\d{2}$)', cpf, flags=re.M))
# print(cpf_reg_exp.search(cpf))


# Teste essa expressão
# em https://regex101.com/r/XDyL7q/1

ip_reg_exp = re.compile(r'''
    ^
    (?:
        (?:
        25[0-5] | # 250-255
        2[0-4][0-9] | # 200-249
        1[0-9]{2} | # 100-199
        [1-9][0-9] | #10-99
        [0-9] # 0-9
        )
        \.?
    ){4}
    \b
    $
''', flags=re.X)

ip_reg_exp_test = re.compile(r'''
    ^
    (?:
        (?:
        25[0-5] | # 250-255
        2[0-4][0-9] | # 200-249
        1[0-9]{2} | # 100-199
        [1-9][0-9] | #10-99
        [0-9] # 0-9
        )
        \.
    ){3}
     (?:
    25[0-5] | # 250-255
    2[0-4][0-9] | # 200-249
    1[0-9]{2} | # 100-199
    [1-9][0-9] | #10-99
    [0-9] # 0-9
    )
    $
''', flags=re.X)


for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'

    print(ip, ip_reg_exp.findall(ip))
