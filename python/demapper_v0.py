#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2020 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy as np
from gnuradio import gr

class demapper_v0(gr.sync_block):
    """
    QPSK demmaper
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="demapper_v0",
            in_sig=[np.complex64],
            out_sig=[np.uint32])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        distances = np.zeros(4, dtype=np.float32)
        for i in range(len(in0)):
            for s in range(4):  # QPSK
                if s == 0:
                    symbol = np.complex64(+1+1j)
                elif s == 1:
                    symbol = np.complex64(-1+1j)
                elif s == 2:
                    symbol = np.complex64(+1-1j)
                elif s == 3:
                    symbol = np.complex64(-1-1j)
                else:
                    pass
                distances[s] = (np.real(in0[i]) - np.real(symbol))**2 + (np.imag(in0[i]) - np.imag(symbol))**2
            out[i] = np.argmin(distances)
        return len(output_items[0])

