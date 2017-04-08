'''
Created on Apr 7, 2017

@author: Praveen Shastri
'''


def hasSeenSum(myinput,testsum):
    myCompList=set()
    
    for i in myinput:
        print "myinput: ", myinput
        print "comList: ", myCompList
        print "i: ", i
        mycomp=testsum-i
        if i in myCompList:
            print "sum-i: ", mycomp
            print "Found"
        else: 
            myCompList.add(mycomp)
            print "Not found"
    
        
    
    
if __name__=="__main__":
    myinput=[1,2,3,4]
    testsum=7
    hasSeenSum(myinput, testsum)