import os
import phony.headset
import phony.base.ipc
import phony.audio.alsa
import phony.bluetooth.adapters
import phony.bluetooth.profiles.handsfree
from phony.base import log
from phony.base.log import ClassLogger, ScopedLogger

interface="hci0"
audio_card_index=3
session_bus_path = os.environ.get('DBUS_SESSION_BUS_ADDRESS')
bus = phony.base.ipc.BusProvider(session_bus_path)

with phony.base.ipc.OwnedSocketFile(bus, socket_file) as socket, \
     phony.bluetooth.adapters.Bluez5(bus, interface) as adapter, \
     phony.bluetooth.profiles.handsfree.Ofono(bus) as hfp, \
     phony.audio.alsa.Alsa(audio_card_index) as audio, \
     phony.headset.HandsFreeHeadset(bus, adapter, hfp, audio) as hs:
    
    pass
