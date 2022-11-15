print(len('abc'))                   #довжина: кількість елементів
print('abc' + 'def')                #конкатенація
print('Ni!' * 4)                    #повторення

print('---------------')            #15 символів - , важкий спосіб
print('-' * 15)                     #15 символів - , легкий спосіб

myjob = "hacker"
for c in myjob: print(c, end=' ')   #прохід по елементам з виводом кожного

print("k" in myjob)                 #знайдено
print("z" in myjob)                 #не знайдено
print('spam' in 'abcspamdef')       #пошук підстроки без повернення позиції