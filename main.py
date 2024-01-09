import pygame

# Initialize pygame module
pygame.init()

# Set Width and Height of the Chess Game screen
WIDTH = 640
HEIGHT = 640

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Two-Player Chess Game')

# Fonts
font = pygame.font.Font('fonts/Bubblegum.ttf', 20)
mid_font = pygame.font.Font('fonts/Bubblegum.ttf', 40)
big_font = pygame.font.Font('fonts/Bubblegum.ttf', 50)

# Clock and Frames per Second
timer = pygame.time.Clock()
fps = 60

# Game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

captured_pieces_white = []
captured_pieces_black = []

# 0 - white's turn no selection:
# 1-white's turn piece selected:
# 2- black's turn no selection
# 3 - black's turn piece selected

turn_step = 0
selection = 100
valid_moves = []

#Importing Chess Pieces
'''**********************************<BLACK PIECES>************************************'''

piece_width = WIDTH/9
piece_height = HEIGHT/9
piece_width_small = piece_width/2
piece_height_small = piece_height/2

black_queen = pygame.image.load('chess_pieces_imgs/Chess_qdt60.png')
black_queen = pygame.transform.scale(black_queen, (piece_width, piece_height))
black_queen_small = pygame.transform.scale(black_queen, (piece_width_small, piece_height_small))

black_king = pygame.image.load('chess_pieces_imgs/Chess_kdt60.png')
black_king = pygame.transform.scale(black_king, (piece_width, piece_height))
black_king_small = pygame.transform.scale(black_king, (piece_width_small, piece_height_small))

black_rook = pygame.image.load('chess_pieces_imgs/Chess_rdt60.png')
black_rook = pygame.transform.scale(black_rook, (piece_width, piece_height))
black_rook_small = pygame.transform.scale(black_rook, (piece_width_small, piece_height_small))

black_bishop = pygame.image.load('chess_pieces_imgs/Chess_bdt60.png')
black_bishop = pygame.transform.scale(black_bishop, (piece_width, piece_height))
black_bishop_small = pygame.transform.scale(black_bishop, (piece_width_small, piece_height_small))

black_knight = pygame.image.load('chess_pieces_imgs/Chess_ndt60.png')
black_knight = pygame.transform.scale(black_knight, (piece_width, piece_height))
black_knight_small = pygame.transform.scale(black_knight, (piece_width_small, piece_height_small))

black_pawn = pygame.image.load('chess_pieces_imgs/Chess_pdt60.png')
black_pawn = pygame.transform.scale(black_pawn, (9*piece_width/10, 9*piece_height/10))
black_pawn_small = pygame.transform.scale(black_pawn, (piece_width_small, piece_height_small))

'''*************************************<WHITE PIECES>****************************************'''

white_queen = pygame.image.load('chess_pieces_imgs/Chess_qlt60.png')
white_queen = pygame.transform.scale(white_queen, (piece_width, piece_height))
white_queen_small = pygame.transform.scale(white_queen, (piece_width_small, piece_height_small))

white_king = pygame.image.load('chess_pieces_imgs/Chess_klt60.png')
white_king = pygame.transform.scale(white_king, (piece_width, piece_height))
white_king_small = pygame.transform.scale(white_king, (piece_width_small, piece_height_small))

white_rook = pygame.image.load('chess_pieces_imgs/Chess_rlt60.png')
white_rook = pygame.transform.scale(white_rook, (piece_width, piece_height))
white_rook_small = pygame.transform.scale(white_rook, (piece_width_small, piece_height_small))

white_bishop = pygame.image.load('chess_pieces_imgs/Chess_blt60.png')
white_bishop = pygame.transform.scale(white_bishop, (piece_width, piece_height))
white_bishop_small = pygame.transform.scale(white_bishop, (piece_width_small, piece_height_small))

white_knight = pygame.image.load('chess_pieces_imgs/Chess_nlt60.png')
white_knight = pygame.transform.scale(white_knight, (piece_width, piece_height))
white_knight_small = pygame.transform.scale(white_knight, (piece_width_small, piece_height_small))

white_pawn = pygame.image.load('chess_pieces_imgs/Chess_plt60.png')
white_pawn = pygame.transform.scale(white_pawn, (9*piece_width/10, 9*piece_height/10))
white_pawn_small = pygame.transform.scale(white_pawn, (piece_width_small, piece_height_small)   )

'''**************************************************************************************'''

white_images = [white_pawn, white_queen, white_king,
                white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]

