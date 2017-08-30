import pyglet
from space_objects import Spaceship
from collections import namedtuple


TICK_INTERVAL = 1 / 30


# Pyglet window events


def on_draw():
    """ Redraw screen with all sprites. """
    window.clear()
    batch.draw()


def on_key_press(symbol, modifiers):
    """ Add to set to track the time pressed. """
    pressed_keys.add(symbol)


def on_key_release(symbol, modifiers):
    """ Remove from set. """
    pressed_keys.remove(symbol)


# Pyglet clock events


def tick(dt):
    """
    Call some methods for every object: A general _tick_ once and a _pressed_key_ for every key pressed.
    Default rotation is used, because pyglet sprites are pointing to the right, but image may be pointing in a different
    direction.
    """
    for game_object in space_objects:
        game_object.space_object.tick(dt)
        for key in pressed_keys:
            game_object.space_object.pressed_key(key, dt)
        game_object.sprite.x, game_object.sprite.y = game_object.space_object.x, game_object.space_object.y
        game_object.sprite.rotation = game_object.space_object.rotation + game_object.rotation


# Helper functions


def sprite(path, scale=1):
    """
    Instantiate a new Pyglet sprite in a batch.
    Scale is immutable in this game, thus set only once.
    """
    image = pyglet.image.load(path)
    image.anchor_x, image.anchor_y = image.width // 2, image.height // 2 # Anchor in the center.
    sprite = pyglet.sprite.Sprite(image, batch=batch)
    sprite.scale = scale
    return sprite


# Helper structs.


# GameObject insulates SpaceObject from interface internalities.
GameObject = namedtuple('GameObject', ['space_object', 'sprite', 'rotation'])


# Instantiate global variables.

window = pyglet.window.Window()

batch = pyglet.graphics.Batch()
space_objects = set([
    GameObject(Spaceship(window.width // 2, window.height // 2), sprite('resources/spaceship.png', 0.5), 90)
])
pressed_keys = set()

# Bind events.

window.push_handlers(on_draw=on_draw, on_key_press=on_key_press, on_key_release=on_key_release)
pyglet.clock.schedule_interval(tick, TICK_INTERVAL)

# And run!

pyglet.app.run()
