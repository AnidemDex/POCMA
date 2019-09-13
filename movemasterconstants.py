# encoding: utf-8
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
            raise RobotRangePositionError()
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
    """
    Move Position
    Mueve el final de la mano a una posicion donde las coordenadas son especificadas
    """
    command = "MP {}, {}, {}, {}, {}".format(x, y, z, pitch_angle, roll_angle)
    return command


def MS(pos_num, inter_points, grip_pos=None):
    """
    Move Straigth
    Mueve el robot a una posición especifica pasando a traves de una cantidad especifica de puntos intermedios
    """
    if isValidPosition(pos_num):
        if isValidPoints(inter_points):
            if grip_pos is not None:
                command = "MS {}, {}, {}".format(pos_num, inter_points, grip_pos)
            else:
                command = "MS {}, {}".format(pos_num, inter_points)

            return command
        else:
            raise RobotRangePositionError()
    else:
        raise RobotPositionError()


def MT(pos_num, travel_dist, grip_pos=None):
    """
    Move Tool
    Mueve el final de la mano de la posicion actual a una posicion lejana desde una posicion especificada
    """
    if isValidPosition(pos_num):
        if grip_pos is not None:
            command = "MT {}, {}, {}".format(pos_num, travel_dist, grip_pos)
        else:
            command = "MT {}, {}".format(pos_num, travel_dist)

        return command
    else:
        raise RobotPositionError()


def NT():
    """
    Nest
    Regresa el robot a su origen mecanico
    """
    command = "NT"
    return command


def OG():
    """
    Devuelve al robot a la posición de referencia para las coordenadas cartesianas
    """
    command = "OG"
    return command


def PA(pallet_num, col_grid_points, row_grid_points):
    """
    Pallet Assing
    Define el numero de puntos de cuadricula en una direccion de filas y columnas para especificar el numero de un pallet
    """
    if isValidPallet(pallet_num):
        if isValidColRow(col_grid_points, row_grid_points):
            command = "PA {}, {}, {}".format(pallet_num, col_grid_points, row_grid_points)
            return command
        else:
            raise RobotGridColPointError()
    else:
        raise RobotPalletNumberError()


def PC(position_a, position_b=None):
    """
    Position Clear
    Elimina la posiciones especificadas
    """
    if isValidPosition(position_a) and isValidPosition(position_b):
        if position_b is not None:
            command = "PC {}, {}".format(position_a, position_b)
        else:
            command = "PC {}".format(position_a)
        return command
    else:
        raise RobotPositionError()


def PD(pos_num, x, y, z, pitch_angle, roll_angle):
    """
    Position Define
    Define las coordenadas (posicion y angulo) de una posición especifica.
    """
    if isValidPosition(pos_num):
        command = "PD {}, {}, {}, {}, {}, {}".format(pos_num, x, y, z, pitch_angle, roll_angle)
        return command
    else:
        raise RobotPositionError()

def PL(position_a, position_b):
    """
    Position Load
    Asigna las coordenadas de una posición a otra
    """
    if isValidPosition(position_a) and isValidPosition(position_b):
        command = "PL {}, {}".format(position_a, position_b)
        return command
    else:
        raise RobotPositionError()


def PT(pallet_num):
    """
    Pallet
    Calcula las coordenadas de una cuadricula en el numero
    de pallet especifico e identifica las coordenadas 
    de la posicion correspondiente al pallet especificado
    """
    if isValidPallet(pallet_num):
        command = "PT {}".format(pallet_num)
        return command
    else:
        raise RobotPalletNumberError()


def PX(position_a, position_b):
    """
    Position Exchange
    Intercambia las coordenadas de una posicion a otra
    """
    if isValidPosition(position_a) and isValidPosition(position_b):
        command = "PX {}, {}".format(position_a, position_b)
        return command
    else:
        raise RobotPositionError()


def SF(position_a, position_b):
    """
    Shift
    Cambia las coordenadas de una posicion aumentando sus coordenadas en funcion de otra posicion
    """
    if isValidPosition(position_a) and isValidPosition(position_b):
        command = "SF {}, {}".format(position_a, position_b)
        return command
    else:
        raise RobotPositionError()


def SP(speed_level, variable_level=None):
    """
    Speed
    Configura la velocidad de operacion y el tiempo de (des)aceleración del robot
    DEFAULT: SP 4, L
    """
    if isValidSpeed(speed_level):
        if variable_level is not None:
            command = "SP {}, {}".format(speed_level, variable_level)
        else:
            command = "SP {}".format(speed_level)
        return command
    else:
        raise RobotInvalidSpeedError()


def TI(time_counter):
    """
    Timer
    Detiene el movimiento en un periodo de tiempo especifico (tiempo x 0.1)
    MAXIMO 3276.7 segundos (54.6 minutos)
    """
    command = "TI {}".format(time_counter)
    return command


def TL(tool_length):
    """
    Tool
    Establece la distancia entre el punto de montura de la mano y el final de la mano
    """
    command = "TL {}".format(tool_length)
    return command


def CP(count_num):
    """
    Compare Counter
    """
    command = "CP {}".format(count_num)
    return command


def DA(bit_num):
    """
    Disable Act
    """
    command = "DA {}".format(bit_num)
    return command


