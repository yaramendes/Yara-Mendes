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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from mapper_v0 import mapper_v0
import numpy as np

class qa_mapper_v0 (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        source_data = np.random.randint(0, high=4, size=10, dtype=np.int)
        lut = np.array([(+1+1j), (-1+1j), (+1-1j), (-1-1j)], dtype=complex)
        expected_result = lut[source_data]
        source = blocks.vector_source_i(source_data)
        qpsk_mapper = mapper_v0()
        sink = blocks.vector_sink_c()
        self.tb.connect(source, qpsk_mapper)
        self.tb.connect(qpsk_mapper, sink)
        self.tb.run()
        result_data = np.asarray(sink.data(), dtype=complex)
        # Check data
        comparison = expected_result == result_data
        check = comparison.all()
        print(check)


if __name__ == '__main__':
    gr_unittest.run(qa_mapper_v0, "qa_mapper_v0.xml")
