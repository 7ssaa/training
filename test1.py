"""
20180703 Python training 1

"""

# print ("hello, world")

# msg = "hello, world"
# print (msg)

import time

def changecolor (color):
    """red, grey, yellow, green"""
    valid_colors = ("red", "grey", "yellow", "green")
    if color in valid_colors:
        if changecolor.times:
            print("The color was last changed at ", changecolor.times[-1])
        print (color)
        changecolor.times.append(time.asctime())
    else:
        n = valid_colors.__len__()
        not_last = valid_colors[:n-1]
        last = valid_colors[-1]

        message = ', '.join(not_last) + ' and ' + last
        print ("sorry, a color can only be", message)

changecolor.times = []