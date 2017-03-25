'''
Created on Mar 21, 2017

@author: pshastri
'''
def parseExpression(inputExpression):
    allDigitExpression=['']
    allSymbolExpression=['']
    for eachChar in inputExpression:
        if eachChar.isdigit():
            if allDigitExpression[-1].isdigit():
                allDigitExpression[-1]+=eachChar
            else:
                allDigitExpression.append(eachChar)
        else:
            allSymbolExpression.append(eachChar)
    print allDigitExpression
    print allSymbolExpression
            
inputExpression=raw_input()
parseExpression(inputExpression)