# Four-operations
the original program of Four operations

from fractions import Fraction
from random import randint
amount=30
acc_amount=0
while acc_amount!=amount:
    all_random=randint(1,2)
    if  (all_random==1):
        first_num=randint(0,10)
        second_num=randint(0,10)
        opreation_num=randint(1,4)#计算结果
        if(opreation_num==4): #/
            if(second_num==0):
                while second_num==0:
                    second_num=randint(0,10)
            result=first_num/second_num
        if(opreation_num==1):#+
            result=first_num+second_num
        if(opreation_num==2): #-
            result=first_num-second_num
        if(opreation_num==3): #*
            result=first_num*second_num
        if(result<=100 and result>=0): #判断结果 判断被除数是否为零
                                   #判断结果是否在允许范围内
            print first_num,
            if(opreation_num==4): #/
                print"/",
            if(opreation_num==1):#+
                print"+",
            if(opreation_num==2): #-
                print"-",
            if(opreation_num==3): #*
                print"*",
            print second_num
            acc_amount=acc_amount+1
            
    if  (all_random==2):
        first_num1=randint(0,10)
        first_num2=randint(1,10)
        second_num1=randint(0,10)
        second_num2=randint(1,10)
    
        while first_num1>=first_num2:
            first_num1=randint(0,10)
            first_num2=randint(1,10)
        while second_num1>=second_num2:
            second_num1=randint(0,10)
            second_num2=randint(1,10)
        

        first_num=Fraction(first_num1, first_num2)
        second_num=Fraction(second_num1,second_num2)

        opreation_num=randint(1,4)#计算结果
        if(opreation_num==4): #/
            if(second_num==0):
                while second_num2==0 or second_num1==0:
                    second_num1=randint(0,10)
                    second_num2=randint(1,10)
                    second_num=Fraction(second_num1,second_num2)
            result=first_num/second_num
        if(opreation_num==1):#+
            result=first_num+second_num
        if(opreation_num==2): #-
            result=first_num-second_num
        if(opreation_num==3): #*
            result=first_num*second_num
        if(result<=100 and result>=0):
            #if()
            print "(",
            print first_num,
            print")",
            if(opreation_num==4): #/
                print"/",
            if(opreation_num==1):#+
                print"+",
            if(opreation_num==2): #-
                print"-",
            if(opreation_num==3): #*
                print"*",
            print "(",
            print second_num,
            print")"
            acc_amount=acc_amount+1
