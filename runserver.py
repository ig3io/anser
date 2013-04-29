from anser import Anser


server = Anser(__name__, debug=True)


@server.action('default')
def action_a(message, address):
    print("{0} - {1}".format(address, message))


server.run()
