from anser import Anser


server = Anser(__name__, debug=True)


@server.action('default')
def action_a(message, address):
    print message['type']
    print message['body']


server.run()

