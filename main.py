a = str(input("Введите первую строку: ")) #Запрашиваем первую строку
b = str(input("Введите вторую строку: ")) #Запрашиваем вторую строку
rep1 = a.replace(" ","") #Заменяем пробелы (удаляем)
rep2 = b.replace(" ","") #Заменяем пробелы (удаляем)
len1 = len(rep1) #Ищем длинну
len2 = len(rep2) #Ищем длинну
count = 0 
for i in rep1.lower(): #Перебор i в rep1
    if i in rep2.lower(): #Перебо i в rep2
        count += 1
if count == len1 and len1 == len2: #Условие
    print("Является анаграммой ")
else:
    print("Неявляется анаграммой ")
