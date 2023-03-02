# left

def on_button_pressed_a():
    player.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

# right

def on_button_pressed_b():
    player.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

# game setup
enemy_5: game.LedSprite = None
enemy_4: game.LedSprite = None
score = 0
player: game.LedSprite = None
time = 0
player = game.create_sprite(2, 2)
enemy = game.create_sprite(Math.round(randint(1, 5)), 5)
enemy_2 = game.create_sprite(Math.round(randint(1, 5)), 5)
enemy_3 = game.create_sprite(Math.round(randint(1, 5)), 5)
# score

def on_forever():
    global score
    basic.pause(1000)
    score += 1
basic.forever(on_forever)

# game over

def on_forever2():
    if enemy.is_touching(player):
        game.game_over()
        basic.show_number(score)
    if enemy_2.is_touching(player):
        game.game_over()
        basic.show_number(score)
    if enemy_3.is_touching(player):
        game.game_over()
        basic.show_number(score)
    if enemy_4.is_touching(player):
        game.game_over()
        basic.show_number(score)
    if enemy_5.is_touching(player):
        game.game_over()
        basic.show_number(score)
basic.forever(on_forever2)

# timer

def on_forever3():
    global time
    basic.pause(100)
    time += 1
basic.forever(on_forever3)

# enemy logic

def on_forever4():
    enemy.change(LedSpriteProperty.Y, -1)
    enemy_2.change(LedSpriteProperty.Y, -1)
    enemy_3.change(LedSpriteProperty.Y, -1)
    enemy_4.change(LedSpriteProperty.Y, -1)
    player.change(LedSpriteProperty.Y, -1)
    basic.pause(500)
basic.forever(on_forever4)

# enemy respawn

def on_forever5():
    global enemy
    basic.pause(3000 - time)
    enemy.delete()
    enemy = game.create_sprite(Math.round(randint(1, 5)), 5)
basic.forever(on_forever5)

# enemy 2 respawn

def on_forever6():
    global enemy_2
    basic.pause(3000)
    enemy_2.delete()
    basic.pause(randint(3000, 4500) - time)
    enemy_2 = game.create_sprite(Math.round(randint(1, 5)), 5)
basic.forever(on_forever6)

# enemy 3 respawn

def on_forever7():
    global enemy_3
    basic.pause(3000)
    enemy_3.delete()
    basic.pause(randint(3000, 4500) - time)
    enemy_3 = game.create_sprite(Math.round(randint(1, 5)), 5)
basic.forever(on_forever7)

# enemy 4 respawn

def on_forever8():
    global enemy_4
    basic.pause(3000)
    enemy_4.delete()
    basic.pause(randint(3000, 4500) - time)
    enemy_4 = game.create_sprite(Math.round(randint(1, 5)), 5)
basic.forever(on_forever8)

# enemy 5 respawn

def on_forever9():
    global enemy_5
    basic.pause(3000)
    enemy_5.delete()
    basic.pause(randint(3000, 4500) - time)
    enemy_5 = game.create_sprite(Math.round(randint(1, 5)), 5)
basic.forever(on_forever9)
