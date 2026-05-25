# list=["ali","aziz","montasir","adam","khalid","mossa"]


# print("befor",list)

# list.insert(-1,"mother")

# print("after",list)

#fruits=["apple","orange","banane","coout","pineaple"]
# print(fruits[3])
# for x in fruits:
#     print(x)
#print(dir(fruits))
# #print(len(fruits))

# print("apple "in fruits)

# fruits[0]="pineapple"
# for fruit in fruits:
#     print(fruit)

# print(len(fruits))






# for i in range(1,11):
#     print(i)

# word="python"
# for letter in word:
#     print(letter)


# name="Hafadine Abdel aziz hissein"
# for letter in name:
#     print(letter)


# total=0
# for i in range(1,11):
#     total=total+i
# print  ("total=",total)  

# i=5
# while i<=10:
#     print("Ahmat")
#     i+=1
# print("welcome")



# i=0
# while i<=10:
#     print(i)
#     i+=2

# i = 0
# while i<=10 :
#     print(i)  
#     i+=3
    
# for x in range(1,11):
#     print(x)

# print("HAPPY NEW YEAR")

# #first
# for x in range(1,21):
#     if x==13:
#         break
#     else:
#         print(x)

# for number in range(0,10,2):
#     print("Attemp",number+1,(number+1)*".")

# successful=False 
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("successful")
#         break
# else:
#     print("attempted 3 time and failed")


# #NESTED LOOP
# for x in range(5):
#     for y in range(3):
#         print(f"({x},{y})")




# # iterable
# for x in "python":
#     print(x)

# i=0
# for i in range(0,10,2):
    
#     print(i)
# print("we have only even number")
# count=0
# for number in range(1,10):
#     if number %2==0:
#         count+=1
#         print(number)
    

# print(f"we have {count} even nuber")






#WHILE

# name=input("Enter your name :")
# while name =="":
#     print("you did not enter your name")
#     name =input("Enter your name :")
# print(f"Hello {name}")




#EXAMPLE    
# age=int(input("Enter your age :"))
# while age<0:
#     print("Age can not be Nagative")
#     age=int(input("Enter your age :"))
# print(f"you are {age} years old")    


# food=input("Enter a food you like (q,to quit) : ")
# while not food=="q":
#     print(f"you like {food}")
#     food=input("Enter another food you like (q,to quit) : ")
# print("bye")


#exirsie
# for i in range(1,6):
#     print(i)


#exirsi
# for name in range(5):
#     print("hafadine")


# x=1
# while x<=5:
#     print(x)
    


# password=""
# while password !="12345":
#     password=input("ENter your password :")

# print("welcome")




# num=int(input("Enter number :"))
# i=1
# while i<=num:
#     print(i)
#     i+=1


#password="12345"
# for i in range(3):
#     user_Name=input("Enter your password :")
#     if user_Name==password:
#         print("login is successful")
#     else:
#         print("wrong password") 
# else:
#     print("Accoun locked")           



# num=int(input("Enter your number :"))
# for i in range(1,11):
#     print(num,"x",i,"=",num*i)




# total=0
# while True :
#     num=int(input("Enter a number (0 to stop) : "))
#     if num==0:
#         break
    
#     total+=num
# print("Total",total)    




# balance=10000
# password="1234"

# for i in range(3):
#     user_password=input("Enter your password :")
#     if user_password==password:
#         print("login successful")
#         break
#     else:
#      print("wrong password")    
# else:
#    print("card blocked")




# while True:
#    print("---ATM Menu----")
#    print("1. check Balance")
#    print("2.withdraw")
#    print("3.Deposit")
#    print("4.Exit")
#    choice=input("choose your option:")  
#    if choice=="1":
#       print("your balance is:",balance)
#    elif choice == "2":
#       amount=float(input("Enter your amount to withdraw:"))
#       if amount<=balance:
#          balance-=amount
#          print("withdrawal successfull")
#       else:
#          print("Not enough balance") 
#    elif choice =="3":
#       amount=float(input("Enternamount to deposite :"))
#       balance += amount
#       print("Deposit succssful")
#    elif choice=="4":
#       print("thank you!")
#       break




# i=4
# # while i<=6:
#    print(i)
#    i+=1

# i=0
# while i<=10:
#    print(i)
#    i+=2

# num=int(input("Enter a number :"))
# for i in range(1,11):
#    print(num,"x",i,"=",num*i)


# name="Hafadine abdel aziz Hissein "
# for ch in name:
#    print(ch)



# for i in range(3):
#     print(i)


# i=0
# while i<=3:
#     print("hafadine")
#     i+=1


#for loop with list


# names={"aziz","MHT","ADAM","HISSEIN","KHALID","MOSSA","HAFADINE"}
# for  name in names:
#     print(name)       

# grades= [23,43,53,44,32,556,32,2,45,3,14,789,67,89,98,98,67,56,44,67,33,6,7,89]
# pass_student=0
# for gr in grades:
#     if gr>=50:
#         pass_student+=1
# print("number of student who passed ", pass_student)        
    


# list=["aziz","khalid","adam","youssf ","MHT","Hello"]
# print(list)
# print(list[0])
# print(list[-1])


# number=[10,20,30,40,60,70,80,90]
# number.append(50)
# number.remove(20)
# print(number)

# for num in number:
#     print(num)


# number=[1,2,3,4,5,6,

# couler=("red","blow","green","yalow","orenge")
# for clou in couler:
#     print(clou)


# number=(10,20)
# print("x = ", number[0])
# print("y = ",number[1])

# point=(2,5,67,46,75,43,68,98,787,57,88,75,89,886,85)
# print("Max =" , max(point))
# print("Min =", min(point))




students =["ali","aziz","hissen","hassan","khalid","moussa","adam"]
school_information=("ABC school",2026)
print("student list")
for student in students:
    print(student)


new_student=input("Enter new student name :")
students.append(new_student)

remove_student= input("Enter student name to remove:")
students.remove(remove_student)


print("update list : ")
for student in students:
    print(students)
