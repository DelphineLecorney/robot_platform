import pygame


# Class Robot for the simulation of the robot in the pygame window (main.py)
class Robot:
    def __init__(self, x, y):
        self.wheel_y = None
        self.wheel_x = None
        self.x = x
        self.y = y
        self.color_body = (0, 0, 255)  # Color body of the robot
        self.color_head = (255, 0, 0)  # Color head of the robot
        self.color_arms = (0, 255, 0)  # Color arms of the robot
        self.color_wheel = [255, 0, 0]  # Color of the wheel
        self.speed = 0.5  # Speed of the robot
        self.wheel_radius = 10  # Radius of the wheel

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

        # Calculating the coordinates of the wheel
        self.wheel_x = self.x
        self.wheel_y = self.y + 40  # Position the wheel below the robot's body

    # Function to draw the robot in the pygame window (main.py)
    def draw(self, window):
        # Body drawing
        pygame.draw.rect(window, self.color_body, pygame.Rect(self.x - 20, self.y, 40, 40))

        # Head drawing
        pygame.draw.circle(window, self.color_head, (self.x, self.y - 30), 20)

        # Arms drawing
        pygame.draw.line(window, self.color_arms, (self.x - 20, self.y), (self.x + 20, self.y), 8)

        # Forearms drawing
        pygame.draw.line(window, self.color_arms, (self.x - 10, self.y + 20), (self.x - 20, self.y + 20), 8)
        pygame.draw.line(window, self.color_arms, (self.x + 10, self.y + 20), (self.x + 20, self.y + 20), 8)

        # Wheel drawing
        pygame.draw.circle(window, self.color_wheel, (self.wheel_x, self.wheel_y), self.wheel_radius)


class Platform:
    platforms = []

    # Function to draw the platform in the pygame window (main.py)
    def __init__(self, x, y, width, height):
        self.platforms.append(pygame.Rect(x, y, width, height))
        self.color = (162, 162, 162)  # Color of the platform
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # Function to draw the platform in the pygame window (main.py)
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    # Function to get the platforms in the pygame window (main.py)
    def get_platforms(self):
        return self.platforms

    def collision(self, robot):
        if self.x <= robot.wheel_x <= self.x + self.width:
            if self.y <= robot.wheel_y + robot.wheel_radius <= self.y + self.height:
                return True
        return False
