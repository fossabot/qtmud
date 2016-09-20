""" Game library
    
    .. moduleauthor: emsenn <morgan.sennhauser@gmail.com>
    
    .. versionadded:: 0.0.1
    .. versionchanged:: 0.0.1-feature/environments
        added Tavern, Village
    .. versionchanged:: 0.0.1-feature/parser
        added a Field
    .. versionchanged:: 0.0.2-feature/neverforgetholidayupdate
        added NineElevenMemorial ;_;7
    
    Testing for potential game library - don't expect good documentation here.
"""

from qtmud.qualities import (Physical, Container, Room, Renderable, Teaching,
                             Noisy)

from qtmud.lib.qualities import Swordsmanship, Healthful

class Tavern(object):
    """ Ye Olde Tavern
    
        .. versionadded:: 0.0.1-feature/environments
        .. versionchanged:: 0.0.3-feature/noise
            added noises & more Renderables
    """
    def __init__(self):
        return
    
    def apply(self, thing):
        """ turn a thing into a Tavern
        
            .. versionadded:: 0.0.1-features/environments
            .. versionchanged:: 0.0.2-features/parser
                Added explicit use of Container quality.
        """
        tavern = thing.manager.add_qualities(thing, [Room, 
                                                     Container,
                                                     Renderable])
        tavern.name = 'Ye Olde Tavern'
        tavern.description = ('This is the inside of a tavern so normal, it '
                              'hardly warrants description. There are tables '
                              'and chairs, and against one wall, there\'s a '
                              'long counter. An open doorway leads outside.')
        tavern.noises = {'listen': ['A wind outside causes the tavern to '
                                    'creak slightly.'],
                         'look': ['A bough shifts outside, covering a window '
                                  'and darkening the tavern for a moment.']}
        tables = tavern.manager.new_thing(Renderable)
        tables.update({'name': 'scattered tables',
                      'description': ('Ye Olde Tavern has several tables set '
                                      'up. They\'re all wooden, but that is '
                                      'about where the similarities end. One '
                                      'table is painted bright red, another '
                                      'is unusually short, and a third is '
                                      'round and clearly not level.')})
        red_table = tavern.manager.new_thing(Renderable, Container)
        red_table.update({'name': 'bright red painted table',
                         'description': ('This table is painted bright red, '
                                         'with sloppy brush strokes clearly '
                                         'visible.')})
        brush_strokes = tavern.manager.new_thing(Renderable)
        brush_strokes.update({'name': 'messy paint',
                             'nametags': {'brushstrokes', 'strokes'},
                             'adjectives': {'brush','red','paint'},
                             'description': ('The paint strokes on the table '
                                             'laid down the paint thick, '
                                             'leaving permanent dribbles and '
                                             'smears.')})
        red_table.add(brush_strokes)
        short_table = tavern.manager.new_thing(Renderable, Container)
        short_table.update({'name': 'short table',
                            'description': ('This table looks like it was '
                                            'made for ants.')})
        round_table = tavern.manager.new_thing(Renderable, Container)
        round_table.update({'name': 'The Round Table',
                            'adjectives': {'uneven', 'unlevel'},
                            'description': ('This round table seems to be '
                                            'significant, although its hard '
                                            'to place exactly why. It also '
                                            'is clearly uneven.')})
        counter = tavern.manager.new_thing(Renderable, Container)
        counter.update({'name': 'tavern bar',
                        'nametags': {'counter'},
                        'adjectives': {'long'},
                        'description': ('Not quite a bar, as there\'s no '
                                        'seating, this counter separates the '
                                        'employees of Ye Olde Tavern from '
                                        'the patrons.')})
        windows = tavern.manager.new_thing(Renderable)
        windows.update({'name': 'windows',
                        'nametags': {'window'},
                        'adjectives': {'two'},
                        'description': ('Two windows are in the facade wall '
                                        'of Ye Olde Tavern, letting the sun '
                                        'light the room.')})
        daylight = tavern.manager.new_thing(Renderable)
        daylight.update({'name': 'daylight',
                         'description': ('Thanks to the two windows, daylight '
                                        'fills Ye Olde Tavern.')})
        # TODO overwrite round_table add() method to have things roll off
        # this'll be the go-to demonstration of overwriting qualities
        tavern.add(tables, red_table, short_table, round_table, counter, windows, daylight)
        tavern.exits = { 'outside' : Village }
        return tavern
        
