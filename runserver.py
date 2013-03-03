from anser import Anser


server = Anser(__name__, protocol='udp')
server.run(ip='127.0.0.1',
           port=8083,
           debug=True)
