grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', '0', '0', '.', '.', '.'],
    ['.', '0', '0', '0', '0', '.'],
    ['0', '0', '0', '0', '0', '.'],
    ['0', '0', 'a', 's', 't', '$'],
    ['.', '/', '}', 's', 't', '$'],
    ['0', '/', ']', 's', 't', '$'],
    ['0', '0', '0', 's', 't', '$'],
    ['.', '/', 'a', '1', '0', '7']
]

# print(grid)

def printer(img):
    for i in img:
        # for pix in img:
        # print(i)
        string = ''
        for x in i:

            string += str(x)
        # for pix in img[i]:
        #     # print(img[i][-1])
        #     # if string == img[i][-1]:
        #     #     string += pix
        #     # else:
        #     #     string += pix + ', '
        #     print(img)
        print(string)


printer(grid)