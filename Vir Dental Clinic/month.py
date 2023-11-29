import calendar as cal
year = 2019
month = [1,2,3,4,5,6,7,8,9,10,11,12]
list1=[]
for i in month:
    list1.insert(i,cal.month(year,i))
print(list1[2])
