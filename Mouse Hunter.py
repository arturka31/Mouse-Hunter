from random import randint

def draw_grid(grid):
    for row in grid:
        print(" ".join(row))

def hide_mouse(grid_size):
    mouse_row = randint(1,grid_size)
    mouse_col = randint(1,grid_size)
    return (mouse_col,mouse_row)
def distance_to_mouse(x,y,mx,my):
    return abs(x-mx) + abs(y-my)


def main():
    grid_size = 5
    guess_limit = 3
    play = True

    while play:
        grid = [["O" for x in range(grid_size)] for y in range(grid_size)]

        mousex, mousey = hide_mouse(grid_size)

        guesses_taken = 0
        draw_grid(grid)
        while guesses_taken < guess_limit:
            print('Guess {} of {}...'.format(guesses_taken+1,guess_limit))
            print('Guess row:')
            guess_row = input()
            guess_row = int(guess_row)
            print('Guess col:')
            guess_col = input()
            guess_col = int(guess_col)
            mdist = distance_to_mouse(guess_row, guess_col, mousex, mousey)
            if mdist == 0:
                grid[guess_row-1][guess_col-1] = 'x'
                draw_grid(grid)
                print('Congrats! You caught the mouse in {} moves.'.format(guesses_taken+1))
                break
            grid[guess_row-1][guess_col-1] = str(mdist)
            draw_grid(grid)
            guesses_taken += 1


        print('Want to play again? y/n')
        again = input()
        if str(again) == 'n':
            play = False;

if __name__ == '__main__':
  main()
