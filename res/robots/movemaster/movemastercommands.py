# encoding: utf-8
try:
    import movemasterconstants as command
except:
    import res.robots.movemaster.movemasterconstants as command

class Execute:
    """
    Execute.<Command>()
    Envia un comando directamente al robot para su ejecución inmediata
    """
    def __init__(self, rob_handler):
        """
        rob_handler: (RVM1)
        """
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
            if grip_pos == None:
                self.robot.send(command.MA(pos_a, pos_b))
            else:
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
                self.robot.send(command.MO(pos_num))
            else:
                self.robot.send(command.MO(pos_num, grip_pos))
        except command.RobotPositionError as error:
            print(error)


    def MP(self, x, y, z, pitch, roll):
        self.robot.send(command.MP(x, y, z, pitch, roll))


    def MS(self, pos_num, inter_points, grip_pos=None):
        try:
            if grip_pos == None:
                self.robot.send(command.MS(pos_num, inter_points))
            else:
                self.robot.send(command.MS(pos_num, inter_points, grip_pos))
        except command.RobotPositionError as error:
            print(error)
        except command.RangePositionError as error:
            print(error)


    def MT(self, pos_num, travel, grip_pos=None):
        try:
            if grip_pos == None:
                self.robot.send(command.MT(pos_num, travel))
            else:
                self.robot.send(command.MT(pos_num, travel, grip_pos))
        except command.RobotPositionError as error:
            print(error)


    def NT(self):
        self.robot.send(command.NT())


    def OG(self):
        self.robot.send(command.OG())


    def PA(self, pallet, col, row):
        try:
            self.robot.send(command.PA(pallet, col, row))
        except command.PalletNumberError as error:
            print(error)
        except command.GridColPointError as error:
            print(error)


    def PC(self, pos_a, pos_b=None):
        try:
            self.robot.send(command.PC(pos_a, pos_b))
        except command.RobotPositionError as error:
            print(error)


    def PD(self, pos_num, x=0, y=0, z=0, pitch=0, roll=0):
        try:
            self.robot.send(command.PD(pos_num, x, y, z, pitch, roll))
        except command.RobotPositionError as error:
            print(error)


    def PL(self, pos_a, pos_b):
        try:
            self.robot.send(command.PL(pos_a, pos_b))
        except command.RobotPositionError as error:
            print(error)


    def PT(self, pallet):
        try:
            self.robot.send(command.PT(pallet))
        except command.RobotPalletNumberError as error:
            print(error)


    def PX(self, pos_a, pos_b):
        try:
            self.robot.send(command.PX(pos_a, pos_b))
        except command.RobotPositionError as error:
            print(error)


    def SF(self, pos_a, pos_b):
        try:
            self.robot.send(command.SF(pos_a, pos_b))
        except command.RobotPositionError as error:
            print(error)


    def SP(self, speed, var=None):
        try:
            self.robot.send(command.SP(speed, var))
        except command.RobotInvalidSpeedError as error:
            print(error)


    def TI(self, time):
        self.robot.send(command.TI(time))


    def TL(self, length):
        self.robot.send(command.TL(length))


    def CP(self, count):
        self.robot.send(command.CP(count))


    def DA(self, bit):
        self.robot.send(command.DA(bit))


    def DC(self, count):
        self.robot.send(command.DC(count))


    def DL(self, line_a, line_b=None):
        self.robot.send(command.DL(line_a, line_b))


    def EA(self, sign, bit, line):
        self.robot.send(command.EA(sign, bit, line))


    def ED(self):
        self.robot.send(command.ED())


    def GT(self, line):
        self.robot.send(command.GT(line))


    def IC(self, count):
        self.robot.send(command.IC(count))


    def NW(self):
        self.robot.send(command.NW())


    def NX(self):
        self.robot.send(command.NX())


    def RC(self, cycle):
        self.robot.send(command.RC(cycle))


    def RN(self, start_line, end_line=None):
        self.robot.send(command.RN(start_line, end_line))


    def RT(self):
        self.robot.send(command.RT())


    def SC(self, count, val=None):
        self.robot.send(command.SC(count, val))


    def GC(self):
        self.robot.send(command.GC())


    def GF(self, val):
           self.robot.send(command.GF(val))

    def GO(self):
        self.robot.send(command.GO())


    def GP(self, s_grip, r_grip, r_time):
           self.robot.send(command.GP(s_grip, r_grip, r_time))


    def ID(self):
        self.robot.send(command.ID())


    def IN(self):
        self.robot.send(command.IN())

    def OT(self, data):
        self.robot.send(command.OT(data))

    #### RS232 READ SECTION ####

    def CR(self, count):
        self.robot.send(command.CR(count))
        reply = self.read()
        return reply


    def DR(self):
        self.robot.send(command.DR())
        reply = self.read()
        return reply


    def ER(self):
        self.robot.send(command.ER())
        reply = self.read()
        return reply


    def LR(self, line):
        self.robot.send(command.LR(line))
        reply = self.read()
        return reply


    def PR(self, pos_num):
        self.robot.send(command.PR(pos_num))
        reply = self.read()
        return reply


    def WH(self):
        self.robot.send(command.WH())
        reply = self.read()
        return reply

    def RS(self):
        self.robot.send(command.RS())

    def TR(self):
        self.robot.send(command.TR())


    def WR(self):
        self.robot.send(command.WR())


    def read(self):
        eol = b'\r' #End Of File. Con eso modificas el terminador de linea
        leneol = len(eol)
        line = bytearray()

        self.robot.conexion.flush()
        while True:
            character = self.robot.conexion.read(1)
            if character:
                line += character
                if line[-leneol:] == eol:
                    break
            else:
                break
        del line[-leneol:]
        return bytes(line)

