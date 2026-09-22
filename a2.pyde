from processing import *
import random

grid_size = [10,10]
screen_size = [500,500]
grid = []
colour = [[255,100,100],[100,255,100],[100,100,255]]
selection = [False, 0, 0]

#---------------------------------setup---------------------------------------

def setup():
    size(screen_size[0],screen_size[1])
    strokeWeight(3)
    x = 0
    while x < grid_size[1]:
        row = []
        y = 0
        while y < grid_size[0]:
            row.append(0)
            y = y + 1
        grid.append(row)
        x = x + 1

#---------------------------------main----------------------------------------

def fillin():
    a = 0
    while a < grid_size[1]:
        b = 0
        while b < grid_size[0]:
            if grid[a][b] == 0:
                grid[a][b] = random.randint(1,3)
            b = b + 1
        a = a + 1


def visual():
    cell_width = screen_size[0] / grid_size[0]
    cell_height = screen_size[1] / grid_size[1]

    i = 0
    while i <= grid_size[0]:
        x = i * cell_width
        line(x, 0, x, screen_size[1])
        i = i + 1

    i = 0
    while i <= grid_size[1]:
        y = i * cell_height
        line(0, y, screen_size[0], y)
        i = i + 1

    y = 0
    while y < grid_size[1]:
        x = 0
        while x < grid_size[0]:
            cellx = (x * cell_width) + (cell_width / 2)
            celly = (y * cell_height) + (cell_height / 2)
            colour_index = grid[y][x]
            fill_colour = colour[colour_index - 1]
            fill(fill_colour[0], fill_colour[1], fill_colour[2])
            ellipse(cellx, celly, cell_width * 0.6, cell_height * 0.6)
            x = x + 1
        y = y + 1


def three_del():
    y = 0
    while y < grid_size[1]:
        x = 0
        while x < grid_size[0]:
            colour_index = grid[y][x]

            if colour_index != 0:
                if x + 2 < grid_size[0]:
                    if colour_index == grid[y][x+1] and colour_index == grid[y][x+2]:
                        grid[y][x] = 0
                        grid[y][x+1] = 0
                        grid[y][x+2] = 0

                if y + 2 < grid_size[1]:
                    if colour_index == grid[y+1][x] and colour_index == grid[y+2][x]:
                        grid[y][x] = 0
                        grid[y+1][x] = 0
                        grid[y+2][x] = 0
            x = x + 1
        y = y + 1


#def fall():


def mousePressed():
    cell_width = screen_size[0] / grid_size[0]
    cell_height = screen_size[1] / grid_size[1]
    click_x = int(mouseX / cell_width)
    click_y = int(mouseY / cell_height)

    if selection[0] == False:
        selection[0] = True
        selection[1] = click_x
        selection[2] = click_y
        return

    x0 = selection[1]
    y0 = selection[2]

    diff_x = x0 - click_x
    if diff_x < 0:
        diff_x = 0 - diff_x

    diff_y = y0 - click_y
    if diff_y < 0:
        diff_y = 0 - diff_y

    next_to_each_other = ((diff_x + diff_y) == 1)
    if next_to_each_other:
        temp = grid[y0][x0]
        grid[y0][x0] = grid[click_y][click_x]
        grid[click_y][click_x] = temp

    selection[0] = False

#----------------------------------draw---------------------------------------

def draw():
    background(255)
    fillin()
    visual()
    three_del()


run()