import movemasterconstants as command

class Execute:
    """Envia un comando directamente al robot para su ejecución inmediata"""

    def __init__(self, rob_handler):
        self.robot = rob_handler


    def DP(self):
        self.robot.send(command.DP())


    def DW(self, x, y, z):
        self.robot.send(command.DW(x, y, z))


    def HE(self, pos_num):
        try:
            self.robot.send(command.HE(pos_num))
        except command.RobotPositionError as error:
            print(error)


    def HO(self):
        self.robot.send(command.HO())


    def IP(self):
        self.robot.send(command.IP())


    def MA(self, pos_a, pos_b, grip_pos=None):
        try:
            self.robot.send(command.MA(pos_a, pos_b, grip_pos))
        except command.RobotPositionError as error:
            print(error)

    
    def MC(self, pos_a, pos_b):
        try:
            self.robot.send(command.MC(pos_a, pos_b))
        except command.RobotPositionError as error:
            print(error)
        except command.RobotPositionError as error:
            print(error)


    def MJ(self, waist, shoulder, elbow, pitch, roll):
        self.robot.send(command.MJ(waist, shoulder, elbow, pitch, roll))
        
    def MO(self, pos_num, grip_pos=None):
        try:
            if grip_pos == None:
                command.MO(pos_num)
            else:
                command.MO(pos_num, grip_pos)
        except command.RobotPositionError as error:
            print(error)
    


    def NT(self):
        command.NT()
