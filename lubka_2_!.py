'''
Обчислити значення виразу при заданому значенні  nєN.
2-4+8-16+32-64+128-...n - доданків
'''
# позначення
'''num_n - кількість доданків
n- номер доданку
S- cума 
c- степінь
a- доданок
b- знак доданку
'''
# введення
num_n = int(input('Введіть кількість доданків : '))
S = 0
a = 2
stс = 1
b = 1
n = 1
# обчислення
while n <= num_n :
    S = S+b*(a**stс)
    b = b*(-1)
    stс = stс+1
    n = n+1
# виведення
print('Сума = {0}'.format(S))