def DC(count_num):
    """
    Decrement Counter
    """
    command = "DC {}".format(count_num)
    return command


def DL(line_a, line_b=None):
    """
    Delete Line
    Elimina el contenido de una cantidad especifica de lineas
    """
    if line_b is not None:
        command = "DL {}, {}".format(line_a, line_b)
    else:
        command = "DL {}".format(line_a)
    return command


def EA(sign, bit_num, line_num):
    """
    Enable Act
    """
    command = "EA {}{}, {}".format(sign, bit_num, line_num)
    return command


def ED():
    """
    End
    Termina el programa
    No es necesario a no ser que estes programando al robot.
    Si se ejecutan los comandos directamente, este comando es innecesario
    """
    command = "ED"
    return command


def GT(line_num):
    """
    Go To
    Permite a la secuencia programada saltar a una linea especifica
    """
    command = "GT {}".format(line_num)
    return command


def IC(count_num):
    """
    Increment Counter
    """
    command = "IC {}".format(count_num)
    return command


def NW():
    """
    New
    Elimina todo programa y datos de posición guardados en la RAM
    """
    command = "NW"
    return command


def NX():
    """
    Next
    """
    command = "NX"
    return command


def RC(q_cycle):
    """
    Repeat Cycle
    """
    command = "RC {}".format(q_cycle)
    return command


def RN(start_line_num, end_line_num=None):
    """
    Run
    Ejecuta una parte especifica de instrucciones en el programa
    """
    if end_line_num is not None:
        command = "RN {}, {}".format(start_line_num, end_line_num)
    else:
        command = "RN {}".format(start_line_num)

    return command


def RT():
    """
    Return
    """
    command = "RT"
    return command


def SC(count_num, val=None):
    """
    Set Counter
    """
    if val is not None:
        command = "SC {}, {}".format(count_num, val)
    else:
        command = "SC {}".format(count_num)

    return command


def GC():
    """
    Grip Close
    Cierra el gripper
    """
    command = "GC"
    return command


def GF(val):
    """
    Grip Flag
    Define el estado abierto/cerrado del gripper (se usa junto con PD)
    """
    command = "GF {}".format(val)
    return command


def GO():
    """
    Grip Open
    Abre el gripper
    """
    command = "GO"
    return command


def GP(start_grip_force, retain_grip_force, retention_time):
    """
    Grip Pressure
    Define la fuerza de presion que sera aplicada por el motor cuando el gripper este abierto o cerrado
    """
    command = "GP {}, {}, {}".format(start_grip_force, retain_grip_force, retention_time)
    return command

def ID():
    """
    Input Direct
    """
    command = "ID"
    return command


def IN():
    """
    Input
    """
    command = "ID"
    return command


def OT(output_data):
    """
    Output
    """
    command = "OT {}".format(output_data)
    return command


"""""""""""""""""""""""""""""""""""""""""""""""""""""
RS232 READ SECTION
"""""""""""""""""""""""""""""""""""""""""""""""""""""

def CR(count_num):
    """
    Counter Read
    Lee el contenido de un contador especifico
    """
    command = "CR {}".format(count_num)
    return command


def DR():
    """
    Data Read
    Lee el contenido del registro interno
    """
    command = "DR"
    return command


def ER():
    """
    Error Read
    Lee el estado del error
    """
    command = "ER"
    return command


def LR(line_num):
    """
    Lee una linea especifica del programa
    """
    command = "LR {}".format(line_num)
    return command


def PR(pos_num):
    """
    Position Read
    Lee las coordenadas de una posicion especifica
    """
    command = "PR {}".format(pos_num)
    return command


def WH():
    """
    Where
    Lee las coordenadas de la posicion actual
    """
    command = "WH"
    return command


def RS():
    """
    Reset
    Reinicia el programa y la condicion de error
    """
    command = "RS"
    return command


def TR():
    """
    Transfer
    Traslada el programa y las posiciones guardadas en la EPROM a la RAM
    """
    command = "TR"
    return command


def WR():
    """
    Escribe el programa generado y las posiciones en la EPROM
    """
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

def isValidPoints(point_num):
    if point_num >= 1 and point_num <= 99:
        return True
    else:
        return False

def isValidPallet(pallet_num):
    if pallet_num >= 1 and pallet_num <= 9:
        return True
    else:
        return False

def isValidColRow(col, row):
    if (col >= 1 and col <=255) and (row >= 1 and row <= 255):
        return True
    else:
        return False

def isValidSpeed(speed):
    if speed >= 0 and speed <= 9:
        return True
    else:
        return False

class RobotPositionError(Exception):
    def __str__(self):
        return repr("[ERROR] El valor para la posicion debe ser >= 1 y <= 629")

class RobotRangePositionError(Exception):
    def __str__(self):
        return repr("[ERROR] El rango de las posiciones dadas supera la capacidad del robot")

class RobotGridColPointError(Exception):
    def __str__(self):
        return repr("[ERROR] El valor especificado para las columnas/filas excede la capacidad del robot")

class RobotPalletNumberError(Exception):
    def __str__(self):
        return repr("[ERROR] El numero del pallet debe ser <= 9 y >= 1")

class RobotInvalidSpeedError(Exception):
    def __str__(self):
        return repr("[ERROR] La velocidad debe estar entre 0 y 9")