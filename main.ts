namespace SpriteKind {
    export const boss = SpriteKind.create()
}

sprites.onOverlap(SpriteKind.Player, SpriteKind.boss, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    scene.cameraShake(4, 500)
    otherSprite.destroy(effects.disintegrate)
    sprite.startEffect(effects.fire, 200)
    info.changeLifeBy(-3)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    projectile = sprites.createProjectileFromSprite(img`
            . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        `, ship, 0, -140)
    projectile.startEffect(effects.coolRadial, 100)
    music.bigCrash.play()
})
sprites.onOverlap(SpriteKind.Food, SpriteKind.Player, function on_on_overlap2(sprite2: Sprite, otherSprite2: Sprite) {
    info.changeLifeBy(1)
    sprite2.destroy()
    music.baDing.play()
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.boss, function on_on_overlap3(sprite3: Sprite, otherSprite3: Sprite) {
    sprite3.destroy()
    otherSprite3.destroy(effects.disintegrate)
    info.changeScoreBy(3)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function on_on_overlap4(sprite4: Sprite, otherSprite4: Sprite) {
    sprite4.destroy()
    otherSprite4.destroy(effects.disintegrate)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap5(sprite5: Sprite, otherSprite5: Sprite) {
    scene.cameraShake(4, 500)
    otherSprite5.destroy(effects.disintegrate)
    sprite5.startEffect(effects.fire, 200)
    info.changeLifeBy(-1)
})
let projectile : Sprite = null
let ship : Sprite = null
let asteroids = [img`
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . f f f f f f f f . . . . . 
            . . . f f f f f f f f . . . . . 
            . . . f f 1 f f 1 f f . . . . . 
            . . . f f f f f f f f . . . . . 
            . . . f f f f f f f f . . . . . 
            . . . 1 f 1 f 1 f 1 f . . . . . 
            . . . f 1 f 1 f 1 f 1 . . . . . 
            . . . f f f f f f f f . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    `, img`
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . 1 1 1 1 1 1 1 1 1 . . . . . 
            . . 1 1 1 1 1 1 1 1 1 . . . . . 
            . . 1 1 f 1 1 1 f 1 1 . . . . . 
            . . 1 1 1 1 1 1 1 1 1 . . . . . 
            . . 1 1 1 1 1 1 1 1 1 . . . . . 
            . . 1 f 1 1 1 1 1 f 1 . . . . . 
            . . 1 f f f f f f f 1 . . . . . 
            . . 1 1 1 1 1 1 1 1 1 . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    `]
ship = sprites.create(img`
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . f f f f f f f f f f . . . . . 
            . f f f f f f f f f f . . . . . 
            . f f 1 f f f f 1 f f . . . . . 
            . f f f f f f f f f f . . . . . 
            . f f f f f f f f f f . . . . . 
            . f f f f f f f f f f . . . . . 
            . f 1 f f f f f f 1 f . . . . . 
            . f f 1 1 1 1 1 1 f f . . . . . 
            . f f f f f f f f f f . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    `, SpriteKind.Player)
let boss2 = [img`
    . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . 5 . 5 . 5 . 5 . 5 . . . . 
        . . . 5 2 5 7 5 4 5 8 5 . . . . 
        . . . 1 1 1 1 1 1 1 1 1 . . . . 
        . . . 1 1 1 1 1 1 1 1 1 . . . . 
        . . . 1 1 f 1 1 1 f 1 1 . . . . 
        . . . 1 1 1 1 1 1 1 1 1 . . . . 
        . . . 1 1 1 1 1 1 1 1 1 . . . . 
        . . . 1 f 1 1 1 1 1 f 1 . . . . 
        . . . 1 f f f f f f f 1 . . . . 
        . . . 1 1 1 1 1 1 1 1 1 . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . .
`]
let health = [img`
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . 7 7 7 7 7 7 7 7 . . . . . 
            . . . 7 1 7 7 7 7 1 7 . . . . . 
            . . . 7 7 7 7 7 7 7 7 . . . . . 
            . . . 7 7 7 7 7 7 7 7 . . . . . 
            . . . 1 1 7 7 7 7 7 7 . . . . . 
            . . . 7 7 1 1 1 1 1 7 . . . . . 
            . . . 7 7 7 7 7 7 7 7 . . . . . 
            . . . 7 7 7 7 7 7 7 7 . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    `, img`
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . 7 7 7 7 7 7 7 7 . . . . . 
            . . . 7 1 7 7 7 7 1 7 . . . . . 
            . . . 7 7 7 7 7 7 7 7 . . . . . 
            . . . 7 7 7 7 7 7 7 7 . . . . . 
            . . . 1 1 7 7 7 7 7 7 . . . . . 
            . . . 7 7 1 1 1 1 1 7 . . . . . 
            . . . 7 7 7 7 7 7 7 7 . . . . . 
            . . . 7 7 7 7 7 7 7 7 . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    `]
ship.setStayInScreen(true)
ship.bottom = 120
controller.moveSprite(ship, 100, 100)
info.setLife(3)
effects.starField.startScreenEffect(100)
music.playMelody("C D D E G F E D ", 90)
music.playMelody("C D - - - - - - ", 90)
game.onUpdateInterval(5000, function on_update_interval() {
    
    projectile = sprites.createProjectileFromSide(boss2[randint(0, boss2.length - 1)], 0, 75)
    projectile.setKind(SpriteKind.boss)
    projectile.x = randint(10, 150)
    boss2 = [img`
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . 5 . 5 . 5 . 5 . 5 . . . . 
                . . . 5 2 5 7 5 4 5 8 5 . . . . 
                . . . 1 1 1 1 1 1 1 1 1 . . . . 
                . . . 1 1 1 1 1 1 1 1 1 . . . . 
                . . . 1 1 f 1 1 1 f 1 1 . . . . 
                . . . 1 1 1 1 1 1 1 1 1 . . . . 
                . . . 1 1 1 1 1 1 1 1 1 . . . . 
                . . . 1 f 1 1 1 1 1 f 1 . . . . 
                . . . 1 f f f f f f f 1 . . . . 
                . . . 1 1 1 1 1 1 1 1 1 . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    `]
})
game.onUpdateInterval(2000, function on_update_interval2() {
    
    projectile = sprites.createProjectileFromSide(health[randint(0, asteroids.length - 1)], 0, 75)
    projectile.setKind(SpriteKind.Food)
    projectile.x = randint(10, 150)
})
game.onUpdateInterval(500, function on_update_interval3() {
    
    projectile = sprites.createProjectileFromSide(asteroids[randint(0, asteroids.length - 1)], 0, 75)
    projectile.setKind(SpriteKind.Enemy)
    projectile.x = randint(10, 150)
})
