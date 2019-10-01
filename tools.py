import socket
import configparser
import os


def get_ip():
    """
    Return:(str) local_ip
    Esta funcion devuelve la ip local de la maquina donde se este ejecutando
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()
    print("[TOOLS] Uso de la herramienta para obtencion de IPs. Resultado: {}".format(local_ip))
    return local_ip


def get_port_property():
    """
    Return:(str) port
    Esta funcion devuelve la configuracion de puertos de los metadatos del archivo INI de configuracion
    """
    configuration_file = configparser.ConfigParser()
    configuration_file.read("config.ini")
    port = configuration_file['puertos']
    return port


def get_directory():
    """
    Return: (str) directory
    Esta funcion devuelve el directorio absoluto del directorio de trabajo actual
    """
    directory = os.getcwd()
    print("[TOOLS] Directorio de trabajo: {}".format(directory))
    return directory
