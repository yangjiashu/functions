def choose_action(self, state, epsilon):

    # 提取出index=state的一行getrow，并找出该行最大Q值的action，即最大值对应的下标
    getrow = self.q_table.loc[[state],:].ix[0]
    getrow = getrow.reindex(np.random.permutation(getrow.index))
    action = getrow.idxmax()
    
    # if geedy
    if np.random.uniform() > epsilon:
        greedy = True
        return action, greedy

    #if not greedy
    else:
        newrow = getrow.drop(action)
        action = np.random.choice(newrow)
        greedy = False
        return action, greedy

