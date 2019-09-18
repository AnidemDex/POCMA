import socket

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()
    print("Uso de la herramienta para obtencion de IPs. Resultado: {}".format(local_ip))
    return local_ip