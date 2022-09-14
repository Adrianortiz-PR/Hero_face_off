import random
while True:
 
 Fighter1=input("Pick fighter one: ")
 Fighter2=input("Pick figther two: ")
 
 F1moves=["Energy","Strength","Speed"]
 F2moves=["Energy","Strength","Speed"]
 F1=random.choice(F1moves)
 F2=random.choice(F2moves)

 if F1==F2:
    print(Fighter1, "and", Fighter2, "fought to a draw!")
 elif F1=="Energy" and F2 == "Strength":
    print(Fighter1, "beat", Fighter2)
 elif F1=="Strength" and F2 == "Speed":
    print(Fighter1, "beat", Fighter2)
 elif F1=="Speed" and F2 == "Energy":
    print(Fighter1, "beat", Fighter2)
 elif F1=="Energy" and F2 == "Speed":
    print(Fighter2, "beat", Fighter1)
 elif F1=="Speed" and F2 == "Strength":
    print(Fighter2, "beat", Fighter1)
 elif F1=="Strength" and F2 =="Energy":
    print(Fighter2, "beat", Fighter1)



