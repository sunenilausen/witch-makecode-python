def on_up_repeated():
    global projectileX, projectileY
    witch.set_image(sprites.swamp.witch_back0)
    witch.y += -1
    projectileX = 0
    projectileY = -50
controller.up.on_event(ControllerButtonEvent.REPEATED, on_up_repeated)

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_side(sprites.projectile.explosion1, projectileX, projectileY)
    projectile.set_position(witch.x, witch.y)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_right_repeated():
    global projectileX, projectileY
    witch.set_image(sprites.swamp.witch_right0)
    witch.x += 1
    projectileX = 50
    projectileY = 0
controller.right.on_event(ControllerButtonEvent.REPEATED, on_right_repeated)

def on_down_repeated():
    global projectileX, projectileY
    witch.set_image(sprites.swamp.witch_forward0)
    witch.y += 1
    projectileX = 0
    projectileY = 50
controller.down.on_event(ControllerButtonEvent.REPEATED, on_down_repeated)

def on_left_repeated():
    global projectileX, projectileY
    witch.set_image(sprites.swamp.witch_left0)
    witch.x += -1
    projectileX = -50
    projectileY = 0
controller.left.on_event(ControllerButtonEvent.REPEATED, on_left_repeated)

projectile: Sprite = None
witch: Sprite = None
projectileX = 0
projectileY = 0
witch = sprites.create(sprites.swamp.witch_left0, SpriteKind.player)