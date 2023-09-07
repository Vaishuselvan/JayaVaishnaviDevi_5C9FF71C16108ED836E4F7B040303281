year=int(input("enter the year:"))
if(year%400==0 and year%100==0):
  print("Yes leap year")
elif(year%4==0 and year % 100!=0):
  print("Yes leap year")
else:
  print("Not leap year")