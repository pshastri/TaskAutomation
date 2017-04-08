'''
Created on Apr 7, 2017

@author: Praveen Shastri
'''


def hasSeenSum(myinput,testsum):
    myCompList=set()
    
    for i in myinput:
#         print "myinput: ", myinput
#         print "comList: ", myCompList
#         print "i: ", i
        mycomp=testsum-i
        if i in myCompList:
#             print "sum-i: ", mycomp
            print "Found the pair"
            print "pair: %d and %d" %(i,mycomp)
            return True
            
            break
        else: 
            myCompList.add(mycomp)
            mybool=False
    
    if not mybool:
        print "Did not find the sum or pair"   
    
    
if __name__=="__main__":
    myinput=[1,2,3,4]
    testsum=10
    hasSeenSum(myinput, testsum)