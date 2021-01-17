import random as rnd
#x-случайное число
lb=1
rb=100
x=rnd.randint(1, 100)
n=5
print ("Ваша задача отгадать число от %s до %s. У вас %s попыток" %(lb, rb, n))

for g in range(n):
    y=int(input("назовите число: "))
    if x==y:
        print ("вы выйграли")
        break
    elif x>y:
        print ("введите число больше")
    elif x<y:
        print ("введите число меньше")
else: print ("вы проиграли.", "правильный ответ: %s" %(x))
