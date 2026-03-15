import array
import wave


def break_the_silence():
    with wave.open("in6.wav", "rb") as source:
        params = source.getparams()
        frames = source.readframes(source.getnframes())

    if params.sampwidth == 1:
        samples = array.array("B", frames)
        centered_samples = [sample - 128 for sample in samples]
        filtered = array.array("B")

        for i in range(0, len(centered_samples), params.nchannels):
            frame = centered_samples[i:i + params.nchannels]
            if any(abs(sample) > 5 for sample in frame):
                filtered.extend(sample + 128 for sample in frame)
    elif params.sampwidth == 2:
        samples = array.array("h", frames)
        filtered = array.array("h")

        for i in range(0, len(samples), params.nchannels):
            frame = samples[i:i + params.nchannels]
            if any(abs(sample) > 5 for sample in frame):
                filtered.extend(frame)
    else:
        raise ValueError("Only 8-bit and 16-bit wav files are supported")

    with wave.open("out6.wav", "wb") as result:
        result.setparams(params)
        result.writeframes(filtered.tobytes())


break_the_silence()
