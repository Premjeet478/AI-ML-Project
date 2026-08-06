    
#to find 2nd largest no
x = [2344566,678789,898776,44545,9887,566778,88765,987,9876754,345678,23344567890]
l = 0
sl = 0
print(max(x))
for i in x:
    if i>l:
        l = i
    elif i>sl and i!= l:  #ye wala logic 2nd largest ko dhundne ke liye hai
        sl = i
print(l,sl)

#exception example
def zero(x,y):
    try:
        z = x/y
        print(z)
    except:
        print("devide by 0 is wrong")

zero(10,0)