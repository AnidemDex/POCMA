
def DP():
    """
    Decrement Position
    Movest he robot to a predefine position with a position numbers smaller than the current one.
    """
    command = "DP"
    return command


def DW(travel_x, travel_y, travel_z):
    """
    Draw
    """
    command = "DW {}, {}, {}".format(travel_x, travel_y, travel_z)
    return command


def HE(PositionNumber):
    """
    Here
    Definets the coordinates of the current position by assigning a positionn number to it
    """
    command = "HE {}".format(PositionNumber)
    return command


def HO():
    """
    Home
    reference posotion in the cartesioan coordenate system
    """
    command = "HO"
    return command


def IP():
    """
    Increment Position
    """
    command = "IP"
    return command


def MA(position_a, position_b, grip_pos=None):
    """
    Move Approach
    """
    if grip_pos is not None:
        command = "MA {}, {}, {}".format(position_a, position_b, grip_pos)
    else:
        command = "MA {}, {}".formar(position_a, position_b)
        
    return command


def MC(position_a, position_b):
    command = "MC {}, {}".format(position_a, position_b)
    return command
	

def MJ(waist_angle=0, shoulder_angle=0, elbow_angle=0, pitch_angle=0, roll_angle=0):
    command = "MJ {}, {}, {}, {}, {}".format(waist_angle, shoulder_angle, elbow_angle, pitch_angle, roll_angle)
    return command


def MO(pos_num, grip_pos=None):
    if grip_pos is not None:
        command = "MO {}, {}".format(pos_num, grip_pos)
    else:
        command = "MO {}".format(pos_num)

    return command
	

def MP(x, y, z, pitch_angle, roll_angle):
	command = "MP {}, {}, {}, {}, {}".format(x, y, z, pitch_angle, roll_angle)
	return command
	

def MS(pos_num, inter_points, grip_pos=None):
	if grip_pos is not None:
		command = "MS {}, {}, {}".format(pos_num, inter_points, grip_pos)
	else:
		command = "MS {}, {}".format(pos_num, inter_points)
	
	return command


def MT(pos_num, travel_dist, grip_pos=None):
	if grip_pos is not None:
		command = "MT {}, {}, {}".format(pos_num, travel_dist, grip_pos)
	else:
		command = "MT {}, {}".format(pos_num, travel_dist)
	
	return command


def NT():
    command = "NT"
    return command


def OG():
	command = "OG"
	return command


def PA(pallet_num, col_grid_points, row_grid_points):
	command = "PA {}, {}, {}".format(pallet_num, col_grid_points, row_grid_points)
	return command


def PC(position_a, position_b=None):
	if position_b is not None:
		command = "PC {}, {}".format(position_a, position_b)
	else:
		command = "PC {}".format(position_a)
	
	return command


def PD(pos_num, x, y, z, pitch_angle, roll_angle):
	command = "PD {}, {}, {}, {}, {}, {}".format(pos_num, x, y, z, pitch_angle, roll_angle)
	return command
	

def PL(position_a, position_b):
	command = "PL {}, {}".format(position_a, position_b)
	return command


def PT(pallet_num):
	command = "PT {}".format(pallet_num)
	return command


def PX(position_a, position_b):
	command = "PX {}, {}".format(position_a, position_b)
	return command


def SF(position_a, position_b):
	command = "SF {}, {}".format(position_a, position_b)
	return command


def SP(speed_level, variable_level=None):
	if variable_level is not None:
		command = "SP {}, {}".format(speed_level, variable_level)
	else:
		command = "SP {}".format(speed_level)
	
	return command


def TI(time_counter):
	command = "TI {}".format(time_counter)
	return command


def TL(tool_length):
	command = "TL {}".format(tool_length)
	return command


def CP(count_num):
	command = "CP {}".format(count_num)
	return command


def DA(bit_num):
	command = "DA {}".format(bit_num)
	return command


def DC(count_num):
	command = "DC {}".format(count_num)
	return command


def DL(line_a, line_b=None):
	if line_b is not None:
		command = "DL {}, {}".format(line_a, line_b)
	else:
		command = "DL {}".format(line_a)
	
	return command


def EA(sign, bit_num, line_num):
	command = "EA {}{}, {}".format(sign, bit_num, line_num)
	return command


def ED():
	command = "ED"
	return command


def GT(line_num):
	command = "GT {}".format(line_num)
	return command


def IC(count_num):
	command = "IC {}".format(count_num)
	return command


def NW():
	command = "NW"
	return command


def NX():
	command = "NX"
	return command


def RC(q_cycle):
	command = "RC {}".format(q_cycle)
	return command


def RN(start_line_num, end_line_num=None):
	if end_line_num is not None:
		command = "RN {}, {}".format(start_line_num, end_line_num)
	else:
		command = "RN {}".format(start_line_num)
	
	return command


def RT():
	command = "RT"
	return command


def SC(count_num, val=None):
	if val is not None:
		command = "SC {}, {}".format(count_num, val)
	else:
		command = "SC {}".format(count_num)
	
	return command


def GC():
	command = "GC"
	return command


def GF(val):
	command = "GF {}".format(val)
	return command


def GO():
	command = "GO"
	return command


def GP(start_grip_force, retain_grip_force, retention_time):
	command = "GP {}, {}, {}".format(start_grip_force, retain_grip_force, retention_time)
	return command

def ID():
	command = "ID"
	return command


def IN():
	command = "ID"
	return command


def OT(output_data):
	command = "OT {}".format(output_data)
	return command


def CR(count_num):
    command = "CR {}".format(count_num)
    return command


def DR():
    command = "DR"
    return command


def ER():
    command = "ER"
    return command


def LR(line_num):
    command = "LR {}".format(line_num)
    return command


def PR(pos_num):
    command = "PR {}".format(pos_num)
    return command


def WH():
    command = "WH"
    return command


def RS():
    command = "RS"
    return command


def TR():
    command = "TR"
    return command


def WR():
    command = "WR"
    return command


class Execute:
    """Envia un comando directamente al robot para su ejecución inmediata"""

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
