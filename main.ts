// right
input.onButtonPressed(Button.A, function () {
    player.change(LedSpriteProperty.X, -1)
})
// right
input.onButtonPressed(Button.B, function () {
    player.change(LedSpriteProperty.X, 1)
})
// game setup
let score = 0
let player: game.LedSprite = null
let time = 0
player = game.createSprite(2, 0)
let enemy = game.createSprite(Math.round(randint(1, 5)), 5)
let enemy_2 = game.createSprite(Math.round(randint(1, 5)), 5)
let enemy_3 = game.createSprite(Math.round(randint(1, 5)), 5)
let enemy_4 = game.createSprite(Math.round(randint(1, 5)), 5)
let enemy_5 = game.createSprite(Math.round(randint(1, 5)), 5)
// score
basic.forever(function () {
    basic.pause(1000)
    score += 1
})
// game over
basic.forever(function () {
    if (enemy.isTouching(player)) {
        game.gameOver()
        basic.showNumber(score)
    }
    if (enemy_2.isTouching(player)) {
        game.gameOver()
        basic.showNumber(score)
    }
    if (enemy_3.isTouching(player)) {
        game.gameOver()
        basic.showNumber(score)
    }
    if (enemy_4.isTouching(player)) {
        game.gameOver()
        basic.showNumber(score)
    }
    if (enemy_5.isTouching(player)) {
        game.gameOver()
        basic.showNumber(score)
    }
})
// timer
basic.forever(function () {
    basic.pause(100)
    time += 1
})
// enemy logic
basic.forever(function () {
    enemy.change(LedSpriteProperty.Y, -1)
    enemy_2.change(LedSpriteProperty.Y, -1)
    enemy_3.change(LedSpriteProperty.Y, -1)
    enemy_4.change(LedSpriteProperty.Y, -1)
    enemy_5.change(LedSpriteProperty.Y, -1)
    basic.pause(500 - time * 1.5)
})
// enemy respawn
basic.forever(function () {
    basic.pause(3000 - time * 9)
    enemy.delete()
    enemy = game.createSprite(Math.round(randint(1, 5)), 5)
})
// enemy 2 respawn
basic.forever(function () {
    basic.pause(3000)
    enemy_2.delete()
    basic.pause(randint(3000, 4500) - time * 9)
    enemy_2 = game.createSprite(Math.round(randint(1, 5) - 0.5), 5)
})
// enemy 3 respawn
basic.forever(function () {
    basic.pause(3000)
    enemy_3.delete()
    basic.pause(randint(3000, 4500) - time * 9)
    enemy_3 = game.createSprite(Math.round(randint(1, 5)), 5)
})
// enemy 4 respawn
basic.forever(function () {
    basic.pause(3000)
    enemy_4.delete()
    basic.pause(randint(3000, 4500) - time * 9)
    enemy_4 = game.createSprite(Math.round(randint(1, 5)), 5)
})
// enemy 5 respawn
basic.forever(function () {
    basic.pause(3000)
    enemy_5.delete()
    basic.pause(randint(3000, 4500) - time * 9)
    enemy_5 = game.createSprite(Math.round(randint(1, 5)), 5)
})
