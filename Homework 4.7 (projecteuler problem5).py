# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
x=20
while x%20!=0 or x%19!=0 or x%18!=0 or x%17!=0 or x%16!=0 or x%15!=0 or x%14!=0 or x%13!=0 or x%12!=0 or x%11!=0:
    x+=1
print(x)
# 232792560