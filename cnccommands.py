# encoding: utf-8
"""
Archivo intencionalmente documentado de forma parcial debido a falta de informacion sobre su funcionamiento
Una buena porcion de las funciones son autoexplicatorias
"""
class Execute:

    def __init__(self, cnc_handler):
        self.cnc = cnc_handler

    def nc(self, directory_file):
        """
        Abre un archivo NC y envia los comandos, linea por linea
        """
        try:
            file = open(directory_file, "rb")
        except OSError as error:
            print("[ERROR] El fichero especificado quizas no existe")
            print("[DETALLES] {}").format(error)
        else:
            line = 0
            for command in file:
                print(line)
                self.cnc.conexion.write(command)
                line += 1


        def code(self, line):
            self.cnc.send(line)


        def M(self, code):
            command = "M{};"
            self.cnc.send(command)


        def husillo_horario(self):
            command = "M03;"
            self.cnc.send(command)


        def husillo_antihorario(self):
            command = "M04;"
            self.cnc.send(command)


        def stop_spindle(self):
            command = "M05;"
            self.cnc.send(command)


        def change_tool(self, tool):
            command = "M06 {};".format(tool)
            self.cnc.send(command)


        def open_helper(self):
            command = "M010;"
            self.cnc.send(command)


        def close_helper(self):
            command = "M011;"
            self.cnc.send(command)


        def open_n_stop(self):
            command = "M037;"
            self.cnc.send(command)


        def open_door(self):
            command = "M38;"
            self.cnc.send(command)


        def close_door(self):
            command = "M39;"
            self.cnc.send(command)