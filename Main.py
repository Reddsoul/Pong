# Main.py

import pygame
from Constants import *
from Paddle import *
from Ball import *
from GameFunctions import *
from Drawing import *
from Shape import *

# Initialize Pygame
pygame.init()

# Create the screen with the RESIZABLE flag
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Pong')

# Initialize game variables
ball_x, ball_y, ball_vx, ball_vy = WIDTH // 2, HEIGHT // 2, 5, 5
paddle1_x, paddle1_y = 50, HEIGHT // 2 - 50
paddle2_x, paddle2_y = WIDTH - 60, HEIGHT // 2 - 50

# Game loop
running = True
while running:
    pygame.time.delay(30)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_r:
                ball_x, ball_y, ball_vx, ball_vy, paddle1_x, paddle1_y, paddle2_x, paddle2_y, game_over, winner, score1, score2 = reset_game()
                game_started = False  # Reset game state
            if event.key == pygame.K_SPACE:
                if game_over:
                    ball_x, ball_y, ball_vx, ball_vy, paddle1_x, paddle1_y, paddle2_x, paddle2_y, game_over, winner, score1, score2 = reset_game()
                    game_started = False  # Reset game state after game over
                else:
                    game_started = True  # Start the game

        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            ball_x, ball_y, ball_vx, ball_vy, paddle1_x, paddle1_y, paddle2_x, paddle2_y, game_over, winner = reset_ball_and_paddles(HEIGHT, WIDTH)
            game_started = False  # Reset game state on resize

    if not game_over:
        # Handle paddle movement for Player 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle1_y > 0:  # Move up
            paddle1_y -= PADDLE_SPEED
        if keys[pygame.K_s] and paddle1_y < HEIGHT - PADDLE_HEIGHT:  # Move down
            paddle1_y += PADDLE_SPEED
        if keys[pygame.K_a] and paddle1_x > 0:  # Move left
            paddle1_x -= PADDLE_SPEED
        if keys[pygame.K_d] and paddle1_x < WIDTH // 2 - PADDLE_WIDTH:  # Move right, but not past the middle
            paddle1_x += PADDLE_SPEED

        # Handle paddle movement for Player 2
        if keys[pygame.K_i] and paddle2_y > 0:  # Move up
            paddle2_y -= PADDLE_SPEED
        if keys[pygame.K_k] and paddle2_y < HEIGHT - PADDLE_HEIGHT:  # Move down
            paddle2_y += PADDLE_SPEED
        if keys[pygame.K_j] and paddle2_x > WIDTH // 2:  # Move left, but not past the middle
            paddle2_x -= PADDLE_SPEED
        if keys[pygame.K_l] and paddle2_x < WIDTH - PADDLE_WIDTH:  # Move right
            paddle2_x += PADDLE_SPEED

    if not game_over and game_started:  # Check if the game is started
        # Update ball position
        ball_x += ball_vx
        ball_y += ball_vy

        # Ball collision with top and bottom walls
        if ball_y - BALL_SIZE // 2 <= 0 or ball_y + BALL_SIZE // 2 >= HEIGHT:
            ball_vy = -ball_vy  # Reverse the vertical direction
            
        next_ball_x = ball_x + ball_vx
        next_ball_y = ball_y + ball_vy

        # Check if the ball is colliding with the front of the paddle
        if paddle1_x < next_ball_x < paddle1_x + PADDLE_WIDTH and paddle1_y <= next_ball_y <= paddle1_y + PADDLE_HEIGHT:
            if ball_vx < 0:  # Only reverse direction if the ball is moving towards the paddle
                ball_x = paddle1_x + PADDLE_WIDTH + BALL_SIZE // 2  # Reposition ball to avoid overlap
                ball_vx = abs(ball_vx)  # Ensure ball moves to the right
                ball_vy += calculate_bounce_angle(ball_y, paddle1_y, PADDLE_HEIGHT)

        if paddle2_x < next_ball_x < paddle2_x + PADDLE_WIDTH and paddle2_y <= next_ball_y <= paddle2_y + PADDLE_HEIGHT:
            if ball_vx > 0:  # Only reverse direction if the ball is moving towards the paddle
                ball_x = paddle2_x - BALL_SIZE // 2  # Reposition ball to avoid overlap
                ball_vx = -abs(ball_vx)  # Ensure ball moves to the left
                ball_vy += calculate_bounce_angle(ball_y, paddle2_y, PADDLE_HEIGHT)

        # Clamp ball velocity to prevent it from going too fast
        ball_vx = max(-MAX_BALL_SPEED, min(MAX_BALL_SPEED, ball_vx))
        ball_vy = max(-MAX_BALL_SPEED, min(MAX_BALL_SPEED, ball_vy))

        # Check for goals
        if ball_x < 0:
            score2 += 1
            ball_x, ball_y, ball_vx, ball_vy, paddle1_x, paddle1_y, paddle2_x, paddle2_y, game_over, winner = reset_ball_and_paddles(HEIGHT, WIDTH)
            ball_vx = ball_favor(2)
            game_started = False  # Stop the game after a goal
        if ball_x > WIDTH:
            score1 += 1
            ball_x, ball_y, ball_vx, ball_vy, paddle1_x, paddle1_y, paddle2_x, paddle2_y, game_over, winner = reset_ball_and_paddles(HEIGHT, WIDTH)
            ball_vx = ball_favor(1)
            game_started = False  # Stop the game after a goal

        # Check for a winner
        if score1 >= WINNING_SCORE:
            game_over = True
            winner = "Player 1"
        elif score2 >= WINNING_SCORE:
            game_over = True
            winner = "Player 2"

    # Draw everything
    screen.fill(BLACK)
    draw_middle_line(screen, HEIGHT)
    draw_paddles(screen, paddle1_x, paddle1_y, paddle2_x, paddle2_y)
    draw_ball(screen, ball_x, ball_y)

    # Display the scores
    font = pygame.font.Font(None, 74)
    text = font.render(str(score1), 1, WHITE)
    screen.blit(text, (WIDTH // 2 - 100, 10))
    text = font.render(str(score2), 1, WHITE)
    screen.blit(text, (WIDTH // 2 + 100, 10))

    if game_over:
        # Display the winner
        screen.fill(BLACK)
        font = pygame.font.Font(None, 74)
        win_text = font.render(f"{winner} Wins!", 1, WHITE)
        screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - win_text.get_height() // 2))

    pygame.display.flip()

pygame.quit()