class Giraffes():
    #函数：左脚向前
    def funcLeftFootForward(self):
        print('left foot forward')
    #函数：右脚向前
    def funcRightFootForward(self):
        print('right foot forward')
    #函数：左脚向后
    def funcLeftFootBack(self):
        print('left foot back')
    #函数：右脚向后
    def funcRightFootBack(self):
        print('right foot back')
    #函数：跳舞
    def funcDance(self):
        self.funcLeftFootForward()
        self.funcLeftFootBack()
        self.funcRightFootForward()
        self.funcRightFootBack()
        self.funcLeftFootBack()
        self.funcRightFootBack()
        self.funcRightFootForward()
        self.funcLeftFootForward()
 
reginald=Giraffes()
reginald.funcDance()