class Program:
    """
    Program.<Command>()
    Crea una lista temporal de comandos para ser escritos en la memoria del robot
    para luego ser ejecutados con el comando Execute.RN()
    Cada linea se suma sola en un digito de forma automatica con cada comando usado
    """
    def __init__(self, rob_handler):
        self.robot = rob_handler
        self.line = 0


    def clear_lines(self):
        """
        Pone en 0 el contador de linea para esccribir un nuevo programa
        """
        self.line = 0

    def set_lines(self, value):
        """
        Establece el contador de linea en el valor deseado para continuar desde
        ese punto la programación
        """
        self.line = value


    def DP(self):
        self.__program(command.DP())


    def DW(self, x, y, z):
        self.__program(command.DW(x, y, z))


    def HE(self, pos_num):
        try:
            self.__program(command.HE(pos_num))
        except command.RobotPositionError as error:
            print(error)


    def HO(self):
        self.__program(command.HO())


    def IP(self):
        self.__program(command.IP())


    def MA(self, pos_a, pos_b, grip_pos=None):
        try:
            if grip_pos == None:
                self.__program(command.MA(pos_a, pos_b))
            else:
                self.__program(command.MA(pos_a, pos_b, grip_pos))
        except command.RobotPositionError as error:
            print(error)


    def MC(self, pos_a, pos_b):
        try:
            self.__program(command.MC(pos_a, pos_b))
        except command.RobotPositionError as error:
            print(error)
        except command.RobotPositionError as error:
            print(error)


    def MO(self, pos_num, grip_pos=None):
        try:
            if grip_pos == None:
                self.__program(command.MO(pos_num))
            else:
                self.__program(command.MO(pos_num, grip_pos))
        except command.RobotPositionError as error:
            print(error)


    def MS(self, pos_num, inter_points, grip_pos=None):
        try:
            if grip_pos == None:
                self.__program(command.MS(pos_num, inter_points))
            else:
                self.__program(command.MS(pos_num, inter_points, grip_pos))
        except command.RobotPositionError as error:
            print(error)
        except command.RangePositionError as error:
            print(error)


    def MT(self, pos_num, travel, grip_pos=None):
        try:
            if grip_pos == None:
                self.__program(command.MT(pos_num, travel))
            else:
                self.__program(command.MT(pos_num, travel, grip_pos))
        except command.RobotPositionError as error:
            print(error)


    def NT(self):
        self.__program(command.NT())


    def OG(self):
        self.__program(command.OG())


    def PA(self, pallet, col, row):
        try:
            self.__program(command.PA(pallet, col, row))
        except command.PalletNumberError as error:
            print(error)
        except command.GridColPointError as error:
            print(error)


    def PL(self, pos_a, pos_b):
        try:
            self.__program(command.PL(pos_a, pos_b))
        except command.RobotPositionError as error:
            print(error)


    def PT(self, pallet):
        try:
            self.__program(command.PT(pallet))
        except command.RobotPalletNumberError as error:
            print(error)


    def PX(self, pos_a, pos_b):
        try:
            self.__program(command.PX(pos_a, pos_b))
        except command.RobotPositionError as error:
            print(error)


    def SF(self, pos_a, pos_b):
        try:
            self.__program(command.SF(pos_a, pos_b))
        except command.RobotPositionError as error:
            print(error)


    def SP(self, speed, var=None):
        try:
            self.__program(command.SP(speed, var))
        except command.RobotInvalidSpeedError as error:
            print(error)


    def TI(self, time):
        self.__program(command.TI(time))


    def TL(self, length):
        self.__program(command.TL(length))


    def CP(self, count):
        self.__program(command.CP(count))


    def DA(self, bit):
        self.__program(command.DA(bit))


    def DC(self, count):
        self.__program(command.DC(count))


    def EA(self, sign, bit, line):
        self.__program(command.EA(sign, bit, line))


    def ED(self):
        self.__program(command.ED())


    def GT(self, line):
        self.__program(command.GT(line))


    def IC(self, count):
        self.__program(command.IC(count))


    def NX(self):
        self.__program(command.NX())


    def RC(self, cycle):
        self.__program(command.RC(cycle))


    def RT(self):
        self.__program(command.RT())


    def SC(self, count, val=None):
        self.__program(command.SC(count, val))


    def GC(self):
        self.__program(command.GC())


    def GF(self, val):
        self.__program(command.GF(val))

    def GO(self):
        self.__program(command.GO())


    def GP(self, s_grip, r_grip, r_time):
        self.__program(command.GP(s_grip, r_grip, r_time))


    def ID(self):
        self.__program(command.ID())


    def IN(self):
        self.__program(command.IN())

    def OT(self, data):
        self.__program(command.OT(data))

    def __program(self, arg):
        self.line += 1
        comando = "{} {}".format(self.line, arg)
        self.robot.send(comando)


