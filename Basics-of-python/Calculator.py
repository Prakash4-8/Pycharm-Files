"""
This project is based on mimicing a calculator using Python but with some special add-ons.
It calculates area of different objects.
It also checks speciality of a number.
"""

import time as t
import Pal as P
import Spec as S
import Perf as Pe
import Prime as Pr
import Arith as A
import Area as Ar


while True:
    print('\n',' ' * 75,'CALCULATOR\n',' ' * 75,'++++++++++')
    ch = int(input('\n  1.Calculate arithmetic value\n  2.Calculate area\n'
                   '  3.Check details of a number\n  4.Exit\nEnter your choice: '))
    if ch == 1:
        while True:
            op = input('Choose an operator ( + , - , * , / ) : ')
            if op == '+' or op == '-' or op == '*' or op == '/':
                a = int(input('Enter first number : '))
                b = int(input('Enter second number : '))
                if op == '+':
                    A.add(a, b)
                elif op == '-':
                    A.sub(a, b)
                elif op == '*':
                    A.mult(a, b)
                elif op == '/':
                    A.div(a, b)
                c = input('Want to continue? ( y/n ) : ')
                if c == 'y' or c == 'Y':
                    continue
                else:
                    break
            else:
                print('Wrong choice!!! Enter again...')

    elif ch == 2:
        while True:
            x = int(input('\nArea calculator\n  1.Triangle\n  2.Square\n  3.Rectangle\nEnter your choice: '))
            if x ==1 or x == 2 or x == 3:
                Ar.calc_area(x)
                t.sleep(3)
                break
            else:
                print('Wrong choice!!! Enter again')



    elif ch == 3:
        n = int(input("Enter a number (integer) : "))
        if n == 0:
            print('Fact 1. If you multiply it with any number it will remain the same'
                  '\nFact 2. You can\'t divide any number by it.')
        else:
            if (n // 2) != 0:
                print('%d is an odd number.' % n)
            else:
                print('%d is an even number.' % n)
            Pr.check_prime(n)
            P.check_pal(n)
            S.check_spec(n)
            Pe.check_perf(n)
            t.sleep(10)
    elif ch == 4:
        print(' ' * 75,'  Exiting...')
        t.sleep(1)
        exit()
    else:
        print('Wrong choice!!! Enter again!')
