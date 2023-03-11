import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
words = ['king', 'king', 'liver', 'pool', 'joey', 'joey', 'joey', 'joey', 'liver', 'liver']
integers = [1,3,5,8,6,7,7,9,9,99,55,70,56,1111,8787,1,2,4,5,890,4321,655, 1,2,33,4,5,6,7,8,9]



def counter(message):
    count = {}
    for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] + 1

    # pprint.pprint(count)
    print(pprint.pformat(count))

counter(words)
counter(message)
counter(integers)