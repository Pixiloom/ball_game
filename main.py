@namespace
class SpriteKind:
    boss = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    scene.camera_shake(4, 500)
    otherSprite.destroy(effects.disintegrate)
    sprite.start_effect(effects.fire, 200)
    info.change_life_by(-3)
sprites.on_overlap(SpriteKind.player, SpriteKind.boss, on_on_overlap)

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . . . . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . . 
                    . . . 1 1 . . .
        """),
        ship,
        0,
        -140)
    projectile.start_effect(effects.cool_radial, 100)
    music.big_crash.play()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap2(sprite2, otherSprite2):
    info.change_life_by(1)
    sprite2.destroy()
    music.ba_ding.play()
sprites.on_overlap(SpriteKind.food, SpriteKind.player, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    sprite3.destroy()
    otherSprite3.destroy(effects.disintegrate)
    info.change_score_by(3)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.boss, on_on_overlap3)

def on_on_overlap4(sprite4, otherSprite4):
    sprite4.destroy()
    otherSprite4.destroy(effects.disintegrate)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap4)

def on_on_overlap5(sprite5, otherSprite5):
    scene.camera_shake(4, 500)
    otherSprite5.destroy(effects.disintegrate)
    sprite5.start_effect(effects.fire, 200)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap5)

projectile: Sprite = None
ship: Sprite = None
asteroids = [img("""
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
    """),
    img("""
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
    """)]
ship = sprites.create(img("""
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
    """),
    SpriteKind.player)
boss2 = [img("""
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
""")]
health = [img("""
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
    """),
    img("""
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
    """)]
ship.set_stay_in_screen(True)
ship.bottom = 120
controller.move_sprite(ship, 100, 100)
info.set_life(3)
effects.star_field.start_screen_effect(100)
music.play_melody("C D D E G F E D ", 90)
music.play_melody("C D - - - - - - ", 90)

def on_update_interval():
    global projectile, boss2
    projectile = sprites.create_projectile_from_side(boss2[randint(0, len(boss2) - 1)], 0, 75)
    projectile.set_kind(SpriteKind.boss)
    projectile.x = randint(10, 150)
    boss2 = [img("""
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
    """)]
game.on_update_interval(5000, on_update_interval)

def on_update_interval2():
    global projectile
    projectile = sprites.create_projectile_from_side(health[randint(0, len(asteroids) - 1)], 0, 75)
    projectile.set_kind(SpriteKind.food)
    projectile.x = randint(10, 150)
game.on_update_interval(2000, on_update_interval2)

def on_update_interval3():
    global projectile
    projectile = sprites.create_projectile_from_side(asteroids[randint(0, len(asteroids) - 1)], 0, 75)
    projectile.set_kind(SpriteKind.enemy)
    projectile.x = randint(10, 150)
game.on_update_interval(500, on_update_interval3)
