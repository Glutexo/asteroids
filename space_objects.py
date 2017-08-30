from pyglet.window.key import LEFT, RIGHT, DOWN, UP

spaceship_acceleration = 50

class Spaceship:
    """ The player’s character. Keyboard controllable, moving along cartesian coordinates."""

    def __init__(self):
        """ Initialize with zero defaults. """
        self.x, self.y = 0, 0
        self.x_speed, self.y_speed = 0, 0
        self.rotation = 0

    def tick(self, dt):
        """ Move the spaceship according to its speed. """
        self.x += dt * self.x_speed
        self.y += dt * self.y_speed

    def pressed_key(self, key, dt):
        """ Key presses adjust the x_ and y_speed. making the spaceship move cartesian way."""
        if key == LEFT:
            self.x_speed -= dt * spaceship_acceleration
        if key == RIGHT:
            self.x_speed += dt * spaceship_acceleration
        if key == DOWN:
            self.y_speed -= dt * spaceship_acceleration
        if key == UP:
            self.y_speed += dt * spaceship_acceleration
