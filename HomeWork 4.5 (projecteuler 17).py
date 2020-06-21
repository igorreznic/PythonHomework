#HomeWork 4.5
# one=3, two=3, three=5, four=4, five=4, six=3, seven=5, eight=5, nine=4
# eleven=6, twelve=6, thirteen=8, fourteen=8, fifteen=7, sixteen=7, seventeen=9, eighteen=8, nineteen=8
# ten=3, twenty=6, thirty=6, forty=5, fifty=5, sixty=5, seventy=7, eighty=6, ninety=6
# (hundred and=10) 100=13, 200=13, 300=15, 400=14, 500=14, 600=13, 700=15, 800=15, 900=14
# one thousand =11
n=0 #    n = sum of letters
for i in range(1,20):
	if i==1:
		n+=3
	if i==2:
		n+=3
	if i==3:
		n+=5
	if i==4:
		n+=4
	if i==5:
		n+=4
	if i==6:
		n+=3
	if i==7:
		n+=5
	if i==8:
		n+=5
	if i==9:
		n+=4
	if i==10:
		n+=3
	if i==11:
		n+=6
	if i==12:
		n+=6
	if i==13:
		n+=8
	if i==14:
		n+=8
	if i==15:
		n+=7
	if i==16:
		n+=7
	if i==17:
		n+=9
	if i==18:
		n+=8
	if i==19:
		n+=8
for i in range(20,1000):
	if str(i)[-1]=='1':
		n+=3
	if str(i)[-1]=='2':
		n+=3
	if str(i)[-1]=='3':
		n+=5
	if str(i)[-1]=='4':
		n+=4
	if str(i)[-1]=='5':
		n+=4
	if str(i)[-1]=='6':
		n+=3
	if str(i)[-1]=='7':
		n+=5
	if str(i)[-1]=='8':
		n+=5
	if str(i)[-1]=='9':
		n+=4
	if str(i)[-2]=='2':
		n+=6
	if str(i)[-2]=='3':
		n+=6
	if str(i)[-2]=='4':
		n+=5
	if str(i)[-2]=='5':
		n+=5
	if str(i)[-2]=='6':
		n+=5
	if str(i)[-2]=='7':
		n+=7
	if str(i)[-2]=='8':
		n+=6
	if str(i)[-2]=='9':
		n+=6
for i in range(100,1001):
	if str(i)[-3]=='1':
		n+=13
	if str(i)[-3]=='2':
		n+=13
	if str(i)[-3]=='3':
		n+=15
	if str(i)[-3]=='4':
		n+=14
	if str(i)[-3]=='5':
		n+=14
	if str(i)[-3]=='6':
		n+=13
	if str(i)[-3]=='7':
		n+=15
	if str(i)[-3]=='8':
		n+=15
	if str(i)[-3]=='9':
		n+=14
	if i%100==0 and i<1000:
		n-=3
	if i==1000:
		n+=11
print(n) 