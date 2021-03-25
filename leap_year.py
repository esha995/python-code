year=int(input('enter year'))
if year%4==0:
    print(year,"leap year")
elif year%100==0:
    print(year,"not leap year")
elif year%400==0:
    print(year,"leap year")
else:
    print("leap year")
