def step(self, action):
    # Firstly, change the environment to next state.
    # step-1
    order = self.demand(action, self.left_t)

    # terminal
    # 如果时间处在最后一个定价时间点或者需求大于库存，则下一个状态为terminal
    if self.left_i == len(self.times)-1 or order-self.left_c >= 0:
        # step-2.21
        s_ = tuple([0, 0])
        r = action * min(self.left_c, order)
        done = False
        info = {}
    
    # not terminal
    else:
        # step-2.11 更行environment的状态
        self.left_c = self.left_c - order
        self.i += 1
        self.left_t = self.times[self.i]
        
        # step-2.12 获取观测值
        s_ = self.left_c
        r = order * action
        done = False
        info = {}

    # Then return the observations
    return s_, r, done, info
