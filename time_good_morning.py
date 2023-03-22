import time
t = time.localtime().tm_hour 

if( t < 12):
    print("Good Morning!")
elif(t >=12 and t<16):
    print("Good Afternoon!")
elif(t>=16 and t<=24):
     print("Good Evening!")

