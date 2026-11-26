# Piano Scale Chord Progression Generator
# Belajar chord dasar tiap key

major_scales = {
    "C":  ["C", "Dm", "Em", "F", "G", "Am", "Bdim"],

    "C#": ["C#", "D#m", "Fm", "F#", "G#", "A#m", "B#dim"],
    "Db": ["Db", "Ebm", "Fm", "Gb", "Ab", "Bbm", "Cdim"],

    "D":  ["D", "Em", "F#m", "G", "A", "Bm", "C#dim"],

    "D#": ["D#", "Fm", "Gm", "G#", "A#", "Cm", "Ddim"],
    "Eb": ["Eb", "Fm", "Gm", "Ab", "Bb", "Cm", "Ddim"],

    "E":  ["E", "F#m", "G#m", "A", "B", "C#m", "D#dim"],

    "F":  ["F", "Gm", "Am", "Bb", "C", "Dm", "Edim"],

    "F#": ["F#", "G#m", "A#m", "B", "C#", "D#m", "E#dim"],
    "Gb": ["Gb", "Abm", "Bbm", "Cb", "Db", "Ebm", "Fdim"],

    "G":  ["G", "Am", "Bm", "C", "D", "Em", "F#dim"],

    "G#": ["G#", "A#m", "Cm", "C#", "D#", "Fm", "Gdim"],
    "Ab": ["Ab", "Bbm", "Cm", "Db", "Eb", "Fm", "Gdim"],

    "A":  ["A", "Bm", "C#m", "D", "E", "F#m", "G#dim"],

    "A#": ["A#", "Cm", "Dm", "D#", "F", "Gm", "Adim"],
    "Bb": ["Bb", "Cm", "Dm", "Eb", "F", "Gm", "Adim"],

    "B":  ["B", "C#m", "D#m", "E", "F#", "G#m", "A#dim"],
    "Cb": ["Cb", "Dbm", "Ebm", "Fb", "Gb", "Abm", "Bbdim"],
}

print("=== Piano Chord Major Scale Trainer  ===")

while True:


    print("\nHello User !!!")
    print("\nPlease Choose Available Key:")
    print(", ".join(major_scales.keys()))

    key = input("\nInput key (atau exit): ").capitalize()

    if key.lower() == "exit":
        print("Bye!")
        break

    if key in major_scales:

        chords = major_scales[key]

        print(f"\nChord dalam key {key} Major:\n")

        print("I    =", chords[0])
        print("ii   =", chords[1])
        print("iii  =", chords[2])
        print("IV   =", chords[3])
        print("V    =", chords[4])
        print("vi   =", chords[5])
        print("vii° =", chords[6])

        print(f"\n Major Progression Chord {key} :")
        print(" - ".join(chords))
        print("\n======================")

    else:
        print("Key tidak ditemukan")