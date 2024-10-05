# GameFunctions.py

from Constants import *

# GameFunctions.py

def reset_ball_and_paddles(HEIGHT, WIDTH):
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    ball_vx = BALL_SPEED_X
    ball_vy = BALL_SPEED_Y
    paddle1_x = 50  # Paddle 1 close to the left wall
    paddle1_y = HEIGHT // 2 - PADDLE_HEIGHT // 2 
    paddle2_x = WIDTH - 50  # Paddle 2 close to the right wall
    paddle2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
    game_over = False
    winner = None
    
    return ball_x, ball_y, ball_vx, ball_vy, paddle1_x, paddle1_y, paddle2_x, paddle2_y, game_over, winner

def reset_game():
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    ball_vx = BALL_SPEED_X
    ball_vy = BALL_SPEED_Y
    paddle1_x = 50  # Paddle 1 close to the left wall
    paddle1_y = HEIGHT // 2 - PADDLE_HEIGHT // 2 
    paddle2_x = WIDTH - 50  # Paddle 2 close to the right wall
    paddle2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
    game_over = False
    winner = None
    score1 = 0
    score2 = 0

    return ball_x, ball_y, ball_vx, ball_vy, paddle1_x, paddle1_y, paddle2_x, paddle2_y, game_over, winner, score1, score2

def ball_favor (scoring_player = None):
    if scoring_player == 1:
        ball_vx = BALL_SPEED_X  # Move towards Player 2
    elif scoring_player == 2:
        ball_vx = -BALL_SPEED_X  # Move towards Player 1
    else:
        ball_vx = BALL_SPEED_X  # Reset to default direction

    return ball_vx
    