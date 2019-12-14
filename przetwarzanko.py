#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def sumuj_lata():
    if not input(os.getcwd()+"\\Dane\n\nJesteś pewien że podany katalog jest właściwy? T/N\n").lower().startswith("t"):
        return
    # skrypt sumujący zawartość każdego folderu