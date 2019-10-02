from opcua import ua
import time

is_station_ready = False


def ConfigStation(machine, robot):
	__robotconfig(robot)
	__cncconfig(machine)
	global is_station_ready
	is_station_ready = True


def RunStation(files, server_event, machine, robot, pieza):
	"""
	Funcion encargada de mecanizar una pieza
	files: (String)Un string del directorio absoluto donde estan los archivos
	server_event: El evento del servidor a activar
	machine: (Robot) Objeto encargado de mover la maquina CNC
	robot: (Robot) Objeto encargado de mover el robot
	pieza: (Int)
	"""
	if is_station_ready:
		__runstationprocess(files, server_event, machine, robot, pieza)
	else:
		raise StationIsNotReadyError()


def check_file(absolute_path, pieza):
	switcher = {
		1: "{}/files/BOTELLA.NC".format(absolute_path),
		2: "{}/files/SOLDADO.NC".format(absolute_path),
		3: "{}/files/EJE.NC".format(absolute_path)
		}

	return switcher.get(pieza, None)


def __robotconfig(robot):
	print("[ROBOT][INFO] PROCESO DE ENSEÑANZA DEL ROBOT INICIALIZADO")
	robot.key_cnc.teach_routine()
	robot.execute.MO(550, "O")


def __cncconfig(machine):
	print("[CNC][INFO] PROCESO DE CONFIGURACION INICIADO")
	machine.execute.close_door()
	machine.execute.close_door()
	machine.execute.code("G28 X0 Y0")
	machine.execute.open_helper()
	machine.execute.open_door()
	machine.execute.open_helper()
	machine.execute.open_door()


def __runstationprocess(files, server_event, machine, robot, pieza):
	robot.key_cnc.run_movement(1)
	machine.execute.open_helper()

	time.sleep(2)

	robot.key_cnc.run_movement(2)
	machine.execute.close_door()
	time.sleep(1)

	file = check_file(files, pieza)

	machine.execute.nc(file)
	time.sleep(3)

	machine.execute.open_door()

	# Desbordamiento de buffer
	limiter = 0
	while limiter < 200:
		machine.execute.code("M11")
		limiter += 1
	time.sleep(1)

	robot.key_cnc.run_movement(3)
	machine.execute.open_helper()
	time.sleep(2)

	robot.key_cnc.run_movement(4)
	time.sleep(1)

	reply = "Proceso Mecanizado Completado"
	# FIXME REPARA ESTE TRYCATCH QUE ESTA HORRIBLE LA FORMA DE MANEJAR ESTE ERROR
	try:
		server_event.event.Message = ua.LocalizedText(reply)
		server_event.event.Estado = 2
		server_event.trigger()
	except Exception:
		print("NO SE ENVIO EL EVENTO")
	print("[CNC][INFO] "+reply)


class StationIsNotReadyError(Exception):
	def __str__(self):
		str_error = """[ERROR] La estación no se encuentra lista para un correcto funcionamiento.
		Asegurese de haber usado mcprocess.ConfigStation(machine, robot)
		antes de usar mcprocess.RunStation(files, server_event, machine, robot, pieza)"""
		return repr("{}".format(str_error))
