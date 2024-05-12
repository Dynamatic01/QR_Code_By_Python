# -*- coding: utf-8 -*-
"""
Created on Mon May  6 22:45:41 2024

@author: mehta
"""
import qrcode as qr
 
img=qr.make("https://indiahub.online/")

img.save("IndiaHub_Online.png")