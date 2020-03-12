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

class demapper(gr.sync_block):
    """
    QPSK demapper
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="demapper",
            in_sig=[np.complex64],
            out_sig=[np.uint32])
        self.constellation = {
            'qpsk': np.array([(+1 + 1j), (-1 + 1j), (+1 - 1j), (-1 - 1j)])}  # 0, 1, 2, 3

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        map = self.constellation['qpsk']

        # First Kronecker product generates a matrix where the lines are copies of in0.
        # Second Kronecker product generates a matrix where each lines repeats a symbol of the constellation in each column.
        dist = abs( np.kron(in0, np.ones([map.size, 1])) - np.kron(map, np.ones([in0.size, 1])).transpose() )
        
        print(in0)

        print(map.size)
        print(np.ones([map.size, 1]))
        print(np.kron(in0, np.ones([map.size, 1])))

        print(in0)

        print(in0.size)
        print(np.ones([in0.size, 1]))
        print(np.kron(map, np.ones([in0.size, 1])).transpose())

        # print(( np.kron(in0, np.ones([map.size, 1])) - np.kron(map, np.ones([in0.size, 1])).transpose() ))
        # print(dist)

        # Check each column of the dist matrix for finding the smaller element. 
        # The index of the row corresponds to the constellation's symbol index.
        out[:] = np.argmin(dist, axis=0)
        return len(output_items[0])

