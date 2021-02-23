
a={'january':31,'february':28, 'march':31, 'april':30, 'may':31, 'june':30, 'july':31, 'august':31, 'september':30, 'october':31, 'november':30, 'december':31}

#print (a.keys()    
klist=list(a.keys())
vlist=list(a.values())
#print(a.items())
print("keys",klist)
print("Months With 30 days")
for key,value in a.items():
    if 30==value:
        print (key)
