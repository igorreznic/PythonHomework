#HomeWork 4.1 Make a script that would iterate through all the values of the dictionary and would print only the even numbers.
D = dict(key1=12, key2=2, key3=3, key4=4, key5=7, key6=11, key7=10)
for x in D:
    if D[x]%2==0:
     print(D[x])
# return: 12 2 4 10
