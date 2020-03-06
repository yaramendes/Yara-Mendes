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

class mapper_v0(gr.sync_block):
    """
    QPSK mapper implementation using if else structure.
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="mapper_v0",
            in_sig=[np.uint32],
            out_sig=[np.complex64])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        for i in range(len(in0)):
            if in0[i] == 0:
                out[i] = +1+1j
            elif in0[i] == 1:
                out[i] = +1-1j
            elif in0[i] == 2:
                out[i] = -1-1j
            elif in0[i] == 3:
                out[i] = -1+1j
            else:
                pass
        return len(output_items[0])

