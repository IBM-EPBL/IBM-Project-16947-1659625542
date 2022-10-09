import random

for i in range(7):
    a=random.randint(20,200)  

    b=random.randint(20,100)  
    print('Day', i) 
    print('Temperature:', a )
    print('Humidity   :', b )
    if a>80:
      if b>80:
        print("HAZARD PREDICTED... ")
      else:
        print("HIGH TEMPERATURE ")
    elif a==80:
        print("TEMPERATURE HIGH ")
    else:
        print("ALL GOOD ")
    print()
