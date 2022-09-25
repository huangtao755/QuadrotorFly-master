#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The file used to implement the data store and replay

By xiaobo
Contact linxiaobo110@gmail.com
Created on Wed Jan 17 10:40:44 2018
"""
# Copyright (C)
#
# This file is part of QuadrotorFly
#
# GWpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GWpy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GWpy.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np
import torch as t

"""
********************************************************************************************************
**-------------------------------------------------------------------------------------------------------
**  Compiler   : python 3.6
**  Module Name: MemoryStore
**  Module Date: 2018-04-17
**  Module Auth: xiaobo
**  Version    : V0.1
**  Description: create the module
**-------------------------------------------------------------------------------------------------------
**  Reversion  : V0.2
**  Modified By: xiaobo
**  Date       : 2019-4-25
**  Content    : rewrite the module, add note
**  Notes      :
"""

"""
*********************************************************************************************************
Define nural network
*********************************************************************************************************
"""

t.manual_seed(5)

state_dim = 12
v_dim = 1
action_dim = 4
learning_rate = 0.005
learning_num = 1000
sim_num = 20
x0 = np.array([2, -1])
epislon = 0.0001
Fre_V1_paras = 5


############################################################################################################
# 定义网络
############################################################################################################


class Model(t.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.lay1 = t.nn.Linear(state_dim, 10, bias=False)
        self.lay1.weight.data.normal_(0, 0.5)
        self.lay2 = t.nn.Linear(10, 1, bais=False)
        self.lay2.weight.date.normal_(0, 0.5)

    def forward(self, x):
        layer1 = self.lay1(x)
        layer1 = t.nn.functional.relu(layer1)
        output = self.lay2(layer1)
        return output


class ADP_s():
    def __init__(self, evn, state_dim):
        self.evn = evn

        self.V1_model = Model()
        self.V2_model = Model()
        self.Criterion = t.nn.MSELoss(reduction='mean')

        self.optimizerV2 = t.optim.SGD(self.V2_model.parameters(), lr=learning_rate)

        self.state = None
        self.state_dim = state_dim

        self.action = 0
