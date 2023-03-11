def numeric():
    while True:
        print('Enter your age:')
        age = input()
        if age.isdecimal():
            break
        print('Please enter a number for your age.')

    while True:
        print('Select a new password "letters and numbers only":')
        password = input()
        if password.isalnum():
            break
        print('please can only have letters and numbers.')

# def alpha():
#     print('Enter your age')
#     age = input('alphabets please')
#     print('select a new password "letters and numbers only ":')
#     password = input()
numeric()




