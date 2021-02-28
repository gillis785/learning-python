# picture

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for image in picture:
    for pixel in image:
        if (pixel):
            print('*', end ="") # * at the 1's
        else:
            print(' ', end ="") # spaces at the 0
    print('')