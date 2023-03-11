spam = ['apples', 'bananas', 'tofu', 'cats', 'dog', 'room', 'liver']



def string(list):

    string = ''
    for x in list:
        name2 = x
        
        if name2 == list[-1]:
            string += 'and '+ x
        
        else:
            string += x+', '
    print(string)
# def stringify(items):
#     for item in range(len(items)):
        
string(spam)
