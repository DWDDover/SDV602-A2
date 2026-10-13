count = 50

def fizzbuzz(count):
    for i in range(count):
        if(i == 0):
            continue
        elif(i % 15) == 0:
            print('FizzBuzz')
        elif(i % 3) == 0:
            print('Fizz')
        elif(i % 5) == 0:
            print('Buzz')
        else:
            print(i)
            
if '_main_':
    print('How many Numbers?')
    user_input = int(input())
    fizzbuzz(user_input)
