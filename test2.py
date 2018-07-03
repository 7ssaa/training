import time
class ChangeColor(object):
    def __init__(self, valid_colors):
        self.valid_colors = valid_colors
        self.times = []

    def __call__(self, color):
        if color in self.valid_colors:
            if self.times:
                print("The color was last changed at ", self.times[-1])
            print(color)
            self.times.append(time.asctime())
        else:
            n = self.valid_colors.__len__()
            not_last = self.valid_colors[:n - 1]
            last = self.valid_colors[-1]

            message = ', '.join(not_last) + ' and ' + last
            print("sorry, a color can only be", message)

changeRGBColors = ChangeColor(['red', 'green', 'blue'])
changeRGBColors('red')

changeFancyColors = ChangeColor(['pink', 'purple'])
changeFancyColors('red')