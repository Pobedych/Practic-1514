import wave


def pitch_and_toss():
    with wave.open("in7.wav", "rb") as source:
        params = source.getparams()
        frame_count = source.getnframes()
        frames = source.readframes(frame_count)

    frame_size = params.nchannels * params.sampwidth
    part_size = frame_count // 4

    first = frames[0:part_size * frame_size]
    second = frames[part_size * frame_size:part_size * 2 * frame_size]
    third = frames[part_size * 2 * frame_size:part_size * 3 * frame_size]
    fourth = frames[part_size * 3 * frame_size:]

    with wave.open("out7.wav", "wb") as result:
        result.setparams(params)
        result.writeframes(third + fourth + first + second)


pitch_and_toss()
