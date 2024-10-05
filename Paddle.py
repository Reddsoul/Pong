# Paddle.py

import pygame
from Constants import *

def move_paddle(keys, paddle_x, paddle_y, up_key, down_key, left_key, right_key, width, height, side):
    if keys[up_key] and paddle_y > 0:  # Move up
        paddle_y -= PADDLE_SPEED
    if keys[down_key] and paddle_y < height - PADDLE_HEIGHT:  # Move down
        paddle_y += PADDLE_SPEED
    if side == 'left' and keys[left_key] and paddle_x > 0:  # Move left
        paddle_x -= PADDLE_SPEED
    if side == 'left' and keys[right_key] and paddle_x < width // 2 - PADDLE_WIDTH:  # Move right
        paddle_x += PADDLE_SPEED
    if side == 'right' and keys[left_key] and paddle_x > width // 2:  # Move left
        paddle_x -= PADDLE_SPEED
    if side == 'right' and keys[right_key] and paddle_x < width - PADDLE_WIDTH:  # Move right
        paddle_x += PADDLE_SPEED
    
    return paddle_x, paddle_y