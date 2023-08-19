ch = 'y'

while ch.lower() != 'n' and ch.lower() == 'y':
                                    
                    
                    
                    a = int(input('enter the first number : '))
                    b = int(input('enter the second number  : '))
                    op = input('enter the operation[+,-,*,/]')

                    if op == '+':
                                        r = a +b 
                                        print(r)
                    elif op == '-':
                                        if a>b or a==b :
                                                            r = a-b
                                                            print(r)
                                        else :
                                                            r = b-a
                                                            print(r)

                    elif op=='*':
                                        r = a*b 
                                        print(r)
                                        
                    elif op=='/':
                                        if b!=0:
                                                            r = a/b 
                                                            print(r)
                                        else :
                                                            print("denominator cannot be 0 for division")

                    else :
                                        print('enter a valid operation !!')  
                    k = input('do you wish to continue[y/n] : ')  
                    if k.lower()!='n'and k.lower()!='y' :
                                        while k.lower()!='n' and k.lower()!='y':
                                                            print('please enter a valid choice')
                                                            k = input('do you wish to continue[y/n] : ')
                                                            if k.lower() =='n' or k.lower() == 'y':
                                                                                ch = k    
                    
                    
                    else :
                                        ch = k           