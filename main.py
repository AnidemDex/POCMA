from res.robots.robot import CNC, RVM1
from res.mcstation import MCStation
from res.tstation import TStation

import tools
import threading

puerto = tools.get_port_property()
puerto_torno = puerto['torno']
puerto_robot_torno = puerto['robot_torno']
puerto_mecanizado = puerto['mecanizado']
puerto_robot_mecanizado = puerto['robot_mecanizado']


torno = CNC()
robot_torno = RVM1()
mecanizado = CNC()
robot_mecanizado = RVM1()

torno.connect(puerto_torno)
robot_torno.connect(puerto_robot_torno)

mecanizado.connect(puerto_mecanizado)
robot_mecanizado.connect(puerto_robot_mecanizado)

ip = tools.get_ip()
directorio = tools.get_directory()

servidor_torno = TStation(ip, torno, robot_torno, directorio)
servidor_mecanizado = MCStation(ip, mecanizado, robot_mecanizado, directorio)

thread_servidor_torno = threading.Thread(target=servidor_torno.server_start)
thread_servidor_mecanizado = threading.Thread(target=servidor_mecanizado.server_start)

thread_servidor_torno.start()
thread_servidor_mecanizado.start()




input()
servidor_torno.stop()
servidor_mecanizado.stop()
exit()
