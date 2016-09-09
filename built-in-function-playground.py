# globals()
animal = 'dog'
food = 'banana'
color = 'red'
material = 'wool'
print globals()

# bin()
print '13 in binary: ' + bin(13)
print '140827 in binary: ' + bin(140827)

# map()
def capitalize(word):
    return word.upper()
print map(capitalize, ['yes', 'no', 'for sure', 'go'])
