#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
# author    : "javier pérez santos para orangepiweb.es"
# credits   : "javier pérez santos, orangepiweb.es"
# copyright : "Copyright 2017, orangepiweb.es"

"""
   ___                             ____  ___        __   _
  / _ \ _ __ __ _ _ __   __ _  ___|  _ \(_) \      / /__| |__   ___  ___
 | | | | '__/ _` | '_ \ / _` |/ _ \ |_) | |\ \ /\ / / _ \ '_ \ / _ \/ __|
 | |_| | | | (_| | | | | (_| |  __/  __/| | \ V  V /  __/ |_) |  __/\__ \
  \___/|_|  \__,_|_| |_|\__, |\___|_|   |_|  \_/\_/ \___|_.__(_)___||___/
                        |___/

Controlando GPIO con Python
"""

import os
import sys

from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port

rele = port.PA1
led0 = port.PA12
led1 = port.PA11
led2 = port.PA6

gpio.init()
gpio.setcfg(rele, gpio.INPUT)
gpio.setcfg(led0, gpio.OUTPUT)
gpio.setcfg(led1, gpio.OUTPUT)
gpio.setcfg(led2, gpio.OUTPUT)

try:
    print ("Pulsa CTRL+C para salir")
    while True:
        if gpio.input(port.PA1) == 0:
                gpio.output(led0, 1)
                sleep(0.1)
                gpio.output(led0, 0)
                #sleep(0.1)

                gpio.output(led1, 1)
                sleep(0.1)
                gpio.output(led1, 0)
                #sleep(0.1)

                gpio.output(led2, 1)
                sleep(0.1)
                gpio.output(led2, 0)
                #sleep(0.1)

                sleep(0.6)
except KeyboardInterrupt:
    print ("Saliendo")
