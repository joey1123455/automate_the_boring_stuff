#Divide or multiply
def calculate(numb):

    if numb % 2 == 0 :
        numb = numb / 2
        return numb
    elif numb % 2 == 1:
        numb = 3 * numb + 1
        return(numb)
    # else:
    #     getNumb()

#Pass input and perform action
def getNumb():
    number = int(input('Whats the number? '))
    answer = int(calculate(number))
    print(answer)

#Loop 10 times
for count in range(1, 11):
    #Input validation
    try: 
        getNumb()
    except ValueError:
        print('Invalid input. Type a number.')
        getNumb()


