from TTS.api import TTS

tts = TTS("tts_models/en/vctk/vits")

tts.tts_to_file(
    text="This is a male voice sample from VCTK.",
    speaker="p376",
    #speaker="p233", p229   # male speaker
    file_path="male376.wav"
)

#tts = TTS("tts_models/en/libritts/tacotron2-DDC")
#tts.tts_to_file(text="Hello!This is a male voice sample", speaker="male", file_path="out.wav")
