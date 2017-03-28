'''
Created on Mar 21, 2017

@author: pshastri
'''
def parseExpression(inputExpression):
#     answer=0
    allDigitExpression=[""]
#     newExpressionList=[]
#     allSymbolExpression=[""]
    for eachChar in inputExpression:
        if eachChar.isdigit():
            if allDigitExpression[-1].isdigit():
                allDigitExpression[-1]+=eachChar
            else:
                allDigitExpression.append(eachChar)
        else:
            allDigitExpression.append(eachChar)
#     print allDigitExpression
#     print ("allDigitExpression.remove(''): ", allDigitExpression.remove(''))
#     print ("allDigitExpression: ", allDigitExpression)
    mathCalculation(allDigitExpression)
    
def mathCalculation(allDigitalExpression):
    mathList=allDigitalExpression
    answer=0
#     print len(mathList)
    mathList.remove("")
#     print mathList
#     print len(mathList)
    for i,j in zip(range(len(mathList)-1),range(len(mathList)-1)):
#         print "I m here"
#         print mathList[i+1]
        if mathList[i+1] == '+':
#             print "i m here"
            answer=answer+int(allDigitalExpression[j])+int(allDigitalExpression[j+2])
        elif i+1 == '-':
            answer=allDigitalExpression[j]-allDigitalExpression[j+2]
    print "Evaluted expression value is: ", answer
    
      
    #print allDigitExpression # got the numbers and symbol in a list
    
#     print type(allDigitExpression[0])
#     for i in range (len(allDigitExpression)):
#         if allDigitExpression[i].isdigit():
#             allDigitExpression[i]=int(allDigitExpression[i])
#         else:
#             allDigitExpression[i]=allDigitExpression[i]
#     print allSymbolExpression
#     print inputExpression.index("+" or "-")
#     for iterI in range (len(allDigitExpression)-1):
#         if 
    

if __name__=="__main__" :
    validInput=False
    while not validInput:
        try:
            print ("Enter the mathematical expression: ")
            inputExpression=raw_input()
            validInput=True
        except:
            print("Something went wrong, enter mathematical expression")
            
    parseExpression(inputExpression)