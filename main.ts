function play_uk_anthem () {
    melody = "G3:2 G3:2 A3:2 F#3:2 G3:2 A3:2 B3:4 " + "B3:2 C4:2 A3:2 B3:2 C4:2 D4:4 " + "D4:2 D4:2 C4:2 A3:2 B3:2 A3:2 G3:4 " + "A3:2 F#3:2 G3:2 A3:2 F#3:2 G3:4"
    music.play(music.stringPlayable(melody, 120), music.PlaybackMode.UntilDone)
}
input.onButtonPressed(Button.A, function () {
    play_uk_anthem()
})
function play_lion_king_theme () {
    // Create a simple original melody inspired by themes from the movie
    melody3 = "C4:4 G4:4 A4:4 F4:4 G4:8 ..."
    music.play(music.stringPlayable(melody3, 120), music.PlaybackMode.UntilDone)
}
input.onButtonPressed(Button.AB, function () {
    play_extended_original_theme()
})
input.onButtonPressed(Button.B, function () {
    play_chinese_anthem()
})
function play_chinese_anthem () {
    melody2 = "E4:2 E4:2 G4:2 G4:2 A4:2 A4:2 C5:4 " + "A4:2 C5:2 E5:2 D5:2 C5:2 A4:4 " + "G4:2 A4:2 C5:2 A4:2 G4:2 E4:4 " + "D4:2 D4:2 E4:2 G4:2 A4:2 A4:2 G4:4 " + "E4:2 E4:2 G4:2 G4:2 A4:2 A4:2 C5:4 " + "A4:2 C5:2 E5:2 D5:2 C5:2 A4:4 " + "G4:2 A4:2 C5:2 A4:2 G4:2 E4:4 " + "D4:2 D4:2 E4:2 G4:2 A4:2 A4:2 G4:4 " + "C5:2 C5:2 C5:2 C5:2 C5:2 A4:2 C5:4 " + "E5:2 E5:2 E5:2 E5:2 E5:2 C5:2 E5:4 " + "G5:2 G5:2 E5:2 C5:2 E5:2 D5:2 C5:4 " + "C5:2 A4:2 G4:2 E4:2 D4:2 C4:2 D4:4 " + "E4:2 E4:2 G4:2 G4:2 A4:2 A4:2 C5:4 " + "A4:2 C5:2 E5:2 D5:2 C5:2 A4:4 " + "G4:2 A4:2 C5:2 A4:2 G4:2 E4:4 " + "D4:2 D4:2 E4:2 G4:2 A4:2 A4:2 G4:4"
    music.play(music.stringPlayable(melody2, 120), music.PlaybackMode.UntilDone)
}
function play_extended_original_theme () {
    edubitRgbBit.showRainbow()
    melody4 = "C4:4 E4:4 G4:4 F4:4 A4:8 G4:4 E4:4 C4:8 " + "D4:4 F4:4 A4:4 G4:4 B4:8 A4:4 F4:4 D4:8 " + "E4:4 G4:4 C5:4 B4:4 D5:8 C5:4 G4:4 E4:8 " + "C4:4 E4:4 G4:4 F4:4 A4:8 G4:4 E4:4 C4:8 " + "E4:4 G4:4 C5:4 A4:4 C5:8 B4:4 G4:4 E4:8 " + "F4:4 A4:4 C5:4 B4:4 D5:8 C5:4 A4:4 F4:8 " + "G4:4 B4:4 D5:4 C5:4 E5:8 D5:4 B4:4 G4:8 " + "E4:4 G4:4 C5:4 A4:4 C5:8 B4:4 G4:4 E4:8 " + "A3:4 C4:4 E4:4 D4:4 F4:8 E4:4 C4:4 A3:8 " + "B3:4 D4:4 F4:4 E4:4 G4:8 F4:4 D4:4 B3:8 " + "C4:4 E4:4 G4:4 F4:4 A4:8 G4:4 E4:4 C4:8 " + "A3:4 C4:4 E4:4 D4:4 F4:8 E4:4 C4:4 A3:8 " + "C4:2 E4:2 G4:2 F4:2 A4:4 G4:2 E4:2 C4:4 " + "D4:2 F4:2 A4:2 G4:2 B4:4 A4:2 F4:2 D4:4 " + "E4:2 G4:2 C5:2 B4:2 D5:4 C5:2 G4:2 E4:4 " + "C4:2 E4:2 G4:2 F4:2 A4:4 G4:2 E4:2 C4:4 " + "C4:4 E4:4 G4:4 C5:4 E5:8 D5:4 B4:4 G4:8 " + "A4:4 C5:4 E5:4 D5:4 F5:8 E5:4 C5:4 A4:8 " + "G4:4 B4:4 D5:4 C5:4 E5:8 D5:4 B4:4 G4:8 " + "C5:4 G4:4 E4:4 C4:4 G4:8 E4:4 C4:4 C4:8"
    // Part 1: Original theme
    // Part 2: Variation with higher notes
    // Part 3: Lower register variation
    // Part 4: Rhythmic variation
    // Part 5: Grand finale
    music.play(music.stringPlayable(melody4, 80), music.PlaybackMode.UntilDone)
}
let melody4 = ""
let melody2 = ""
let melody3 = ""
let melody = ""
// Set the volume
music.setVolume(127)
basic.forever(function () {
	
})
