# nk2-osc

This is a simple script to control `non-mixer` using a nanoKONTROL2, which basically serves as a bridge between MIDI and OSC.

## Usage

Make sure you have running `non-mixer`, and know which OSC port is listening (you can define one by `non-mixer --osc-port=...`).  
Edit `mapping.py` to match a CC channel and your "strip". 

```
$ python3 nk2-osc.py --ip 127.0.0.1 --port 12345
```

There's a `mapping.py` example available in the repository which presents a working example (which I use to set the 3 "main" programs I use).

## Useful info

[non-mixer Manual](http://non.tuxfamily.org/mixer/doc/MANUAL.html)

## Dependencies

* https://pypi.org/project/python-osc/
* https://pypi.org/project/python-rtmidi/


## License

```
        DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
                    Version 2, December 2004 

 Copyright (C) 2018 Mauro L. <mauro@sdf.org> 

 Everyone is permitted to copy and distribute verbatim or modified 
 copies of this license document, and changing it is allowed as long 
 as the name is changed. 

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 

  0. You just DO WHAT THE FUCK YOU WANT TO.
```
