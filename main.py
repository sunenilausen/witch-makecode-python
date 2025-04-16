def on_up_repeated():
    global direction
    direction = "up"
    tank.set_image(sprites.swamp.witch_back0)
    tank.y += -1
controller.up.on_event(ControllerButtonEvent.REPEATED, on_up_repeated)

def on_a_pressed():
    global projectile
    if direction == "up":
        projectile = sprites.create_projectile_from_side(sprites.projectile.explosion1, 0, -50)
    elif direction == "down":
        projectile = sprites.create_projectile_from_side(sprites.projectile.explosion1, 0, 50)
    elif direction == "right":
        projectile = sprites.create_projectile_from_side(sprites.projectile.explosion1, 50, 0)
    else:
        projectile = sprites.create_projectile_from_side(sprites.projectile.explosion1, -50, 0)
    projectile.set_position(tank.x, tank.y)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_right_repeated():
    global direction
    direction = "right"
    tank.set_image(sprites.swamp.witch_right0)
    tank.x += 1
controller.right.on_event(ControllerButtonEvent.REPEATED, on_right_repeated)

def on_down_repeated():
    global direction
    tank.set_image(sprites.swamp.witch_forward0)
    tank.y += 1
    direction = "down"
controller.down.on_event(ControllerButtonEvent.REPEATED, on_down_repeated)

def on_left_repeated():
    global direction
    direction = "left"
    tank.set_image(sprites.swamp.witch_left0)
    tank.x += -1
controller.left.on_event(ControllerButtonEvent.REPEATED, on_left_repeated)

projectile: Sprite = None
direction = ""
tank: Sprite = None
tank = sprites.create(sprites.swamp.witch_left0, SpriteKind.player)