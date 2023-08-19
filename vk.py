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
                                        r = a/b 
                                        print(r)

                    else :
                                        print('enter a valid operation !!')  
                    ch = input('do you wish to continue[y/n] : ')  
                    if ch!='n'or ch!='y' :
                                        print('please neter a valid choice')               