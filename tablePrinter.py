tableData = [
    ['apples', 'oranges', 'cherries', 'bannana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dog', 'cats', 'moose', 'goose']
]
# for i  in tableData:
#     export = str(i) 
#     # print(export)
#     for v in i:
#         export = str(v)
#         print(export)


def printTable(table):
    for i , k in table:
            string = ''


        # print(i)
        # print(table[-1])
        # if i == table[-1]:
        
            size = len(k)
            int = size
            

            # prevInt = 0
            print(size)

            if int > prevInt:
                prevInt += int
                print('higher')
                print(prevInt)
                # return prevInt
            elif int == prevInt:
                # print('equal')
                pass
            else:
                print('lower')
            print(k)
        


        # for k in i:
        #     k = str(k)
        #     string += k
        #     print(string)

printTable(tableData)