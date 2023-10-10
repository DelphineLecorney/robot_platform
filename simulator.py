import pygame


# Class Robot for the simulation of the robot in the pygame window (main.py)
class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color_body = (0, 0, 255)  # Color body of the robot
        self.color_head = (255, 0, 0)  # Color head of the robot
        self.color_arms = (0, 255, 0)  # Color arms of the robot
        self.speed = 1

    # Function to move the robot in the pygame window (main.py)
    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    # Function to draw the robot in the pygame window (main.py)
    def draw(self, window):
        # Body drawing
        pygame.draw.rect(window, self.color_body, pygame.Rect(self.x - 30, self.y - 20, 60, 40))

        # Head drawing
        pygame.draw.circle(window, self.color_head, (self.x, self.y - 40), 20)

        # Arms drawing
        pygame.draw.line(window, self.color_arms, (self.x - 20, self.y), (self.x + 20, self.y), 8)

        # Forearms drawing
        pygame.draw.line(window, self.color_arms, (self.x - 10, self.y + 20), (self.x - 20, self.y + 40), 8)
        pygame.draw.line(window, self.color_arms, (self.x + 10, self.y + 20), (self.x + 20, self.y + 40), 8)
