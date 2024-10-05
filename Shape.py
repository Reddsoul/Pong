#Shape.py

import pygame
from Constants import *

def draw_ball(screen, ball_x, ball_y):
    pygame.draw.ellipse(screen, WHITE, (ball_x - BALL_SIZE // 2, ball_y - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE))

def draw_paddles(screen, paddle1_x, paddle1_y, paddle2_x, paddle2_y):
    pygame.draw.rect(screen, WHITE, (paddle1_x, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (paddle2_x, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    