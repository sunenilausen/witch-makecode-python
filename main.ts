controller.up.onEvent(ControllerButtonEvent.Repeated, function on_up_repeated() {
    
    witch.setImage(sprites.swamp.witchBack0)
    witch.y += -1
    projectileX = 0
    projectileY = -50
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    projectile = sprites.createProjectileFromSide(sprites.projectile.explosion1, projectileX, projectileY)
    projectile.setPosition(witch.x, witch.y)
})
controller.right.onEvent(ControllerButtonEvent.Repeated, function on_right_repeated() {
    
    witch.setImage(sprites.swamp.witchRight0)
    witch.x += 1
    projectileX = 50
    projectileY = 0
})
controller.down.onEvent(ControllerButtonEvent.Repeated, function on_down_repeated() {
    
    witch.setImage(sprites.swamp.witchForward0)
    witch.y += 1
    projectileX = 0
    projectileY = 50
})
controller.left.onEvent(ControllerButtonEvent.Repeated, function on_left_repeated() {
    
    witch.setImage(sprites.swamp.witchLeft0)
    witch.x += -1
    projectileX = -50
    projectileY = 0
})
let projectile : Sprite = null
let witch : Sprite = null
let projectileX = 0
let projectileY = 0
witch = sprites.create(sprites.swamp.witchLeft0, SpriteKind.Player)
