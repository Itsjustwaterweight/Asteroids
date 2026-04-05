# Asteroids Game

**Overview:**

This project is a simple 2D Asteroids-style game built using Python and the pygame library. The player controls a spaceship that can rotate, move in all directions, and shoot projectiles to destroy incoming asteroids. The game demonstrates core object-oriented programming concepts such as inheritance, polymorphism, and encapsulation, along with real-time game loop mechanics.

**Features:**

The player can rotate left and right, move forward and backward, and shoot projectiles. Asteroids spawn from the edges of the screen and move across it at varying speeds and angles. When large asteroids are hit, they split into smaller asteroids. Smaller asteroids are destroyed completely when shot. Collision detection is implemented between the player and asteroids, as well as between shots and asteroids. A cooldown system prevents the player from firing continuously without delay. The game logs events such as collisions and asteroid destruction to external files.

**Technologies Used:**

The project is written in Python and uses the pygame library for rendering graphics, handling input, and managing the game loop.

**File Structure:**

main.py is responsible for initializing the game, handling the main loop, and managing object groups.
player.py defines the Player class, including movement, rotation, and shooting behavior.
asteroid.py defines the Asteroid class, including movement and splitting logic.
asteroidfield.py handles spawning asteroids at random intervals and positions.
shot.py defines the Shot class used for projectiles fired by the player.
circleshape.py provides a base class for all circular game objects and includes shared functionality such as movement and collision detection.
constants.py stores configuration values such as screen size, speeds, and gameplay parameters.
logger.py handles logging of game state and events.

**How to Run:**

Ensure Python 3.13 is installed along with pygame version 2.6.1. Create and activate a virtual environment using uv or another environment manager. Install dependencies and run the game using the command:

uv run main.py

Alternatively, you may run the script directly with your Python interpreter if pygame is installed in your environment.

**Controls:**

The A and D keys rotate the player left and right.
The W and S keys move the player forward and backward.
The spacebar fires a projectile.

**Game Mechanics:**

The player has a circular hitbox but is visually represented as a triangle. Movement and rotation are frame-rate independent using delta time. Asteroids are generated at the edges of the screen and travel inward. When a large asteroid is destroyed, it splits into two smaller asteroids with slightly increased speed and different trajectories. Shots are also circular objects and are removed upon collision with asteroids. If the player collides with an asteroid, the game ends immediately.

**Learning Objectives:**

This project reinforces understanding of object-oriented programming, including inheritance and method overriding. It demonstrates how to use pygame sprite groups to manage multiple objects efficiently. It also introduces real-time game loop design, collision detection using vector math, and basic event logging.
