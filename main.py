def play_uk_anthem():
    global melody
    melody = "G3:2 G3:2 A3:2 F#3:2 G3:2 A3:2 B3:4 " + "B3:2 C4:2 A3:2 B3:2 C4:2 D4:4 " + "D4:2 D4:2 C4:2 A3:2 B3:2 A3:2 G3:4 " + "A3:2 F#3:2 G3:2 A3:2 F#3:2 G3:4"
    music.play(music.string_playable(melody, 120),
        music.PlaybackMode.UNTIL_DONE)

def on_button_pressed_a():
    play_uk_anthem()
input.on_button_pressed(Button.A, on_button_pressed_a)

def play_lion_king_theme():
    global melody3
    # Create a simple original melody inspired by themes from the movie
    melody3 = "C4:4 G4:4 A4:4 F4:4 G4:8 ..."
    music.play(music.string_playable(melody3, 120),
        music.PlaybackMode.UNTIL_DONE)

def on_button_pressed_b():
    play_chinese_anthem()
input.on_button_pressed(Button.B, on_button_pressed_b)

def play_chinese_anthem():
    global melody2
    melody2 = "E4:2 E4:2 G4:2 G4:2 A4:2 A4:2 C5:4 " + "A4:2 C5:2 E5:2 D5:2 C5:2 A4:4 " + "G4:2 A4:2 C5:2 A4:2 G4:2 E4:4 " + "D4:2 D4:2 E4:2 G4:2 A4:2 A4:2 G4:4 " + "E4:2 E4:2 G4:2 G4:2 A4:2 A4:2 C5:4 " + "A4:2 C5:2 E5:2 D5:2 C5:2 A4:4 " + "G4:2 A4:2 C5:2 A4:2 G4:2 E4:4 " + "D4:2 D4:2 E4:2 G4:2 A4:2 A4:2 G4:4 " + "C5:2 C5:2 C5:2 C5:2 C5:2 A4:2 C5:4 " + "E5:2 E5:2 E5:2 E5:2 E5:2 C5:2 E5:4 " + "G5:2 G5:2 E5:2 C5:2 E5:2 D5:2 C5:4 " + "C5:2 A4:2 G4:2 E4:2 D4:2 C4:2 D4:4 " + "E4:2 E4:2 G4:2 G4:2 A4:2 A4:2 C5:4 " + "A4:2 C5:2 E5:2 D5:2 C5:2 A4:4 " + "G4:2 A4:2 C5:2 A4:2 G4:2 E4:4 " + "D4:2 D4:2 E4:2 G4:2 A4:2 A4:2 G4:4"
    music.play(music.string_playable(melody2, 120),
        music.PlaybackMode.UNTIL_DONE)
melody2 = ""
melody3 = ""
melody = ""
# Set the volume
music.set_volume(127)

def on_forever():
    pass
basic.forever(on_forever)

def play_extended_original_theme():
    melody = (
        # Part 1: Original theme
        "C4:4 E4:4 G4:4 F4:4 A4:8 G4:4 E4:4 C4:8 " +
        "D4:4 F4:4 A4:4 G4:4 B4:8 A4:4 F4:4 D4:8 " +
        "E4:4 G4:4 C5:4 B4:4 D5:8 C5:4 G4:4 E4:8 " +
        "C4:4 E4:4 G4:4 F4:4 A4:8 G4:4 E4:4 C4:8 " +

        # Part 2: Variation with higher notes
        "E4:4 G4:4 C5:4 A4:4 C5:8 B4:4 G4:4 E4:8 " +
        "F4:4 A4:4 C5:4 B4:4 D5:8 C5:4 A4:4 F4:8 " +
        "G4:4 B4:4 D5:4 C5:4 E5:8 D5:4 B4:4 G4:8 " +
        "E4:4 G4:4 C5:4 A4:4 C5:8 B4:4 G4:4 E4:8 " +

        # Part 3: Lower register variation
        "A3:4 C4:4 E4:4 D4:4 F4:8 E4:4 C4:4 A3:8 " +
        "B3:4 D4:4 F4:4 E4:4 G4:8 F4:4 D4:4 B3:8 " +
        "C4:4 E4:4 G4:4 F4:4 A4:8 G4:4 E4:4 C4:8 " +
        "A3:4 C4:4 E4:4 D4:4 F4:8 E4:4 C4:4 A3:8 " +

        # Part 4: Rhythmic variation
        "C4:2 E4:2 G4:2 F4:2 A4:4 G4:2 E4:2 C4:4 " +
        "D4:2 F4:2 A4:2 G4:2 B4:4 A4:2 F4:2 D4:4 " +
        "E4:2 G4:2 C5:2 B4:2 D5:4 C5:2 G4:2 E4:4 " +
        "C4:2 E4:2 G4:2 F4:2 A4:4 G4:2 E4:2 C4:4 " +

        # Part 5: Grand finale
        "C4:4 E4:4 G4:4 C5:4 E5:8 D5:4 B4:4 G4:8 " +
        "A4:4 C5:4 E5:4 D5:4 F5:8 E5:4 C5:4 A4:8 " +
        "G4:4 B4:4 D5:4 C5:4 E5:8 D5:4 B4:4 G4:8 " +
        "C5:4 G4:4 E4:4 C4:4 G4:8 E4:4 C4:4 C4:8"
    )
    
    music.play(music.string_playable(melody, 80), music.PlaybackMode.UNTIL_DONE)

def on_button_pressed_ab():
    play_extended_original_theme()

input.on_button_pressed(Button.AB, on_button_pressed_ab)