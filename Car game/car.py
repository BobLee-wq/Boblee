import pygame
import random

pygame.init()

# Set up the display
screen_width = 700
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Game")

# Set up the game clock
clock = pygame.time.Clock()

# Load the images
car_img = pygame.image.load("car.png")
car_width = 60
car_height = 120

# Set up the game variables
car_x = screen_width // 2 - car_width // 2
car_y = screen_height - car_height - 10
car_speed = 20

obstacle_width = 80
obstacle_height = 80
obstacle_x = random.randint(0, screen_width - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 5

# Define the functions
def draw_car(x, y):
    screen.blit(car_img, (x, y))

def draw_obstacle(x, y):
    pygame.draw.rect(screen, (255, 0, 0), (x, y, obstacle_width, obstacle_height))

def game_loop():
    global car_x, car_y, obstacle_x, obstacle_y
    
    game_over = False
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        
        # Move the car
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x > 0:
            car_x -= car_speed
        elif keys[pygame.K_RIGHT] and car_x < screen_width - car_width:
            car_x += car_speed
        
        # Move the obstacle
        obstacle_y += obstacle_speed
        if obstacle_y > screen_height:
            obstacle_x = random.randint(0, screen_width - obstacle_width)
            obstacle_y = -obstacle_height
        
        # Check for collision
        if car_y < obstacle_y + obstacle_height:
            if car_x < obstacle_x + obstacle_width and car_x + car_width > obstacle_x:
                game_over = True
        
        # Clear the screen
        screen.fill((255, 255, 255))
        
        # Draw the car and the obstacle
        draw_car(car_x, car_y)
        draw_obstacle(obstacle_x, obstacle_y)
        
        # Update the display
        pygame.display.update()
        
        # Set the game clock
        clock.tick(60)
    
    pygame.quit()
    quit()

game_loop()
