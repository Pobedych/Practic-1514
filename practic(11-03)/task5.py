import wave

def chip_and_dale(i):
    inp = wave.open("in.wav", "rb")
    out = wave.open("out5.wav", "wb")

    out.setparams(inp.getparams())

    frames = inp.readframes(inp.getnframes())
    frame_size = inp.getsampwidth() * inp.getnchannels()

    result = b""
    for j in range(0, len(frames), frame_size * i):
        result += frames[j:j + frame_size]

    out.writeframes(result)

    inp.close()
    out.close()