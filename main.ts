controller.up.onEvent(ControllerButtonEvent.Repeated, function on_up_repeated() {
    
    direction = "up"
    tank.setImage(sprites.swamp.witchBack0)
    tank.y += -1
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    if (direction == "up") {
        projectile = sprites.createProjectileFromSide(sprites.projectile.explosion1, 0, -50)
    } else if (direction == "down") {
        projectile = sprites.createProjectileFromSide(sprites.projectile.explosion1, 0, 50)
    } else if (direction == "right") {
        projectile = sprites.createProjectileFromSide(sprites.projectile.explosion1, 50, 0)
    } else {
        projectile = sprites.createProjectileFromSide(sprites.projectile.explosion1, -50, 0)
    }
    
    projectile.setPosition(tank.x, tank.y)
})
controller.right.onEvent(ControllerButtonEvent.Repeated, function on_right_repeated() {
    
    direction = "right"
    tank.setImage(sprites.swamp.witchRight0)
    tank.x += 1
})
controller.down.onEvent(ControllerButtonEvent.Repeated, function on_down_repeated() {
    
    tank.setImage(sprites.swamp.witchForward0)
    tank.y += 1
    direction = "down"
})
controller.left.onEvent(ControllerButtonEvent.Repeated, function on_left_repeated() {
    
    direction = "left"
    tank.setImage(sprites.swamp.witchLeft0)
    tank.x += -1
})
let projectile : Sprite = null
let direction = ""
let tank : Sprite = null
tank = sprites.create(sprites.swamp.witchLeft0, SpriteKind.Player)
