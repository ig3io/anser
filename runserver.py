from anser import Anser


server = Anser(__name__)
server.run(ip='127.0.0.1', port=8053, debug=True)
