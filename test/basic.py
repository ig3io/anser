import unittest
from anser import Anser, Client


class BasicAnserTest(unittest.TestCase):

    def test_creation(self):
        server = Anser(__file__)
        self.assertEqual(server.name, __file__)

    def test_creation_explicit_no_debug(self):
        server = Anser(__file__, debug=False)
        self.assertFalse(server.debug)

    def test_creation_implicit_no_debug(self):
        server = Anser(__file__)
        self.assertFalse(server.debug)

    def test_creation_explicit_debug(self):
        server = Anser(__file__, debug=True)
        self.assertTrue(server.debug)

    def test_add_action(self):
        server = Anser(__file__)
        @server.action('default')
        def dummy_action(message, address):
            pass
        self.assertTrue(dummy_action in server.actions)


class BasicClientTest(unittest.TestCase):

    def test_creation(self):
        client = Client('10.0.0.1', 4000)
        self.assertEqual(client.address, '10.0.0.1')
        self.assertEqual(client.port, 4000)

    def test_creation_implicit_no_debug(self):
        client = Client('10.0.0.1', 4000)
        self.assertFalse(client.debug)

    def test_creation_explicit_debug(self):
        client = Client('10.0.0.1', 4000, debug=True)
        self.assertTrue(client.debug)


if __name__ == '__main__':
    unittest.main()
