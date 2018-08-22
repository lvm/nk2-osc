#!/usr/bin/python

import sys
import rtmidi
import argparse

from time import sleep
from pythonosc import osc_message_builder
from pythonosc import udp_client


try:
    import mapping
except ImportError:
    print ("[!] `mapping.py` file is missing!")
    sys.exit(1)


def midi_callback(message, client):
    _, control, value = message[0]

    if control in list(mapping.callbacks.keys()):
        data = mapping.callbacks.get(control)

        print (data.get('name'), value)
        client.send_message(data.get('url'), value / 127.0)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
                      default="127.0.0.1",
                      help="The ip of the OSC server")
  parser.add_argument("--port",
                      type=int,
                      default=12345,
                      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)

  midi_in = rtmidi.MidiIn()
  port = midi_in.open_port(0)
  port.set_callback(midi_callback, client)

  while True:
      sleep(100)
