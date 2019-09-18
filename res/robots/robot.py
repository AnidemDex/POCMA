# encoding: utf-8
from serial import Serial
from serial import SerialException
from movemaster import movemastercommands as rob_command
from cnc import cnccommands as cnc_command


class Robot:
    """Define parametros y comandos basicos de cualquier robot.
    Cada robot trae por individual su propio metodo de conexion y de comandos"""

    def __init__(rob):
        rob.conexion = Serial()
        """Crea un modulo serial en blanco para el manejo de errores en caso de haberlos"""

    def send(rob, command=None):
        """
        Atajo para la escritura de Serial.write() el cual ya hace el
        proceso de formateo de la cadena de texto
        """

        if command is not None:
            try:
                rob.conexion.write('{}\n'.format(command).encode('utf-8'))
            except SerialException as error:
                print("[ERROR] El comando {} no pudo ser escrito".format(command))
                print("\tVerifica que el robot esté conectado al puerto antes de enviar el comando")
                print("[DETALLES] {}".format(error))
            else:
                print("[INFO] {} enviado correctamente por {}".format(command, rob.conexion.name))
        else:
            return rob

    def disconnect(self):
        """
        Atajo para la escritura de Serial.close(), con un
        conductor de errores personalizado
        """
        if self.conexion.isOpen():
            try:
                self.conexion.close()
            except SerialException as error:
                print("[ERROR] Algo ocurrio al intentar cerrar el puerto")
                print("[DETALLES] {}".format(error))
                pass
            else:
                print("[INFO] Conexion finalizada")
        else:
            print("[INFO] El puerto del robot se encuentra cerrado")

    @property
    def is_clear_to_send(rob):
        """
        Propiedad de manejo de control por hardware que probablemente
        será eliminado en futuras versiones debido a su inutilidad frente
        a su uso en los robots
        """
        return rob.conexion.cts


class RVM1(Robot):
    """
    Hereda: Robot
    Clase creada para el manejo exclusivo del robot MoveMaster
    """

    def __init__(self):
        self.execute = rob_command.Execute(self)
        """Propiedad creada para el envio de comandos al instante"""
        self.program = rob_command.Program(self)
        """Propiedad creada para la programación de comandos por linea"""
        self.key_cnc = rob_command.Cnc(self)
        """Propiedad creada para atajos"""
        self.key_torno = rob_command.Torno(self)

        Robot.__init__(self)

    def connect(self, puerto):
        """
        Conecta el puerto del robot para el envío de comandos
        """

        try:
            self.conexion.port = puerto
            self.conexion.baudrate = 9600
            self.conexion.bytesize = 7
            self.conexion.parity = "O"
            self.conexion.stopbits = 2
            self.conexion.rtscts = True
            self.conexion.timeout= 2.0

            self.conexion.open()
            if self.conexion.isOpen():
                self.conexion.flushInput()  # vacia bufer entrada
                self.conexion.flushOutput()  # vaciar bufer de salida
        except SerialException as error:
            print("[ERROR] No se pudo conectar al puerto {}".format(puerto))
            print("[DETALLES] {}".format(error))
        else:
            print("RVM1 conectado correctamente al puerto {}".format(self.conexion.name))
            return self


class CNC(Robot):
    """
    Hereda: Robot
    Clase creada para el manejo exclusivo del torno CNC y la fresadora CNC
    """


    def __init__(self):
        self.execute = cnc_command.Execute(self)
        """Propiedad creada para el envio de comandos de una libreria"""

        Robot.__init__(self)


    def connect(self, puerto):
        """
        Conecta el puerto del robot para el envío de comandos
        """
        try:
            self.conexion.port = puerto
            self.conexion.baudrate = 2400
            self.conexion.bytesize = 7
            self.conexion.parity = "E"
            self.conexion.stopbits = 2
            self.conexion.rtscts = False
            self.conexion.xonxoff = True
            self.conexion.timeout= 2.0

            self.conexion.open()
            if self.conexion.isOpen():
                self.conexion.flushInput()  # vacia bufer entrada
                self.conexion.flushOutput()  # vaciar bufer de salida
        except SerialException as error:
            print("[ERROR] No se pudo conectar al puerto {}".format(puerto))
            print("[DETALLES] {}".format(error))
        else:
            print("Robot CNC conectado correctamente al puerto {}".format(self.conexion.name))
            return self
