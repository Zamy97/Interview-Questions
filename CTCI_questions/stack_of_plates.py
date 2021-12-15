class SetOfStacks:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("Make your capacity a little bigger please")

        self.capacity = capacity
        self.stacks = [[]]

    def push(self, val):
        if len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])

        self.stacks[-1].append(val)

    def pop(self):
        if len(self.stacks[-1]) == 0:
            if len(self.stacks) == 1:
                raise IndexError("pop from empty stack")
            else:
                self.stacks.pop()
                
        return self.stacks[-1].pop()
