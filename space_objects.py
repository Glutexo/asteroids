from pyglet.window.key import LEFT, RIGHT, DOWN, UP
from math import sin, cos, radians


SPACESHIP_ACCELERATION = 100
SPACESHIP_ROTATION_SPEED = 100


def spaceship_acceleration_x(dt, rotation):
    """ X is positive to the right, rotation 0 is pointing to the right. """
    return dt * SPACESHIP_ACCELERATION * cos(radians(rotation))


def spaceship_acceleration_y(dt, rotation):
    """ Y is positive to the top, rotation is clockwise, meaning down from 0, which is to the right. """
    return dt * SPACESHIP_ACCELERATION * -sin(radians(rotation))


def spaceship_rotation(dt):
    return dt * SPACESHIP_ROTATION_SPEED


class Spaceship:
    """ The player’s character. Keyboard controllable. """

    def __init__(self, x=0, y=0, rotation=0):
        """ Initialize with zero defaults. """
        self.x, self.y = x, y
        self.rotation = rotation

        self.x_speed, self.y_speed = 0, 0

    def tick(self, dt):
        """ Move the spaceship according to its speed. """
        self.x += dt * self.x_speed
        self.y += dt * self.y_speed

    def pressed_key(self, key, dt):
        """ UP/DOWN adjust speed, LEFT/RIGHT adjust rotation."""
        if key == LEFT:
            self.rotation -= spaceship_rotation(dt)
        if key == RIGHT:
            self.rotation += spaceship_rotation(dt)
        if key == DOWN:
            self.x_speed -= spaceship_acceleration_x(dt, self.rotation)
            self.y_speed -= spaceship_acceleration_y(dt, self.rotation)
        if key == UP:
            self.x_speed += spaceship_acceleration_x(dt, self.rotation)
            self.y_speed += spaceship_acceleration_y(dt, self.rotation)
