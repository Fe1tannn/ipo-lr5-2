a = str(input("Введите первую строку: "))
b = str(input("Введите вторую строку: "))
rep1 = a.replace(" ","")
rep2 = b.replace(" ","")
len1 = len(rep1)
len2 = len(rep2)
count = 0
for i in rep1.lower():
    if i in rep2.lower():
        count += 1
if count == len1 and len1 == len2:
    print("Является анаграммой ")
else:
    print("Неявляется анаграммой ")
