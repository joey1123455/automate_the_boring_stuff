def eggs(someParam):
    someParam.append('hello')

spam = [1, 2, 4]
cam = (1,5,9)
camLited = list(cam)

eggs(camLited)
print(camLited)