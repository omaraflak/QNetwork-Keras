class Game():
    def __init__(self):
        self.length = 10;
        self.position = 0;
        self.actions = [0, 1]; # left, right
        self.actionsCount = len(self.actions)

    def takeAction(self, action):
        if action==0:
            if self.position>0:
                self.position += -1;
        if action==1:
            if self.position<self.length-1:
                self.position += 1;

        if self.position==0:
            return -1, self.position;
        elif self.position==self.length-1:
            return 10, self.position;
        else:
            return 0, self.position;

    def reset(self):
        self.position = 0;
        return 0;

    def finished(self):
        return self.position==self.length-1;
