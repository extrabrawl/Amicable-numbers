count = 0
for a in range(2,15000):
    summ = 0
    for i in range(1,a):
        if a%i == 0:
            summ = summ + i
    b = summ
    summ = 0
    for i in range(1,b):
        if b%i == 0:
            summ = summ + i
    if a == summ and a<b:
        print("Число",a,("и число"),b,"дружественные")
        count = count + 1
print("Найдено пар друж.чисел:",count)