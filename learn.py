def learn(self, s, a, r, s_, a_, done, alpha=0.5, gamma=0.9, lam=0.8):
    # step-1 选择状态s_的最优策略
    a_star = self.choose_action(s_, 0)
    
    # step-2 count Q-target
    # step-2.1
    if not done:
        target = r + gamma * self.q_table.loc[[s_],a_star].iloc[0]

    # step-2.2 
    else:
        target = r

    # step-3 count TD-error
    error = target - self.q_table.loc[[s],a].iloc[0]

    # step-4 update the tables
    self.e_table[[s],a] = 1
    self.q_table = self.q_table + alpha*error*self.e_table
    
    # step-5 update e_table
    if a_star == a_:
        self.e_table = self.e_table * lam
    else:
        self.e_table[:] = 0

