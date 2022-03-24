#was to enter 5 string in list & check print string has even number
x=[]
count=0
def createlist(x):
    x=[]

    for i in range(5):
        b=input("Enter any string:")
        x.append(b)
createlist(x)
for i in x:
    count=0
    for j in i:
        count=count+1
    if(count%2==0):
        print('The list is {} and its length is {}'.format(i,count))




     
