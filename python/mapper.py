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

import numpy
from gnuradio import gr
import numpy as np

class mapper(gr.sync_block):
    """
    Q-PSK mapper.
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="mapper",
            in_sig=[numpy.uint32],
            out_sig=[numpy.complex64])
        self.modulation = 'qpsk'
        self.constellation = {'qpsk' : np.array([(+1+1j), (+1-1j), (-1-1j), (-1+1j)])}


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        out[:] = self.constellation[self.modulation].take(in0)
        return len(output_items[0])

