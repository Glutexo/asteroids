import pyglet


tick_interval = 1 / 30
spaceship_rotation_speed = 10
spaceship_acceleration = 50


def on_draw():
    window.clear()
    batch.draw()


def on_key_press(symbol, modifiers):
    pressed_keys.add(symbol)


def on_key_release(symbol, modifiers):
    pressed_keys.remove(symbol)


def tick(dt):
    for object in objects:
        object.tick(dt)


class Spaceship:
    def __init__(self, **kwargs):
        """
        Spaceship (sprite) is position somewhere (x, y) in the space (window). It is pointing (rotation) and heading
        (x_speed, y_speed) somewhere.
        """
        self.x_speed, self.y_speed = 0, 0
        self.rotation = 0
        self.sprite = kwargs['sprite']
        self.window = kwargs['window']

    def tick(self, dt):
        if pyglet.window.key.LEFT in pressed_keys:
            self.x_speed -= dt * spaceship_acceleration
        if pyglet.window.key.RIGHT in pressed_keys:
            self.x_speed += dt * spaceship_acceleration
        if pyglet.window.key.DOWN in pressed_keys:
            self.y_speed -= dt * spaceship_acceleration
        if pyglet.window.key.UP in pressed_keys:
            self.y_speed += dt * spaceship_acceleration

        self.sprite.x += dt * self.x_speed
        self.sprite.y += dt * self.y_speed
        self.rotation += dt * spaceship_acceleration


window = pyglet.window.Window()

batch = pyglet.graphics.Batch()
spaceship_image = pyglet.image.load('resources/spaceship.png')
spaceship_sprite = pyglet.sprite.Sprite(spaceship_image, batch=batch)

spaceship = Spaceship(window=window, sprite=spaceship_sprite)

objects = [spaceship]
pressed_keys = set()


window.push_handlers(on_draw=on_draw, on_key_press=on_key_press, on_key_release=on_key_release)
pyglet.clock.schedule_interval(tick, tick_interval)

pyglet.app.run()
