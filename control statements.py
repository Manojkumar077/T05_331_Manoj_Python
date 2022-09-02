'''

Control Statements :
                    Control statements are used to control the flow of the execution of the loop based on a condition.

 They modify the normal flow/behaviour of the looping statements.

 Three types of control statements are used in python :
  1. Break
  2. Continue
  3. Pass

Break: Break statement the breaks the loop and takes the interpreter out of the loop as soon as the condition is true.
ex:
for i in range(10):
    if i == 5:
        break
    else:
        print(i)


Continue: Continue statements just skips that particular value and executes the other values until the condition is true.
ex:
for i in range(10):
    if i == 5:
        continue
    else:
        print(i)

Pass: Pass statements help to skip the whole condition. It is commonly used when business logic is unclear and to be
        implied later by the developer
ex:
for i in range(10):
    if i < 2:
        i=0
    else:
       pass
    print(i)


'''
