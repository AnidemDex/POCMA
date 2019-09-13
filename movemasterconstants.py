
def DP():
    """
    Decrement Position
    Mueve el robot a una posicion menor a la actual.
    """
    command = "DP"
    return command


def DW(travel_x, travel_y, travel_z):
    """
    Draw
	Mueve el robot una distancia especifica en coordenadas cartesianas
    """
    command = "DW {}, {}, {}".format(travel_x, travel_y, travel_z)
    return command


def HE(pos_num):
    """
    Here
    Enseña la posicion actual al robot
    """
    if isValidPosition(pos_num):
        command = "HE {}".format(pos_num)
        return command
    else:
        raise RobotPositionError()

def HO():
    """
    Home
    Configura la posicion de referencia en coordenadas cartesianas
    """
    command = "HO"
    return command


def IP():
    """
    Increment Position
	Mueve el robot a una posicion superior a la actual
    """
    command = "IP"
    return command


def MA(position_a, position_b, grip_pos=None):
    """
    Move Approach
    Mueve el robot a una posicion especifica de forma incremental
    """
    if isValidPosition(position_a) and isValidPosition(position_b):
        if grip_pos is not None:
            command = "MA {}, {}, {}".format(position_a, position_b, grip_pos)
        else:
            command = "MA {}, {}".formar(position_a, position_b)
            
        return command
    else:
        raise RobotPositionError()


def MC(position_a, position_b):
    """
    Move Continuous
    Mueve el robot de forma continua entre puntos predefinidos
    para ir del punto A al punto B
    """
    if isValidPosition(position_a) and isValidPosition(position_b):
        if isValidRange(position_a, position_b):
            command = "MC {}, {}".format(position_a, position_b)
            return command
        else:
            raise RangePositionError()
    else:
        raise RobotPositionError()


def MJ(waist_angle=0, shoulder_angle=0, elbow_angle=0, pitch_angle=0, roll_angle=0):
    """
    Move Joint
    Mueve cada articulacion en el angulo especificado
    """
    command = "MJ {}, {}, {}, {}, {}".format(waist_angle, shoulder_angle, elbow_angle, pitch_angle, roll_angle)
    return command


def MO(pos_num, grip_pos=None):
    """
    Move
    Mueve el final de la mano del robot a una posicion especifica
    """
    if isValidPosition(pos_num):
        if grip_pos is not None:
            command = "MO {}, {}".format(pos_num, grip_pos)
        else:
            command = "MO {}".format(pos_num)
    
        return command
    else:
        raise RobotPositionError()


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



def isValidPosition(position_number):
    if position_number >= 1 and position_number <= 629:
        return True
    else:
        return False

def isValidRange(x, y):
    operation = abs(x-y)
    if operation <= 99:
        return True
    else:
        return False

class RobotPositionError(Exception):
    def __str__(self):
        return repr("[ERROR] El valor para la posicion debe ser >= 1 y <= 629")

class RangePositionError(Exception):
    def __str__(self):
        return repr("[ERROR] El rango de las posiciones dadas supera la capacidad del robot")