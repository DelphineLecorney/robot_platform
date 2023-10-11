
# Robot simulation with Pygame

This project is a robot simulation using the Pygame library. It visualizes a robot that can move around the screen and interact with platforms.

## Installation

1. Clone this repository to your computer.

```shell
git clone https://github.com/votre-utilisateur/robot-platform.git
```

Make sure you have Python and Pygame installed.


```Copy code
pip install pygame
```


## Utilisation 
Run the main program main.py to start the robot simulation.

```Copy code
python main.py
```


## Fonctionnalités

Move the robot using the arrow keys.
Add multiple platforms to create levels.
Collision management between robot and platforms.

## Structure du projet
```Copy code
main.py: The program's entry point.
```

```Copy code
simulator.py: The file containing the Simulator class for managing the simulation.
```

```Copy code
README.md: This documentation file.
```
## Collision Management

In this robot simulation, I manage collisions between the robot and platforms. When the robot collides with a platform, I perform the following actions:

1. I display the text "Collision" on the screen for two seconds to indicate to the player that a collision has occurred.
2. The robot is returned to its initial position (coordinates x = 100 and y = 100) to prevent it from getting stuck in the platform.

## Contributions
Contributions to this project are welcome ! If you wish to contribute, please open a Pull Request with your modifications.

## License
This project is licensed under the MIT license. See the LICENSE file for more details.
<h2 align="left"> Contact me : </h2> <a href="https://www.linkedin.com/in/delphine-lecorney/" target="_blank"><sub><b>Delphine</b></sub>