# 2nd comment
mySprite = sprites.create(assets.image("""
    myDuckImage
    """), SpriteKind.player)
controller.move_sprite(mySprite)
tiles.set_current_tilemap(tilemap("""
    level1
    """))