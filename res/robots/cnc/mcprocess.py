from opcua import ua
import time

# FIXME REVISA ESTE CODIGO
def RunMcStation(files, server_event, machine, robot, pieza):
	"""
	Funcion encargada de mecanizar una pieza
	files: (String)Un string del directorio absoluto donde estan los archivos
	server_event: El evento del servidor a activar
	machine: (Robot) Objeto encargado de mover la maquina CNC
	robot: (Robot) Objeto encargado de mover el robot
	pieza: (Int)
	"""
	robot.key_cnc.runM1()
	machine.execute.open_helper()

	time.sleep(2)

	robot.key_cnc.runM2()
	machine.execute.close_door()
	time.sleep(1)

	file = check_file(files, pieza)

	machine.nc(file)
	time.sleep(3)

	machine.execute.open_door()

	# Desbordamiento de buffer
	limiter = 0
	while limiter < 200:
		machine.execute.code("M11")
		ch = ch +1			
	time.sleep(1) 

	robot.key_cnc.runM3()
	machine.execute.open_helper()
	time.sleep(2)

	robot.key_cnc.runM3()
	time.sleep(1)

	reply = "Mecanizado Completado"
	server_event.event.Message = ua.LocalizedText(reply)
	server_event.event.Estado = 2
	server_event.trigger()
	print(reply)


def check_file(absolute_path, pieza):
	switcher = {
		1: "{}/BOTELLA.NC".format(absolute_path),
		2: "{}/SOLDADO.NC".format(absolute_path),
		3: "{}/EJE.NC".format(absolute_path)
		}

	return switcher.get(pieza, None)