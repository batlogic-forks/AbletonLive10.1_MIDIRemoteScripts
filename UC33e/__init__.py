# uncompyle6 version 3.4.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  2 2019, 14:32:10) 
# [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)]
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/UC33e/__init__.py
# Compiled at: 2019-04-09 19:23:45
from __future__ import absolute_import, print_function, unicode_literals
from _Generic.GenericScript import GenericScript
import Live
from .config import *

def create_instance(c_instance):
    u""" The generic script can be customised by using parameters (see config.py). """
    return GenericScript(c_instance, Live.MidiMap.MapMode.absolute, Live.MidiMap.MapMode.absolute, DEVICE_CONTROLS, TRANSPORT_CONTROLS, VOLUME_CONTROLS, TRACKARM_CONTROLS, BANK_CONTROLS, CONTROLLER_DESCRIPTIONS, MIXER_OPTIONS)


from _Framework.Capabilities import *

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=2637, product_ids=[
                         245], model_name='UC-33 USB MIDI Controller'), 
       PORTS_KEY: [
                 inport(props=[NOTES_CC, SCRIPT]),
                 inport(props=[NOTES_CC]),
                 outport(props=[SCRIPT])]}