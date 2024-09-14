def on_on_chat():
    gameplay.set_difficulty(PEACEFUL)
player.on_chat("Peace", on_on_chat)

mobs.spawn(CHICKEN, pos(2, 3, 7))