_25 = 0

def on_button_pressed_a():
    global _25
    basic.show_number(9)
    music.play(music.string_playable("C5 B C5 A E D G C ", 500),
        music.PlaybackMode.UNTIL_DONE)
    _25 = 0
input.on_button_pressed(Button.A, on_button_pressed_a)
