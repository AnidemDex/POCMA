import threading

from opcua import Server
from opcua import ua, uamethod
try:
    from robots.cnc.tprocess import RunStation
except:
    from res.robots.cnc.tprocess import RunStation

class MCStation:
    def __init__(self, IP, machine, robot, file_source):
        """
        Clase encargada de la creaci�n de las propiedades del servidor para el centro de mecanizado
        """
        self.cnc = machine
        self.movemaster = robot
        self.files = file_source

        ### CONFIGURACION ###
        self.server = Server()

        self.url = "opc.tcp://{}:8000/T/".format(IP)
        self.server.set_endpoint(self.url)

        server_name = "POCMA_TStation"
        self.server.set_server_name(server_name)

        server_namespace = "http://pocma.javerianacali.edu.co"
        workspace = self.server.register_namespace(server_name)

        nodes = self.server.get_objects_node()

        services = nodes.add_object(workspace, "Servicios")
        #######################


        ### METODO PARA LLAMAR A LA FABRICACION DE PIEZA ###
        arg_archivo = ua.Argument()
        arg_archivo.Name = "Pieza a fabricar ->"
        arg_archivo.DataType = ua.NodeId(ua.ObjectIds.Int32)
        arg_archivo.ValueRank = -1
        arg_archivo.ArrayDimensions = []
        arg_archivo.Description = ua.LocalizedText("fabricar(pieza_numero)")

        arg_reply = ua.Argument()
        arg_reply.Name = "Respuesta del servidor"
        arg_reply.DataType = ua.NodeId(ua.ObjectIds.String)

        method_run_mc = services.add_method(workspace, "Iniciar Torno", self.start_mc, [arg_archivo], [arg_reply])
        #####################################################


        ### EVENTO PARA LA CULMINACION DE LA PIEZA ###

        event_type = self.server.create_custom_event_type(workspace, 'T Ended', ua.ObjectIds.BaseEventType, [('Estado', ua.VariantType.Int32)])

        self.end_event = self.server.get_event_generator(event_type, services)


    def server_start(self):
        try:
            self.server.start()
        except Exception as error:
            print("[DETALLES] ", error)
            print("[INFO] Revisa bien la IP {}".format(self.url))
        else:
            print("Servidor iniciado")

    @uamethod
    def start_mc(self, parent_node, archivo):
        thread = threading.Thread(target=RunMcStation, args=(self.files, self.end_event, self.cnc, self.movemaster, archivo))
        thread.start()

        return "Peticion de pieza {}".format(archivo)
