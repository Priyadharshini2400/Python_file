


print('******lets begin the game********')
def game():
    count_n=0
    count_c=0
    for i in range(1,4):
        print('Enter number 1: stone')
        print('Enter number 2: paper')
        print('Enter number 3: Scisssor')
        print()
        try:
            import random
            n=int(input('Enter a number: '))
            if type(n)!=int:
                raise ValueError ('enter a number')
            elif n>3:
                raise TypeError ('Enter number 1,2,3')
            elif n=='  ':
                raise TypeError
            print()
            c=random.randint(1,3)
            print('computer turn:',c)
            print()
            1=='stone'
            2=='paper'
            3=='scissor'

            choice=['Rock','paper','scissor']
            if i in (1,2,3):
               print(f'your choice is : {choice[n - 1]}')
               print(f'computer choice is : {choice[c - 1]}')

            if (n==1 and c==1) or (n==2 and c==2) or (n==3 and c==3):
                print('Tie')
            elif (n==1 and c==2) or (n==2 and c==3) or (n==3 and c==1):
                count_c+=1
                print('computer won')
            elif (n==2 and c==1) or (n==1 and c==3) or (n==3 and c==2):
                count_n+=1
                print('player won')
                print()

                
        except ValueError:
            print('Enter value must be integer')
        except TypeError:
            print('enter value must be 1,2,3')
            
    print(f'score:{count_n}/{count_c}')
    try:
        m=input('you want to continue the game (Y/N) :')
        f=('y','n','Y','N')
        if m not in f:
            raise NameError
    except NameError:
        print('Enter y or n')
    if m in ('y','Y'):
        game()
    elif m in ('n','N'):
        return



game()
print('*********Game Ends********')




        


        



        
                








    
            





            
            










            
            
