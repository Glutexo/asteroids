import pyglet
from space_objects import Spaceship


tick_interval = 1 / 30

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
    """ Call some methods for every object: A general _tick_ once and a _pressed_key_ for every key pressed. """
    for (space_object, sprite) in space_objects.items():
        space_object.tick(dt)
        for key in pressed_keys:
            space_object.pressed_key(key, dt)
        sprite.x, sprite.y = space_object.x, space_object.y

# Helper functions

def sprite(path):
    """ Instantiate a new Pyglet sprite in a batch. """
    image = pyglet.image.load(path)
    return pyglet.sprite.Sprite(image, batch=batch)

# Instantiate global variables.

window = pyglet.window.Window()

batch = pyglet.graphics.Batch()
space_objects = { Spaceship(): sprite('resources/spaceship.png') }
pressed_keys = set()

# Bind events.

window.push_handlers(on_draw=on_draw, on_key_press=on_key_press, on_key_release=on_key_release)
pyglet.clock.schedule_interval(tick, tick_interval)

# And run!

pyglet.app.run()
