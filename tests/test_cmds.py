from unittest import TestCase

import qtmud
from qtmud import cmds


def _test_helps(tester, cmd, client):
    tester.assertTrue(cmd(client))
    tester.assertTrue(cmd(client, h=True))
    tester.assertTrue(cmd(client, H=True))


def _test_generic_bad_args(tester, cmd, client):
    tester.assertRaises(TypeError, cmd, client, z=True)
    tester.assertRaises(TypeError, cmd, client, fake='bad')


class TestCommands(TestCase):
    def test_commands(self):
        cmd = cmds.commands
        client = qtmud.Client()
        qtmud.subscribers['send'] = [qtmud.subscriptions.send]
        _test_helps(self, cmd, client)
        _test_generic_bad_args(self, cmd, client)
        self.assertTrue(cmd(client))
        self.assertRaises(TypeError, cmd, client, ['womble'])


class TestFoo(TestCase):
    def test_foo(self):
        cmd = cmds.foo
        client = qtmud.Client()
        qtmud.subscribers['send'] = [qtmud.subscriptions.send]
        _test_helps(self, cmd, client)
        _test_generic_bad_args(self, cmd, client)
        self.assertTrue(cmd(client))
        self.assertRaises(TypeError, cmd, client, ['womble'])


class TestHelp(TestCase):
    def test_help(self):
        # TODO more thorough tests
        cmd = cmds.help
        client = qtmud.Client()
        qtmud.subscribers['send'] = [qtmud.subscriptions.send]
        _test_helps(self, cmd, client)
        _test_generic_bad_args(self, cmd, client)
        self.assertTrue(cmd(client))
        self.assertTrue(cmd(client, topic='help'))
        self.assertTrue(cmd(client, topic='talker'))
        self.assertTrue(cmd(client, topic='talker', domain='cmds'))
        self.assertFalse(cmd(client, topic='notarealthing'))


class TestQuit(TestCase):
    def test_quit(self):
        cmd = cmds.quit
        client = qtmud.Client()
        qtmud.subscribers['send'] = [qtmud.subscriptions.send]
        qtmud.subscribers['client_disconnect'] = \
            [qtmud.subscriptions.client_disconnect]
        _test_helps(self, cmd, client)
        _test_generic_bad_args(self, cmd, client)
        self.assertTrue(cmd(client))


class TestTalker(TestCase):
    def test_talker(self):
        cmd = cmds.talker
        client = qtmud.Client()
        talker = qtmud.active_services['talker'] = qtmud.services.Talker()
        qtmud.subscribers['send'] = [qtmud.subscriptions.send]
        talker.tune_in(client, 'one')
        _test_helps(self, cmd, client)
        _test_generic_bad_args(self, cmd, client)
        self.assertTrue(cmd(client))
        self.assertTrue(cmd(client, channel='one'))
        self.assertTrue(cmd(client, channel='one', l=True))
        self.assertIsNone(cmd(client, channel='not-a-real-channel'))


class TestWho(TestCase):
    def test_who(self):
        cmd = cmds.who
        client = qtmud.Client()
        qtmud.subscribers['send'] = [qtmud.subscriptions.send]
        _test_helps(self, cmd, client)
        _test_generic_bad_args(self, cmd, client)
        self.assertTrue(cmd(client))


class TestWhoami(TestCase):
    def test_whoami(self):
        cmd = cmds.whoami
        client = qtmud.Client()
        qtmud.subscribers['send'] = [qtmud.subscriptions.send]
        _test_helps(self, cmd, client)
        _test_generic_bad_args(self, cmd, client)
