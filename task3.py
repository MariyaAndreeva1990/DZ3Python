eng = 'qwertyuiopasdfghjklzxcvbnm'
rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'

list_English = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
list_Russian = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ', 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФШЪ'}

word = input('Введите слово: ')

if word[0].lower() in eng:
    summ = 0
    for i in word:
        for j, value in list_English.items():
            if i.upper() in value:
                summ += j
    print(f'стоимость слова = {summ}')
else:
    if word[0].lower() in rus:
        summ = 0
        for i in word:
            for j, value in list_Russian.items():
                if i.upper() in value:
                    summ += j
    print(f'стоимость слова = {summ}')