import types

class Client(object):
    """ Turns a bland thing into a fancy Client thing.
        
        .. version added:: 0.0.1
        .. version changed:: 0.0.1-feature/parsing
            added the whoami, set, and echo commands
    """
    def __init__(self, **kw):
        """ create the main Client quality instance, so we don't have to 
            keep creating more of them.
        """
        # XXX ^^-^^ It might not actually do that, but that is what it 
        # *should* be doing.
        super(Client, self).__init__(**kw)
        return

    def send(self, thing, data, end='\n'):
        """ prepare data to be sent to a client.
        
            .. versionadded:: 0.0.1
        """
        # XXX strip any trailing newlines from bad previous formating.
        thing.send_buffer += data + end
    
    def echo(self, thing, data):
        """ echo some text to the client)
            
            .. version added:: 0.0.1-feature/parsing
        """
        thing.send(data)
    
    def whoami(self, thing, data):
        """ tells the thing their name and identity
        
            .. version added:: 0.0.1-feature/parsing
        """
        finger = ('name:        {0}\n'
                  'id:          {1}\n'.format(thing.name,
                                              thing.identity))
        thing.send(finger)

    def set(self, thing, trailing):
        """ sets an attribute in the client, meant to be used with the 
            set command
        
            .. version added:: 0.0.1-version/parsing
        """
        if trailing == '':
            thing.send('syntax: set <attribute> <value>',
                        'example: set name Bob')
        trailing = trailing.split()
        attribute, value = trailing[0], " ".join(trailing[1:])
        try:
            setattr(thing, attribute, value)
        except Exception as err:
            self.manager.log.warning('unexpected exception caught '
                                     'when %s entered the command '
                                     '%s %s\nerror to follow:%s', 
                                     client.name, cmd, trailing, err)
            client.send('the command failed, check console')

    def apply(self, thing):
        """ Applies the Client quality to `thing`
        
            .. version added:: 0.0.1
            .. version changed:: 0.0.1-feature/organizing
                added basic attribute overwrite protection
            .. version changed:: 0.0.1-feature/parsing
                added commands dict to Client
                
            addr:           tuple representing the client's address
            send_buffer:    string going to be send to the client next tick()
            recv_buffer:    string received from the client this tick()
            send:           function for formating send_buffer
            whoami:         function for telling Client its name & identity
            echo:           function for testing Client's send/receive parsing
            set:            function for setting Client's attributes.
            
            
        """
        if not hasattr(thing, 'addr'):
            thing.addr = tuple
        if not hasattr(thing, 'send_buffer'):
            thing.send_buffer = ''
        if not hasattr(thing, 'recv_buffer'): 
            thing.recv_buffer = ''              
        if not hasattr(thing, 'name'):
            thing.name = str(thing.identity)
        if not hasattr(thing, 'send'):
            thing.send = types.MethodType(self.send, thing)
        if not hasattr(thing, 'commands'):
            thing.commands = {'whoami': types.MethodType(self.whoami, thing),
                              'echo': types.MethodType(self.echo, thing),
                              'set': types.MethodType(self.set, thing) }
        return thing
