from random import randint

min_number = int(input("Please eneter min value: "));
max_number = int(input("Pleaase enetr teh amx numebr: "))

if(max_number<min_number):
    print('Invalid, shutting down')
else:
    rnd_number = randint(min_number,max_number)
    print(rnd_number)