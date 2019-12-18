
for a in ['1','1.1','a']:
    print(a)
    print(a.isalnum(), a.isalpha(), a.isascii)
    print(a.isdecimal(),a.isdigit,a.isnumeric())
    if a.isnumeric():
        print('정수변환',int(a))
    print('-'*20)
