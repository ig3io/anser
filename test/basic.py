import unittest
from anser import Anser


class BasicTest(unittest.TestCase):

    def setUp(self):
        pass


    def test_creation(self):
        server = Anser(__file__)
        self.assertEquals(server.name, __file__)


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

    def test_receive(self):
        pass


    def test_send(self):
        pass


if __name__ == '__main__':
    unittest.main()
