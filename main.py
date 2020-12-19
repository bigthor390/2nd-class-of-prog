def on_up_pressed():
    Carro.set_image(img("""
        . . . . . . e e c c e e . . . . 
                . . . . . e 2 2 2 2 2 2 e . . . 
                . . . . 2 c 2 2 2 2 2 2 c 2 . . 
                . . . e 2 c 4 2 2 2 2 2 c 2 e . 
                . . . f 2 2 4 2 2 2 2 2 c 2 f . 
                . . . f 2 2 4 2 2 2 2 2 2 2 f . 
                . . . f 2 2 4 2 2 2 2 2 2 2 f . 
                . . . f 2 c 2 4 4 2 2 2 c 2 f . 
                . . . e 2 c e c c c c e c 2 e . 
                . . . e 2 e c b b b b c e 2 e . 
                . . . e 2 e b b b b b b e 2 e . 
                . . . e e e e e e e e e e e e . 
                . . . f e d e e e e e e d e f . 
                . . . f e 2 d e e e e d 2 e f . 
                . . . f f e e e e e e e e f f . 
                . . . . f f . . . . . . f f . .
    """))
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_left_pressed():
    Carro.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . 2 2 2 2 2 2 2 2 . . 
                . . . . . 2 c 2 2 2 2 2 2 4 2 . 
                . . . . 2 c c 2 2 2 2 2 2 4 c 2 
                . . d 2 4 c c 2 4 4 4 4 4 4 c c 
                . d 2 2 4 c b e e e e e e e 2 c 
                . 2 2 2 4 b e e b b b e b b e 2 
                . 2 2 2 2 2 e b b b b e b b b e 
                . 2 2 2 2 e 2 2 2 2 2 e 2 2 2 e 
                . 2 d d 2 e f e e e f e e e e e 
                . d d 2 e e e f e e f e e e e e 
                . e e e e e e e f f f e e e e e 
                . e e e e f f f e e e e f f f f 
                . . . e f f f f f e e f f f f f 
                . . . . f f f f . . . . f f f . 
                . . . . . . . . . . . . . . . .
    """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    Carro.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . 2 2 2 2 2 2 2 2 . . . . 
                . . . 2 4 2 2 2 2 2 2 c 2 . . . 
                . . 2 c 4 2 2 2 2 2 2 c c 2 . . 
                . 2 c c 4 4 4 4 4 4 2 c c 4 2 d 
                . 2 c 2 e e e e e e e b c 4 2 2 
                . 2 2 e b b e b b b e e b 4 2 2 
                . 2 e b b b e b b b b e 2 2 2 2 
                . e e 2 2 2 e 2 2 2 2 2 e 2 2 2 
                . e e e e e e f e e e f e 2 d d 
                . e e e e e e f e e f e e e 2 d 
                . e e e e e e f f f e e e e e e 
                . e f f f f e e e e f f f e e e 
                . . f f f f f e e f f f f f e . 
                . . . f f f . . . . f f f f . . 
                . . . . . . . . . . . . . . . .
    """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    Carro.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . 2 2 2 2 2 2 . . . . 
                . . . . . 2 2 4 4 2 2 2 2 . . . 
                . . . . . c 4 2 2 2 2 2 c . . . 
                . . . . 2 c 4 2 2 2 2 2 c 2 . . 
                . . . e 2 c 4 2 2 2 2 2 c 2 e . 
                . . . f 2 c 4 2 2 2 2 2 c 2 f . 
                . . . f e c 2 2 2 2 2 2 c e f . 
                . . . f 2 c 2 b b b b 2 c 2 f . 
                . . . e 2 2 b c c c c b 2 2 e . 
                . . . e e b c c c c c c b e e . 
                . . . f e 4 4 4 4 4 4 4 4 e f . 
                . . . f e d 2 2 2 2 2 2 d e f . 
                . . . . 2 d d 2 2 2 2 d d 2 f . 
                . . . . f 2 d 2 2 2 2 d 2 f . . 
                . . . . . e 2 2 2 2 2 2 e . . .
    """))
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

Carro: Sprite = None
Carro = sprites.create(img("""
        . . . . . . e e c c e e . . . . 
            . . . . . e 2 2 2 2 2 2 e . . . 
            . . . . 2 c 2 2 2 2 2 2 c 2 . . 
            . . . e 2 c 4 2 2 2 2 2 c 2 e . 
            . . . f 2 2 4 2 2 2 2 2 c 2 f . 
            . . . f 2 2 4 2 2 2 2 2 2 2 f . 
            . . . f 2 2 4 2 2 2 2 2 2 2 f . 
            . . . f 2 c 2 4 4 2 2 2 c 2 f . 
            . . . e 2 c e c c c c e c 2 e . 
            . . . e 2 e c b b b b c e 2 e . 
            . . . e 2 e b b b b b b e 2 e . 
            . . . e e e e e e e e e e e e . 
            . . . f e d e e e e e e d e f . 
            . . . f e 2 d e e e e d 2 e f . 
            . . . f f e e e e e e e e f f . 
            . . . . f f . . . . . . f f . .
    """),
    SpriteKind.player)
controller.move_sprite(Carro, 100, 100)
tiles.set_tilemap(tiles.create_tilemap(hex("""
            15001500010101010101010101010101010101010101010101010202020202010202020202020202020201020204010202020202010202020202020202020201020204010202010202010202010101010101020201020201010202010202010202010101010101020201020201010202010202010202010101010101020201020201010202010202010202010202020202020201020201010202010202010202010202020202020201020201010202010202010202010202020202020201020201010202010202010202010202020202020201020201010202010202010202010202010101020201020201010202010202010202010202010101020202020201010202010202010202010202020201020202020201010202010202010202010202020201010101010101010202010202010202010101010101020202020201010202010202010202020202020202020202020201010202010202010202020202020202020201020201010202010202010101010101010101010101020201010202010202020202020202020202020202020201010202010202020202020202020202020202020201010303010101010101010101010101010101010101
        """),
        img("""
            222222222222222222222
                2.....2..........2...
                2.....2..........2...
                2..2..2..222222..2..2
                2..2..2..222222..2..2
                2..2..2..222222..2..2
                2..2..2..2.......2..2
                2..2..2..2.......2..2
                2..2..2..2.......2..2
                2..2..2..2.......2..2
                2..2..2..2..222..2..2
                2..2..2..2..222.....2
                2..2..2..2....2.....2
                2..2..2..2....2222222
                2..2..2..222222.....2
                2..2..2.............2
                2..2..2..........2..2
                2..2..222222222222..2
                2..2................2
                2..2................2
                2..222222222222222222
        """),
        [myTiles.transparency16,
            sprites.dungeon.floor_light0,
            sprites.castle.tile_grass1,
            sprites.castle.tile_path2,
            sprites.castle.tile_path4],
        TileScale.SIXTEEN))
scene.camera_follow_sprite(Carro)