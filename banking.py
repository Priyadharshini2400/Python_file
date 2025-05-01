print('=====================================')
print()
print('------Welcome to smart bank----------')
print()
print('=====================================')
print()


while True:
    print('*********************************')
    print()
    print('=<< 1.Open a new account      >>=')
    print('=<< 2.Withdraw Money          >>=')
    print('=<< 3.Deposite Money          >>=')
    print('=<< 4.Check Customer & Balance>>=')
    print('=<< 5.Exit/Quit               >>=')
    print()
    print('*********************************')

    n=int(input('select your choice from the above menu :'))
    
    if n==1:
        name=input('Enter your name:')
        addhar=int(input('Enter your 12 digit Addhar number :'))
        if len(str(addhar))==12:
            mobile=int(input('Enter your  mobile number:'))
            if len(str(mobile))==10:
                pan =input('Enter your pan card number :')
                if len(str(pan))==14:
                    pin=int(input('please input a pin of your choice and the pin must be 4 digit : '))
                    if len(str(pin))==4:
                        value=int(input('please input a value to deposite to start an account and the minimum deposite should be amount 500:'))
                        if value>=500:
                            deposite=value
                            print('account created successfully')

                        else:
                            print('deposite the minimum balance 500')


                    else:
                        print('pin must be 4 digit')

                else:
                    print('enter correct pan card')



            else:
                print('enter digits must be 10')



        else:
            print('enter the correct addhar digits')
        
    elif n==2:
        names=input('enter your name :')
        pin1=int(input('enter your pin :'))
        if names == name and pin1==pin:
            withdraw=int(input('enter a amount to withdraw :'))
            if withdraw>deposite:
                print('Your balance is low can not able to withdraw')
            else:
                deposite-=withdraw
                print('withdraw successfully')
                print('your balance is',deposite)
        else:
            print('invalid')




    elif n==3:
        names=input('enter your name :')
        pin1=int(input('enter your pin :'))
        if names == name and pin1==pin:
            dep_money=int(input('Enter the deposite money:'))
            deposite+=dep_money
            print('deposite successfully')
            print('your balance is :',deposite)

        else:
            print('invalid')

    elif n==4:
        print('your name is :',name)
        print('your addhar number is:',addhar)
        print('your mobile number is :',mobile)
        print('your pan card number is :',pan)
        print('your balance amount is :',deposite)

    elif n==5:
        print('***********exit****************')
        break
    








            


            
                     
        
        

    
