from anser import Anser


server = Anser(__name__, debug=True)

counter = 0

def increase_count():
    global counter
    counter += 1
    return counter

@server.action('default')
def action_a(data, address):
    print "Count: " + str(increase_count())

# Message filtering not implemented, yet
@server.action('other_category')
def action_b(data, address):
    print ":D"

server.run()

