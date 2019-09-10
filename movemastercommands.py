
def format_command(command_handler, command_array):
    """Reacomoda la tupla que se le pase de forma que pueda ser escrita en el Robot
    NOTA: Esta es la forma dificil de hacerla en codigo"""

    command_range = len(command_array)
    for i in range(command_range):
        if i == 0:
            data = command_array[i] + " "
        elif i == (command_range-1):
            if isinstance(command_array[i], float):
                if command_array[i] > 0:
                    data = data + "+"+str(command_array[i])
                else:
                    data = data+str(command_array[i])
            else:
                data = data + str(command_array[i])
        else:
            if isinstance(command_array[i], float):
                if command_array[i] > 0:
                    data = data + "+"+str(command_array[i]) + ", "
                else:
                    data = data+str(command_array[i]) + ", "
            else:
                data = data + str(command_array[i]) + ", "
    print("[INFO] Comando a enviar: {}".format(data))
    command_handler.send(data)


def DP(command_handler):
    """
    Decrement Position
    Movest he robot to a predefine position with a position numbers smaller than the current one.
    """
    command_handler.send("DP")


def DW(command_handler, x, y, z):
    """
    Draw
    """
    data = ["DW", x, y, z]
    command_handler.format_command(data)


def HE(command_handler, PositionNumber):
    """
    Here
    Definets the coordinates of the current position by assigning a positionn number to it
    """
    data = ["HE", PositionNumber]
    command_handler.format_command(data)


def HO(command_handler):
    """
    Home
    reference posotion in the cartesioan coordenate system
    """
    command_handler.send("HO")


def IP(command_handler):
    """
    Increment Position
    """
    command_handler.send("IP")


def MA(command_handler, Pa, Pb, OC):
    """
    Move Approach
    """
    data = ["MA", Pa, Pb, OC]
    command_handler.format_command(data)


def MO(command_handler, pos_num, command_number=None):
    command_handler.send("MO {}".format(pos_num))


def NT(command_handler):
    command_handler.send("NT")


class Execute:
    """Enviar un comando directamente al robot para su ejecución inmediata"""

    def __init__(self, rob_handler):
        self.robot = rob_handler

    def DP(self):
        DP(self.robot)

    def DW(self, x, y, z):
        DW(self.robot, x, y, z)

    def HE(self, pos_num):
        HE(self.robot, pos_num)

    def HO(self):
        HO(self.robot)

    def IP(self):
        IP(self.robot)

    def MA(self, arg1, arg2, arg3):
        MA(self.robot, Pa=arg1, Pb=arg2, OC=arg3)

    def MO(self, pos_numb):
        MO(self.robot, pos_numb)

    def NT(self):
        NT(self.robot)
