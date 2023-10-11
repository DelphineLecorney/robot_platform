import sys
import pygame
import pygame.font
from simulator import Robot, Platform


# Function to run the simulation of the robot in the pygame window
def main():
    pygame.init()
    width, height = 1200, 800
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Simulation Robot")

    robot = Robot(100, 100)

    platform = Platform(100, 600, 1000, 20)
    platform2 = Platform(100, 400, 1000, 20)
    platform3 = Platform(100, 200, 1000, 20)

    # Font to display the text in the pygame window
    font = pygame.font.Font(None, 100)

    # Loop to run the simulation of the robot in the pygame window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()

        # Save the old coordinates of the robot
        old_x, old_y = robot.x, robot.y

        robot.move(keys)

        # If the robot collides with the platform, restore its old coordinates
        if platform.collision(robot) or platform2.collision(robot) or platform3.collision(robot):
            collision_text = font.render("Collision", True, (255, 0, 0))
            text_rect = collision_text.get_rect(center=(width // 2, height // 2))
            window.blit(collision_text, text_rect)
            pygame.display.flip()  # Update the pygame window
            pygame.time.delay(2000)  # Wait 2 seconds
            robot.x = 100
            robot.y = 100
        else:
            robot.move(keys)

        # If the robot goes out of the window, restore its old coordinates
        if not (0 <= robot.x <= width - 40) or not (0 <= robot.y <= height - 60):
            robot.x, robot.y = old_x, old_y

        # Draw the robot and the platform in the pygame window
        window.fill((0, 0, 0))
        robot.draw(window)
        platform.draw(window)
        platform2.draw(window)
        platform3.draw(window)

        # Update the pygame window
        pygame.display.flip()


# Run the simulation of the robot in the pygame window
if __name__ == "__main__":
    main()
