def triangle(height):
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        if i == 0:
            print(spaces + '_')
        elif i == height - 1:
            print('__' * i + '\\')
        else:

            print(spaces + '/' + ' ' * (2 * i - 1) + '\\')

height = int(input(" hauteur : "))

triangle(height)
