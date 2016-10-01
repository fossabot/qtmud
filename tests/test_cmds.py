from unittest import TestCase

import qtmud
from qtmud import cmds, services, subscriptions


class TestCommands(TestCase):
    def test_commands(self):
        client = qtmud.Client()
        qtmud.subscribers['send'] = [qtmud.subscriptions.send]
        self.assertTrue(cmds.commands(client, ''))


class TestTalker(TestCase):
    def test_talker(self):
        qtmud.subscribers['send'] = [qtmud.subscriptions.send]
        talker = services.Talker()
        qtmud.active_services['talker'] = talker
        client = qtmud.Client()
        client.channels = ['one']
        self.assertTrue(cmds.talker(client, ''))
        self.assertTrue(cmds.talker(client, 'history'))
        self.assertTrue(cmds.talker(client, 'history one'))
        self.assertFalse(cmds.talker(client, 'history fakechannel'))
        self.assertRaises(AttributeError, cmds.talker, object(), '')
        self.assertRaises(AttributeError, cmds.talker, client, 42)


class TestWhoami(TestCase):
    def test_whoami(self):
        client = qtmud.Client()
        self.assertEqual(cmds.whoami(client, ''), str(client.identity))
