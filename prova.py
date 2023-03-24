import re

def regex_date_and_time(string) -> str:
    print("date: ", re.findall(r'((?:0[0-9]|[1-2][0-9]|3[0-1])\/(?:0[1-9]|1[0-2])\/\d{4})', string, flags=re.M))
    print("time: ", re.findall(r'((?:[0-1][0-9]|2[0-4]):(?:0[0-9]|[1-5][0-9]))', string, flags=re.M))

def regex_ip(string) -> str:
    print(re.sub(r'''
        (?:
            25[0-5] |
            2[0-4][0-9] |
            1[0-9][0-9] |
            [1-9][0-9] |
            [0-9]
        )\.
        (?:
            25[0-5] |
            2[0-4][0-9] |
            1[0-9][0-9] |
            [1-9][0-9] |
            [0-9]
        )\.
        (?:
            25[0-5] |
            2[0-4][0-9] |
            1[0-9][0-9] |
            [1-9][0-9] |
            [0-9]
        )\.
        (?:
            25[0-5] |
            2[0-4][0-9] |
            1[0-9][0-9] |
            [1-9][0-9] |
            [0-9]
        )
    ''',  "ipv4", string, flags=re.X))

def regex_phone_number(string) -> str:
    print(re.findall(r'((?:\(?\d{2,3}\)?\s?)?(?:\d{4,6}(?:-?|\s)\d{4}))', string, flags=re.M))

def formatting_phone_number(string) -> str:
    #verificando se é válido
    if not re.search(r'((?:\(?\d{2,3}\)?\s?)?(?:\d{4,6}(?:-?|\s)\d{4}))', string, flags=re.M):
        return None
    else:
        #pegando o número com findall
        list_number = str(re.findall(r'((?:\(?\d{2,3}\)?\s?)?(?:\d{4,6}(?:-?|\s)\d{4}))', string, flags=re.M))
        ddd_number = ""
        ddd = re.findall(r'(?:\(\d{2,3}\)?)', list_number)
        for letter in ddd:
            ddd_number += letter
        final_cel = re.findall(r'(\b[9][0-9]{4}-?\s?[0-9]{4}\b)', list_number)
        cel_number = ""
        for letter in final_cel:
            cel_number += letter
        final_telephone = re.findall(r'(\b[0-9]{4}-?\s?[0-9]{4}\b)', list_number)
        telephone_number = ""
        for letter in final_telephone:
            telephone_number += letter


        if len(list_number) < 9:
            print(f'{ddd_number} - {telephone_number}')
        else:
            print(f'{ddd_number} - {cel_number}')

if __name__ == "__main__":

    # 2
    string_date_and_time = """
    O sistema vai parar
    para uma manutenção programada no dia 10/09/2020 às 23:00.
    """

    # regex_date_and_time(string_date_and_time)

    # 3
    string_ips = """
    Test changing 192.168.300.145 to new text, again 130.200.12.48, again 1.45.54.145.
    """

    #regex_ip(string_ips)

    # 4
    string_phones_number = """
    (19) 3123-4567 • 193123-4567 • (019)3123-4567 • (19)31234567
    • 1931234567 • (019) 91234 5678 • (019)91234 5678 • 019912345678 • 19 912345678 • 1991234 5678
    """

    # regex_phone_number(string_phones_number)

    # 5
    string_phone_number = "(199) 93123-4567"

    print(formatting_phone_number(string_phone_number))
