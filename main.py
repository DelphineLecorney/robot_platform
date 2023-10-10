import sys
import pygame
from simulator import Robot, Platform


# Function to run the simulation of the robot in the pygame window
def main():
    pygame.init()
    width, height = 1200, 800
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Simulation Robot")

    robot = Robot(100, 100)

    platform = Platform(100, 700, 1000, 20)

    # Loop to run the simulation of the robot in the pygame window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()

        robot.move(keys)

        window.fill((0, 0, 0))

        robot.draw(window)

        platform.draw(window)

        pygame.display.flip()


# Run the simulation of the robot in the pygame window
if __name__ == "__main__":
    main()
