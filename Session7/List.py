# linstrore=(list(range(2,11)))
# print(linstrore)
# linstrore.append(40)
# print(linstrore)
#
# linstrore.pop(-1)
# print(linstrore)
#
# #table
# linstrore=(list(range(2,21,2)))
# print(linstrore)
#
# #pop Second smallest  Number
# listNumber=[23,54,64,23,76,45]
# listNumber.sort()
# print(listNumber)
# listNumber.pop(1)
# print(listNumber)


#how to add multiple list

# list1=list(range(1,5))
# list2=list(range(5,11))
# otherlist=[list1,list2]
# print(otherlist)
#
# #using forloop
# for i in range(2):
#     print(otherlist[i])
#     #print 9 online
# print(otherlist[1][4])



# listMaster=["apple=Rs-2000","Manana=Rs-60","Mango=Rs-150"]
# for item in listMaster:
#     if "a" in item:
#         print(item)
#
# #list Compri hension
# result=[item for item in listMaster if "a" in  item]
# print(result)

# input
# listFor=[]
# for i in range(1,10):
#     inpuetAnyNumChar=input("Enter the your choice:")
#     if inpuetAnyNumChar.lower()=='e':
#         break
#     listFor.append(inpuetAnyNumChar)
# print(listFor)

# listWhile=[]
# while True:
#     inputWhile=input("you are enter the any string:")
#     if inputWhile.upper()=='E' and inputWhile.lower()=='e':
#         break
#     listWhile.append(inputWhile)
# print(listWhile)

marks = int(input("Enter the marks: "))

if marks > 60 and marks <= 100:
    print("Your grade is A++")
elif marks >= 50 and marks <= 60:
    print("Your grade is B")
elif marks >= 30 and marks < 50:
    print("Your grade is C")
else:
    print("You have failed")





