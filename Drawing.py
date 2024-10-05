# Drawing.py

import pygame
from Constants import *

def draw_middle_line(screen, height):
    for i in range(10, height, 40):
        pygame.draw.line(screen, WHITE, (pygame.display.get_surface().get_width() // 2, i), (pygame.display.get_surface().get_width() // 2, i + 20), 2)

def display_scores(screen, score1, score2):
    font = pygame.font.Font(None, 74)
    
    # Display score1 250 pixels from the left wall
    text1 = font.render(str(score1), 1, WHITE)
    screen.blit(text1, (250, 10))
    
    # Display score2 250 pixels from the right wall
    text2 = font.render(str(score2), 1, WHITE)
    screen_width = pygame.display.get_surface().get_width()
    screen.blit(text2, (screen_width - text2.get_width() - 250, 10))