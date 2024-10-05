# Ball.py

import pygame
from Constants import * 

def calculate_bounce_angle(hit_position, paddle_y, paddle_height):
    segment_height = paddle_height // SEGMENTS
    relative_position = hit_position - paddle_y
    segment_hit = relative_position // segment_height
    
    if segment_hit < 0:
        segment_hit = 0
    elif segment_hit >= SEGMENTS:
        segment_hit = SEGMENTS - 1
    
    angle_map = [-3, -2, 0, 2, 3]
    return angle_map[int(segment_hit)]

def move_ball(ball_x, ball_y, ball_vx, ball_vy, height):
    ball_x += ball_vx
    ball_y += ball_vy

    if ball_y - BALL_SIZE // 2 <= 0 or ball_y + BALL_SIZE // 2 >= height:
        ball_vy = -ball_vy
    
    return ball_x, ball_y, ball_vx, ball_vy