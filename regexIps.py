import re

ips = """
5.155.12.122
212.1564.12.12
131.135.10.1
488.454.1.2
100.12.15.14.
14.15.165.17
200.215.14.152
"""

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

    print(ip, re.findall(ip_reg_exp_test,ip))