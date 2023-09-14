Name=input("enter your name:")
registerno=int(input("enter your register no:"))
course=input("course:")
mark1=int(input("enter mark1 :"))
mark2=int(input("enter mark2 :"))
mark3=int(input("enter mark3:"))
mark4=int(input("enter mark4:"))
mark5=int(input("enter mark5:"))
mark6=int(input("enter mark6:"))
sum=mark1+mark2+mark3+mark4+mark5+mark6;
average=sum/6;
max_value=100;
if(mark1 > mark2 and mark1 >mark3 and mark1>mark4 and mark1>mark5 and mark1>mark6):
 max_value=mark1
elif(mark2>mark3 and mark2>mark4 and mark2>mark5 and mark2>mark6):
 max_valuve=mark2
elif(mark3>mark4 and mark3>mark5 and mark3>mark6):
  max_value=mark3
elif(mark4>mark5 and mark4>mark6):
  max_value=mark4
elif(mark5>mark6):
  max_value=mark5
else:
  max_value=6
print("Max_mark is:",max_value)
min_value=40;

if(mark1 < mark2 and mark1 <mark3 and mark1<mark4 and mark1<mark5 and mark1<mark6):
 min_value=mark1
elif(mark2<mark3 and mark2<mark4 and mark2<mark5 and mark2<mark6):
 min_valuve=mark2
elif(mark3<mark4 and mark3<mark5 and mark3<mark6):
  min_value=mark3
elif(mark4<mark5 and mark4<mark6):
  min_value=mark4
elif(mark5<mark6):
  min_value=mark5
else:
  min_value=6
print("Min_marks :",min_value)
print(average)