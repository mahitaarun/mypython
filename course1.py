#PleaseContinue=True
#while(PleaseContinue):
#print("input True to  continue")
#PleaseContinue=input()
#print ("i am done with the loop")
str = "appa is a bad boy"
print str
#[] and [:] is a slice operator
print(str[0])
print(str[2:6])
print(str[2:])
print(str * 2 )
print(str + "test")

strlist=str.split()
print strlist

result = []
for character in str:
    result.append(character)
print result

result = [character for character in str]
print result