black_images = [black_pawn, black_queen, black_king,
                black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

# Check variables/ flashing counter
counter = 0
winner = ''
game_over = False


# Draw main game board
def draw_board(screen_width, screen_height):
    for row in range(8):
        for col in range(8):
            x = col * (screen_width / 8)
            y = row * (screen_height / 8)
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, '#3FB422', (x, y, screen_width / 8, screen_height / 8))
            else:
                pygame.draw.rect(screen, '#B0F49F', (x, y, screen_width / 8, screen_height / 8))

    pygame.draw.rect(screen, 'gold', [0, screen_height, screen_width, screen_height / 8], 5)
    pygame.draw.rect(screen, 'gold', [screen_width, 0, screen_width / 8, screen_height], 5)
    status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                   'Black: Select a Piece to Move!', 'Black: Select a Destination!']
    screen.blit(big_font.render(
        status_text[turn_step], True, 'black'), (20, 820))
    for i in range(9):
        pygame.draw.line(screen, 'black', (0, (screen_height / 8) * i), (screen_width, (screen_height / 8) * i), 2)
        pygame.draw.line(screen, 'black', ((screen_width / 8) * i, 0), ((screen_width / 8) * i, screen_height), 2)
    screen.blit(mid_font.render('FORFEIT', True, 'black'), (screen_width + 20, screen_height + 30))


# Draw pieces onto board
def draw_pieces(screen_width, screen_height, rect_width, rect_height):
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(
                white_pawn, (white_locations[i][0] * screen_width / 8 + rect_width / 20,
                             white_locations[i][1] * screen_height / 8 + rect_height / 20))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * screen_width / 8 + rect_width / 40,
                                              white_locations[i][1] * screen_height / 8 + rect_height / 40))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * screen_width / 8 + 1,
                                                 white_locations[i][1] * screen_height / 8 + 1, screen_width / 8,
                                                 screen_height / 8], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(
                black_pawn, (black_locations[i][0] * screen_width / 8 + rect_width / 20,
                             black_locations[i][1] * screen_height / 8 + rect_height / 20))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * screen_width / 8 + rect_width / 40,
                                              black_locations[i][1] * screen_height / 8 + rect_height / 40))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * screen_width / 8 + 1,
                                                  black_locations[i][1] * screen_height / 8 + 1, screen_width / 8,
                                                  screen_height / 8], 2)

# Function to check all pieces' valid options on the board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list


# Check king valid moves
def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0),
               (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


# Check queen valid moves
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list


# Check bishop moves
def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append(
                    (position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


# Check rook moves
def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append(
                    (position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


# Check valid pawn moves
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

# Check valid knight moves
def check_knight(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (2, 1), (2, -1),
               (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


# Check for valid moves for the selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options


# Draw valid moves on screen
def draw_valid(moves, screen_width, screen_height):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(
            screen, color,
            (moves[i][0] * screen_width / 8 + screen_width / 16, moves[i][1] * screen_height / 8 + screen_height / 16),
            5)


# Draw captured pieces on the side of the screen
def draw_captured(screen_width, screen_height, diff_width, diff_height):

    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (screen_width+(diff_width/4), (screen_height/40) + (screen_height/16) * i))
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (screen_width+(3*diff_width/4), (screen_height/40) + (screen_height/16)* i))


# Draw a flashing square around the king if in check
def draw_check(screen_width, screen_height):
    if turn_step < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [white_locations[king_index][0] * screen_width / 8 + 1,
                                                              white_locations[king_index][1] * screen_height / 8 + 1,
                                                              screen_width / 8, screen_height / 8], 5)
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark blue', [black_locations[king_index][0] * 100 + 1,
                                                               black_locations[king_index][1] * 100 + 1, 100, 100], 5)


# Draw game over screen
def draw_game_over():
    pygame.draw.rect(screen, 'black', [screen_width / 4, screen_height / 4, 400, 200])
    screen.blit(font.render(
        f'{winner} won the game!', True, 'white'), ((screen_width / 4) + 100, (screen_height / 4) + 50))
    screen.blit(font.render(f'Press ENTER to Restart!',
                            True, 'white'), ((screen_width / 4) + 100, (screen_height / 4) + 100))


# Main game loop
screen_width = WIDTH - (WIDTH / 8)
screen_height = HEIGHT - (HEIGHT / 8)
rect_width = screen_width / 8
rect_height = screen_height / 8

diff_width = WIDTH / 8
diff_height = HEIGHT / 8

black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')
run = True
while run:
    timer.tick(fps)
    if counter < 30:
        counter += 1
    else:
        counter = 0
    screen.fill('#8EF1E9')

    draw_board(screen_width, screen_height)
    draw_pieces(screen_width, screen_height, rect_width, rect_height)
    draw_captured(screen_width, screen_height, diff_width, diff_height)
    draw_check(screen_width, screen_height)
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves, screen_width, screen_height)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // (screen_width/8)
            y_coord = event.pos[1] // (screen_height/8)
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_locations[selection] = click_coords
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options(
                        black_pieces, black_locations, 'black')
                    white_options = check_options(
                        white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    black_locations[selection] = click_coords
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(
                        black_pieces, black_locations, 'black')
                    white_options = check_options(
                        white_pieces, white_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                winner = ''
                white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                captured_pieces_white = []
                captured_pieces_black = []
                turn_step = 0
                selection = 100
                valid_moves = []
                black_options = check_options(
                    black_pieces, black_locations, 'black')
                white_options = check_options(
                    white_pieces, white_locations, 'white')

    if winner != '':
        game_over = True
        draw_game_over()

    pygame.display.flip()

pygame.quit()
