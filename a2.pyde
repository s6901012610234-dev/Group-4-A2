from processing import *
import random

grid_size = [10,10]
screen_size = [500,500]
grid = []
letters = ["R","G","B","Y"]
selection = [False, 0, 0]


def setup():
    size(screen_size[0],screen_size[1])
    strokeWeight(1)
    x = 0
    while x < grid_size[1]:
        row = []
        y = 0
        while y < grid_size[0]:
            row.append(".")
            y = y + 1
        grid.append(row)
        x = x + 1


def get_colour(letter):
    if letter == "R":
        return [255,100,100]
    if letter == "G":
        return [100,255,100]
    if letter == "B":
        return [100,100,255]
    if letter == "Y":
        return [255,255,100]
    return [255,255,255]


def fillin():
    a = 0
    while a < grid_size[1]:
        b = 0
        while b < grid_size[0]:
            if grid[a][b] == ".":
                grid[a][b] = letters[random.randint(0,3)]
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
            fill_colour = get_colour(grid[y][x])
            fill(fill_colour[0], fill_colour[1], fill_colour[2])
            ellipse(cellx, celly, cell_width * 0.75, cell_height * 0.75)

            if selection[0] == True:
                if x == selection[1]:
                    if y == selection[2]:
                        noFill()
                        stroke(0,0,0)
                        strokeWeight(3)
                        ellipse(cellx, celly, cell_width * 0.9, cell_height * 0.9)
                        strokeWeight(1)
                        
            x = x + 1
        y = y + 1


def three_del():
    y = 0
    while y < grid_size[1]:
        x = 0
        while x < grid_size[0]:
            candy = grid[y][x]

            if candy != ".":
                if x + 2 < grid_size[0]:
                    if candy == grid[y][x+1] and candy == grid[y][x+2]:
                            grid[y][x] = "."
                            grid[y][x+1] = "."
                            grid[y][x+2] = "."

                if y + 2 < grid_size[1]:
                    if candy == grid[y+1][x] and candy == grid[y+2][x]:
                            grid[y][x] = "."
                            grid[y+1][x] = "."
                            grid[y+2][x] = "."

            x = x + 1
        y = y + 1


def fall():
    x = 0
    while x < grid_size[0]:
        stack = []
        y = grid_size[1] - 1
        while y >= 0:
            if grid[y][x] != ".":
                stack.append(grid[y][x])
            y = y - 1

        y = grid_size[1] - 1
        idx = 0
        while y >= 0:
            if idx < len(stack):
                grid[y][x] = stack[idx]
            else:
                grid[y][x] = "."
            idx = idx + 1
            y = y - 1
        x = x + 1


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


def keyPressed():
    if key == 's':
        save_game()
    if key == 'l':
        load_game()


def save_game():
    text = ""
    y = 0
    while y < grid_size[1]:
        row_text = ""
        x = 0
        while x < grid_size[0]:
            row_text = row_text + grid[y][x]
            x = x + 1
        text = text + row_text
        if y < grid_size[1] - 1:
            text = text + "\n"
        y = y + 1

    with open("save.txt", "w") as f:
        f.write(text)


def load_game():
    with open("save.txt", "r") as f:
        content = f.read()

    lines = []
    current_line = ""
    i = 0
    while i < len(content):
        ch = content[i]
        if ch == "\n":
            lines.append(current_line)
            current_line = ""
        else:
            current_line = current_line + ch
        i = i + 1
    lines.append(current_line)

    y = 0
    while y < grid_size[1]:
        line_text = lines[y]
        x = 0
        while x < grid_size[0]:
            grid[y][x] = line_text[x]
            x = x + 1
        y = y + 1


def draw():
    background(255)
    fillin()
    three_del()
    fall()
    fillin()
    visual()


run()