class Cnc:
    def __init__(self, rob_handler):
        self.robot = rob_handler
        self.robot.program.set_lines(0)
        self.line_movement1 = 0
        self.line_movement2 = 0
        self.line_movement3 = 0
        self.line_movement4 = 0

    def teach_routine(self):
        print("[INFO] Enseñando movimiento 1")
        self.movement1()
        print("[INFO] Enseñando movimiento 2")
        self.movement2()
        print("[INFO] Enseñando movimiento 3")
        self.movement3()
        print("[INFO] Enseñando movimiento 4")
        self.movement4()


    def movement1(self):
        self.robot.program.MO(557,"C")
        self.line_movement1 = self.robot.program.line

        self.robot.program.SP(8,"H")

        self.robot.program.MO(556,"C")

        self.robot.program.MO(555,"C")

        self.robot.program.MO(554,"C")

        self.robot.program.MO(550,"C")

        self.robot.program.MO(551,"C")

        self.robot.program.MO(552,"C")

        self.robot.program.SP(3,"H")

        self.robot.program.MS(553,8,"C")

        self.robot.program.GO()

        self.robot.program.SP(8,"H")

        self.robot.program.MS(552,5,"O")

        self.robot.program.MO(551,"O")

        self.robot.program.MO(550,"O")

        self.robot.program.MO(550,"O")
        # 16

    def movement2(self):
        #salir de la maquina y esperar a que termine de maquinar

        self.robot.program.GO()
        self.line_movement2 = self.robot.program.line

        self.robot.program.TI(1)

        self.robot.program.SP(9,"H")

        self.robot.program.MO(557,"O")

        self.robot.program.MO(556,"O")

        self.robot.program.MO(555,"O")

        self.robot.program.MO(554,"O")

        self.robot.program.MO(550,"O")

        self.robot.program.MO(550,"O")
        # 10

    def movement3(self):
        #entrar a la maquina a sujetar la pieza en la prensa antes de llevarla al pallet

        self.robot.program.SP(9,"H")
        self.line_movement3 = self.robot.program.line

        self.robot.program.MO(554,"O")

        self.robot.program.MO(555,"O")

        self.robot.program.MO(556,"O")

        self.robot.program.MO(557,"O")

        self.robot.program.SP(2,"H")

        self.robot.program.MO(558,"O")

        self.robot.program.GC()
        # 8

    def movement4(self):
        #sacar la pieza de la prensa y llevarla al pallet, despues ir a esperar
        self.robot.program.MO(557,"C")
        self.line_movement4 = self.robot.program.line

        self.robot.program.SP(8,"H")

        self.robot.program.MO(556,"C")

        self.robot.program.MO(555,"C")

        self.robot.program.MO(554,"C")

        self.robot.program.MO(550,"C")

        self.robot.program.MO(551,"C")

        self.robot.program.MO(552,"C")

        self.robot.program.SP(3,"H")

        self.robot.program.MS(553,8,"C")

        self.robot.program.GO()

        self.robot.program.SP(8,"H")

        self.robot.program.MS(552,5,"O")

        self.robot.program.MO(551,"O")

        self.robot.program.MO(550,"O")


        self.robot.program.MO(550,"O")


    def run_movement(self, movement):
        self.robot.conexion.flush()

        if movement == 1:
            self.robot.execute.RN(self.line_movement1, self.line_movement2-1)
        if movement == 2:
            self.robot.execute.RN(self.line_movement2, self.line_movement3-1)
        if movement == 3:
            self.robot.execute.RN(self.line_movement3, self.line_movement4-1)
        if movement == 4:
            self.robot.execute.RN(self.line_movement4, self.robot.program.line)


