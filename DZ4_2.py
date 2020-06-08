p1 = input('Input e-mail: ')
p2 = input('Input e-mail confirmation: ')
#Якщо введений користувачем регістр не має значення
if p1.lower()== p2.lower():
#Якщо потрібне повне співпадіння - можемо написати if p1 == p2
    print('Ok')
else:
    print('Your e-mail confirmation is not correct!')
