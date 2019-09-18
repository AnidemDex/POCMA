#FIXME CONVERTIR ESTE ARCHIVO EN EL CLIENTE
import sys
sys.path.insert(0, "..")

try:
    from IPython import embed
except ImportError:
    import code

    def embed():
        vars = globals()
        vars.update(locals())
        shell = code.InteractiveConsole(vars)
        shell.interact()



from opcua import Client
from opcua import ua

class SubHandler(object):

    """
    Subscription Handler. To receive events from server for a subscription
    data_change and event methods are called directly from receiving thread.
    Do not do expensive, slow or network operation there. Create another
    thread if you need to do such a thing
    """
    def event_notification(self, event):
        print("New event recived: ", event)






url = "opc.tcp://192.168.0.103:4840"
client = Client(url)



try:
    client.connect()
    print("Conectado a {}".format(url))
    root = client.get_root_node()
    print("Objects node is: ", root)

    print("Children of root are: ", root.get_children())

    obj = root.get_child(["0:Objects", "2:Servicios"])
    print("myobj is: ", obj)

    event = root.get_child(["0:Types", "0:EventTypes", "0:BaseEventType", "2:MC Ended"])
    print("Evento: ", event)

    msctl = SubHandler()
    sub = client.create_subscription(100, msctl)
    handle = sub.subscribe_events(obj, event)

    embed()
    sub.unsubscribe(handle)
    sub.delete()

finally:
    client.disconnect()