class Village(object):
    """ A little village.

        .. versionadded:: 0.0.1-feature/environments
        .. versionchanged:: 0.0.2-feature/parser
            added explicit use of the Container quality.
        .. versionchanged:: 0.0.2-feature/nametags
            added some Renderables.
        .. versionchanged:: 0.0.3-feature/learning
            added an exit to Smithy
    """
    def __init__(self):
        return
    
    def apply(self, thing):
        village = thing.manager.add_qualities(thing, [Room,
                                                      Container,
                                                      Renderable])
        village.name = 'Center of Ye Olde Village'
        village.description = ('The center of a small village. On one side of '
                               'the commons is a tavern, and on the other '
                               'side there is a blacksmith\'s workshop.')
        village.sounds = ('It is suspiciously quiet here.')
        tavern = thing.manager.new_thing(Renderable)
        tavern.update({'name': 'Ye Olde Tavern',
                       'description': 'Despite the name, Ye Olde Tavern '
                                      'appears to have been built quite '
                                      'recently. Its facade is built of pine '
                                      'logs, and the door is wide open, so '
                                      'one could just "move inside".'})
        logs = thing.manager.new_thing(Renderable)
        logs.update({'name': 'fresh hewn pine logs',
                     'description': 'The walls of the Ye Olde Tavern are '
                                    'made from pine, so freshly cut they '
                                    'look sticky to the touch.'})
        door = thing.manager.new_thing(Renderable)
        door.update({'name': 'open door',
                     'description': 'The door to Ye Olde Tavern is wide open, '
                                    'making it seem like an inviting place.'})
        village.add(tavern, logs, door)
        village.exits = { 'tavern': Tavern,
                          'smith': Smithy,
                          'field': Field }
        return village

class Field(object):
    """ An empty field.
    
        .. versionadded:: 0.0.2-feature/parser
    """
    def __init__(self):
        return
    
    def apply(self, thing):
        field = thing.manager.add_qualities(thing, [Room,
                                                    Container,
                                                    Renderable])
        field.update({'name': 'Memorial Field',
                      'description': 'This field is just outside Ye Olde '
                                     'Village. There are two copper pillars '
                                     'erected (hehe) here.'})
        memorial = thing.manager.new_thing(Renderable)
        memorial.update({'name': '9/11 Memorial',
                         'nametags': {'pillars'},
                         'adjectives': {'copper', 'solid', 'marbled'},
                         'description': 'Two solid copper blocks rise up from '
                                        'the ground. Wide bands of verdigris '
                                        'marble their surface.'})
        bird = thing.manager.new_thing(Renderable, Physical, Noisy, )
        bird.update({'name': 'bird',
                     'nametags': {'birb'},
                     'adjectives': {'noisy'},
                     'description': ('This is a cute little bird, '
                                     'or if you\'re visiting from Tumblr, '
                                     'you might call it a birb.'),
                     'noises': {'listen': ['the bird tweets melodically',
                                           ('the bird tweets in less than 140 '
                                            'characters.')]}})
        field.add(memorial, bird)
        field.exits = { 'village' : Village }
        return field

class Smithy(object):
    """ A blacksmith's workshop

        .. versionadded:: 0.0.3-feature/learning
    """
    def __init__(self):
        return

    def apply(self, thing):
        smithy = thing.manager.add_qualities(thing, [Room,
                                                     Container,
                                                     Renderable])
        smithy.update({'name': 'Smithy',
                       'description': 'This is the inside of a blacksmith\'s '
                                      'workshop.'})
        blacksmith = thing.manager.new_thing(Renderable, Physical, Teaching)
        blacksmith.update({'name': 'Henry Smith',
                           'nametags': {'smith', 'henry', 'blacksmith'},
                           'adjectives': {'black'},
                           'description': 'Maybe Henry\'s last name is Smith '
                                          'because he is a smith, or maybe '
                                          'Henry is a blacksmith because his '
                                          'last name is Smith.'})
        blacksmith.teachable_qualities['swordsmanship'] = Swordsmanship
        blacksmith.teachable_qualities['health'] = Healthful
        mouse = thing.manager.new_thing(Renderable, Physical, Healthful)
        mouse.update({'name':'mouse',
                      'description': ('they\'re so cute, why would you "fight" '
                                      'them?')})
        smithy.add(blacksmith, mouse)
        smithy.exits = {'outside': Village}
        return smithy