# FIXME Añade los comandos de Robot
class Torno:
    def __init__(self, rob_handler):
        self.robot = rob_handler
        self.robot.program.set_lines(0)
        self.line_movement1 = 0
        self.line_movement2 = 0
        self.line_movement3 = 0
        self.line_movement4 = 0

    def teach_routine(self):
        print("[INFO] Enseñando movimiento 1")
        self.movement1()
        print("[INFO] Enseñando movimiento 2")
        self.movement2()
        print("[INFO] Enseñando movimiento 3")
        self.movement3()
        print("[INFO] Enseñando movimiento 4")
        self.movement4()

    def movement1(self):
        self.robot.program.MO(400,"O")
        self.line_movement1 = self.robot.program.line

        self.robot.program.SP(8,"H")

        self.robot.program.MO(401,"O")

        self.robot.program.SP(5,"H")

        self.robot.program.MO(402,"O")

        self.robot.program.GC()

        self.robot.program.TI(5)

        self.robot.program.MS(403,5,"C")

        self.robot.program.SP(8,"H")

        self.robot.program.MO(400,"C")

        self.robot.program.MO(404,"C")

        self.robot.program.MO(405,"C")

        self.robot.program.SP(4,"H")

        self.robot.program.MO(406,"C")

        self.robot.program.MO(406,"C")


    def movement2(self):
        self.robot.program.SP(8,"H")
        self.line_movement2 = self.robot.program.line

        self.robot.program.GO()

        self.robot.program.MO(405,"O")

        self.robot.program.MO(404,"O")

        self.robot.program.MO(400,"O")

        self.robot.program.MO(400,"O")

    def movement3(self):
        self.robot.program.MO(404,"O")
        self.line_movement3 = self.robot.program.line

        self.robot.program.MO(405,"O")

        self.robot.program.MO(406,"O")

        self.robot.program.GC()

        self.robot.program.GC()

    def movement4(self):
        self.robot.program.MS(405,5,"C")
        self.line_movement4 = self.robot.program.line

        self.robot.program.MO(404,"C")

        self.robot.program.MO(400,"C")

        self.robot.program.MO(403,"C")

        self.robot.program.MS(402,8,"C")

        self.robot.program.GO()

        self.robot.program.TI(3)

        self.robot.program.MO(401,"O")

        self.robot.program.MO(400,"C")

        self.robot.program.MO(400,"C")

    def run_movement(self, movement):
        self.robot.conexion.flush()

        if movement == 1:
            self.robot.execute.RN(self.line_movement1, self.line_movement2-1)
        if movement == 2:
            self.robot.execute.RN(self.line_movement2, self.line_movement3-1)
        if movement == 3:
            self.robot.execute.RN(self.line_movement3, self.line_movement4-1)
        if movement == 4:
            self.robot.execute.RN(self.line_movement4, self.robot.program.line)
