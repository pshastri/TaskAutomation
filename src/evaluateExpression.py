'''
Created on Mar 21, 2017

@author: pshastri
'''
def parseExpression(inputExpression):
    answer=0
    allDigitExpression=[""]
    newExpressionList=[]
#     allSymbolExpression=[]
    for eachChar in inputExpression:
        if eachChar.isdigit():
            if allDigitExpression[-1].isdigit():
                allDigitExpression[-1]+=eachChar
            else:
                allDigitExpression.append(eachChar)
        else:
            allDigitExpression.append(eachChar)
    allDigitExpression.remove('')
    print allDigitExpression
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
    parseExpression("989+9")