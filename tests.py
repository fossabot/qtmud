import unittest

import qtmud
from qtmud.services import MUDSocket


class MUDSocketTest(unittest.TestCase):
    def setUp(self):
        self.mudsocket = MUDSocket()

    def tearDown(self):
        self.mudsocket.shutdown()

    def test_start(self):
        self.assertTrue(self.mudsocket.start())

if __name__ == '__main__':
    unittest.main()