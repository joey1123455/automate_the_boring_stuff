birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Grace': 'Mar 4'}

while True:
    print("Enter a name: 'blank to quit'")
    initialName = input()
    name = str(initialName.title())
    # print(name)
    if name == '':
        break
    if name in birthdays:
        print(f'{birthdays[name]} is the birthday of {name}')
    else:
        print(f'I do not have a record for {name}')
        print('What is your birthday?')
        bDay = input()
        bDay2 = str(bDay.title())
        # print(bDay2)
        birthdays[name] = bDay2
        print('Birthday database updated.')