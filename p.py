from phony.base.ipc import BusProvider
from phony.audio.pulse import PulseAudio

bus_provider=BusProvider()


with PulseAudio(bus_provider) as audio:
    audio.start()
    print(audio._find_microphone_source())


with PulseAudio(bus_provider) as audio:
    audio.start()
    print(audio._find_primary_audio_sink())
