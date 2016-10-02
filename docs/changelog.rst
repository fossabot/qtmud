Changelog
=========

%%version%% (unreleased)
------------------------

Changes
~~~~~~~

- Added Development Flow to Development Docs. [emsenn]

- Documented Parameters in ``qtmud.cmds`` [emsenn]

- Added Tests for qtmud.cmds. [emsenn]

  Also preparing to use gitchangelog to aid with versioning moving
  forward.

Other
~~~~~

- Merge branch 'master' into develop. [emsenn]

- Cleaner Shutdown/Startup. [emsenn]

  Added --logdir and --datadir options to `./bin/qtmud_run`

  Also fixed bugs #21 and #23

- Codecov YML Addition. [emsenn]

- Merge branch 'master' of github.com:emsenn/qtmud. [emsenn]

- Update .travis.yml. [emsenn]

- Update .travis.yml. [emsenn]

- Start of qtmud.cmds Test Cases. [emsenn]

- Added Code Climate Integration to Travis CI. [emsenn]

- Merge branch 'master' of github.com:emsenn/qtmud. [emsenn]

- Delete environment.pickle. [emsenn]

- Merge branch 'release/0.0.7' [emsenn]

- Merge branch 'release/0.0.6' [emsenn]

  First real package, I think? I hope. I'm sorry to anyone reading this
  from the future, I am a newbie.

- Merge branch 'release/0.0.7' into develop. [emsenn]

0.0.7 (2016-10-01)
------------------

- V0.0.7: Doc Refactor & client_disconnect Fix. [emsenn]

- Doc Refactoring, Fixed client_disconnect Bug. [emsenn]

- Merge branch 'release/0.0.6' into develop. [emsenn]

0.0.6 (2016-10-01)
------------------

- First "Good" Packaging Release. [emsenn]

- Merge branch 'master' into release/0.0.6. [emsenn]

  I messed up the git flow whoops

- Some random cleanups. [emsenn]

- Documentation Update - Removed mudlib docs. [emsenn]

- Fixed Broken MUDSocket Test. [emsenn]

- Update README.md. [emsenn]

- Update README.md. [emsenn]

- Update README.md. [emsenn]

- Update README.md. [emsenn]

- Update README.md. [emsenn]

- Update README.md. [emsenn]

- Added CodeClimate Badge to README.md. [emsenn]

- Transition to Package. [emsenn]

  Shifting qtMUD into being an acceptable Python package.

- Code Coverage? [emsenn]

- Fixed ./data/ not being in git. [emsenn]

- More Cards. [emsenn]

  And a few other trivial changes.

- More Fireside Cards. [emsenn]

  Cleaning up of Fireside code, too

- Require sudo in Travis CI. [emsenn]

  Travis-CI doesn't like that we require brlapi, and while I could just
  remove the requirement, we are going to need it eventually.

- Added requirements.txt. [emsenn]

- Merge branch 'master' of github.com:emsenn/qtmud. [emsenn]

- Update README.md. [emsenn]

- Travis CI Scripts. [emsenn]

  Simple tests for Travis CI? Maybe? I don't get how it works.

- Fireside Documentation. [emsenn]

  Built and added Fireside documentation.

- Attempted Fix for ReadTheDocs error. [emsenn]

  error was Could not import extension sphinx.ext.githubpages (exception:
  No module named githubpages)

  this is what google said would help

- PEP8 Updates & Fireside Cards. [emsenn]

- Fireside Mudlib. [emsenn]

  Simple cardgame mudlib and some edits to qtmud methods

- Basic Talker Service. [emsenn]

  A really basic and lazy implementation of a talker service.

- Reduction of Dependence on Starhopper. [emsenn]

  qtMUD, through refactoring, became dependent on Starhopper methods.

  This fixes some of that./

- Documentation Hotfix Part Three. [emsenn]

- Merge branch 'master' of github.com:emsenn/qtmud. [emsenn]

- Merge pull request #16 from emsenn/develop. [emsenn]

  Develop

- Merge pull request #14 from emsenn/develop. [emsenn]

  Develop

- Merge branch 'release/0.0.4' [emsenn]

- Merge branch 'release/0.0.3' [emsenn]

  Release of version 0.0.3 to master woooo

- Merge branch 'release/0.0.4' into develop. [emsenn]

0.0.4 (2016-09-26)
------------------

- Bump to version 0.0.4. [emsenn]

- .gitignore hotfix. [emsenn]

- Documentation Hotfix. [emsenn]

- Documentation Cleanup, Separating Client and Ship in Starhopper.
  [emsenn]

  Title about says it all.

- Mirrored Starhopper Structure in Qtmud. [emsenn]

  Updated qtmud to use a package structure more in line with the updated
  starhopper structure.

- Bringing Back Documentation. [emsenn]

  It's back! and less messy than ever!

- Deleted Broken Documentation, Refactored Starhopper. [emsenn]

  The documentation wasn't rendering right so I just got rid of it.

  also, refactored starhopper. Need to shuffle qtmud to match,
  unfortunately. New system is way better, though.

- Merge branch 'feature/diceroller' into develop. [emsenn]

  Got a little carried away with this feature

- Starhopper Update. [emsenn]

  Got frustrated with trying to buy a full MMORPG in one go so made a
  dinky little space adventure game.

- Migration to Game Library. [emsenn]

  I realized a lot of stuff was in qtmud that was better suited for the
  specific libraries - not every game that gets built is going to want a
  "say" command, for instance.

- Refactor. [emsenn]

  It finally clicked with me what people were saying about organizing the
  engine differently, so this is me shuffling around toward doing that.

  A lot of functionality is broken but I like the new direction.

- Changed Thing's search methods, restructured lib. [emsenn]

  I know it looks like a lot of changes but it's really not much.

- Swordsmanship, Healthful, Acting Qualities in Lib. [emsenn]

  A few qualities to make use of the diceroller.

  Not pleased with any of this code but it's better than nothing.

- Merge branch 'feature/noise' into develop. [emsenn]

  Noises basically work, even if their trigger mechanism is a bit simple.

- Failed to add changes to last commit. [emsenn]

  Whooops!

- Fixed Issue #9 & Added Documentation Theme. [emsenn]

  Fixed Issue #9, where clients weren't removed from their location
  when they disconnect.

  Also, added cute little Tumblebeasts to the documentation!

- Additions to Library: Ye Olde Tavern. [emsenn]

  made ye olde tavern less of a filler thing and more of a real thing.

- Documentation for Noisemaker. [emsenn]

- Noisy quality, Noisemaker service. [emsenn]

  Noisy things randomly send messages to things in their environment
  through the Noisemaker service.

  This is a rough draft and probably hella buggy, and also has like NO
  documentation, but hey, it's progress.

- Learning, Teaching Qualities. [emsenn]

  Learning quality which lets things use learn from qualities with the

  Teaching quality which adds qualities in the teacher's
  teachable_qualities to the learner.

- Merge branch 'release/0.0.3' into develop. [emsenn]

  NLTK-based parser, Prehensile, Hearing Qualities, Sender service

0.0.3 (2016-09-16)
------------------

- Missed adding updated __init__.py. [emsenn]

  Forgot to add this to the last commit ffs

- Bumping things up to version 0.0.3. [emsenn]

  Note to self: remember to rebuild documentation during *this* part of
  the release process, not when closing a feature branch.

- Merge branch 'feature/textblob' into develop. [emsenn]

  Fancier parsing, more qualities, expanded library.

- Documentation Update. [emsenn]

  Rebuilt the Sphinx autodocumentation.

- Prehensile Quality, Hearing Quality. [emsenn]

  Fixed adjectives, added a Prehensile quality that lets Things with it
  'take' objects, which moves them from where they are into the contents
  of the prehensile thing.

  Also added the Hearing quality, which lets things listen. Added the
  sounds string to Renderable quality.

- Sender Service, Fixing Commands. [emsenn]

  A lot of commands broke when I set up the new parser, this fixes a fair
  chunk of them, but certainly not all.

  I also created the Sender service, which does basically what the
  Renderer service does. Leaving the Renderer service for now, because it
  will probably be used to format scenes (which maybe should be called
  frames lol) for users.

- Implementing Natural Language Toolkit. [emsenn]

  Changed qtmud.services.Parser to have the parse_line() function, which
  uses the TextBlob package to do some basic parts of speech tagging on
  player lines, to try and suss out what things the player might be
  talking about.

  It's functional in this commit, but uncommented and not fully
  implemented. Check the Sighted quality's look() method for an example
  usage.

- Merge branch 'feature/nametags' into develop. [emsenn]

  The basic nametags code is finished. There's probably some parts of the
  code which don't use it, though, so be careful.

- Applicative Fix. [emsenn]

  After talking with a friend and having the difference between
  applicative and imperative methods explained, made some changes to
  make the applicative methods more, well, applicative. Also fixed some
  older lines that were outdated but not throwing errors.

- Thing.search('target') method. [emsenn]

  Added a simple method for looking around a thing's potential environment
  to find a match for 'target', intended to be a nametag'

- Library Expansion. [emsenn]

  Lots of MUDs let you 'look at <thing in room>', even if that thing isn't a
  real "item", something you can interact with. A cobblestone road might let
  you 'look cobbles', for example, even though you can't do anything beside
  look at the cobbles. Normally this requires a weird archaic syntax to work.

  because of the granular nature of qualities, these fake-but-still-observable
  items are easy to make, by making a new item and applying the "Renderable"
  quality to it.

  The downside is that this means a new thing is instanced for every lookable
  thing in every room, which could cause memory problems down the line.

  However, I think the extensibility and power this gives the engine is way
  worth that potential cost. Normally it's a big commitment in MUD development
  to move a thing from a lookable to a genuine item - normally a complete
  rewrite. In this case, however, it's as simple as
  lookable.add_quality(Physical).

- Better Nametags Documentation. [emsenn]

  Added some notes on how to use nametags

- Implemented Nametags. [emsenn]

  Nametags are a new thing-level attribute, and are used to find a
  thing if you only have some names it might respond to. (For example
  a client has the nametags 'client', 'player', 'thing', and their name
  (if they've set one).

  I also added a __setattr__ function to qtmud.Thing, so that
  qtmud.qualities.Renderable. Essentially, if a thing has a
  set_attr() function, the thing will use that when attr is being
  set, rather than the type default.

- "inventory" Command & Method in Container Quality. [emsenn]

  Added the inventory() method to the Container quality, and changed
  its apply() method to add the 'inventory' command to that container
  if it is also Commandable.

- Never Forget Holiday Update. [emsenn]

  qtmud's first holiday update! Added a memorial to commemorate September
  11th. Also modified the look command so that people can actually look
  at the memorial.

- Merge branch 'master' of github.com:emsenn/qtmud into develop.
  [emsenn]

- Merge branch 'develop' [emsenn]

  Documentation hotfix

- Merge branch 'release/0.0.2' [emsenn]

  continued shifting of core functions, establishment of real
  documentation using Sphinx, and starting to solidify library-building
  API.

- Merge branch 'release/0.0.1' [emsenn]

  First release version, though I use that term very loosely. It should
  run, and the documentation should explain what the code does, but don't
  expect anything close to gameplay.

- Merge branch 'feature/renderer' into develop. [emsenn]

  Set up a renderer service, among other small changes

- Documentation Update. [emsenn]

  Just some documentation expansion before bed.

- Cleaning up Qualities. [emsenn]

  The last commit rolled out changes to the command backend pretty
  quickly. This commit cleans a lot of that up, and expands the new
  Sphinx-friendly docstrings through more of the code.

- Added Scene Rendering. [emsenn]

  Created a new service at qtmud.services.renderer to handle scheduled
  events for sending information to clients. This makes sure clients
  aren't getting messages too soon - such as building a room description
  with 'look' for a room the player just left.

  Currently, only the 'look' function in the Sighted quality makes use
  of render. Other places where things are currently being sent through
  the Client's send() function will be fixed in later commits.

- Documentation Hotfix. [emsenn]

  Documentation wasn't linking to source properly, reworked the
  configuration files so it would.

- Merge branch 'release/0.0.2' into develop. [emsenn]

0.0.2 (2016-09-10)
------------------

- Bump to Version 0.0.2. [emsenn]

  bumped version number everywhere it occurs. (i think)

- Addition of Sphinx-Generated Documentation. [emsenn]

  shuffled documentation around, in part so the repo should (I think)
  work with Github Pages. Even if it doesn't, it's a better presentation
  of the information within the repo.

- Parser & Breaking Up Qualities. [emsenn]

  rewrote qtmud.services.parser.Parser to look for commands in a
  thing's commands attribute, and for the command's functions to
  live in the quality that gives them.

  This meant breaking up the qualities from qualities/__init__.py into
  individual files.

  I also started documenting things using Sphinx markup. The configuration
  files and such have been added to the repo. Going to try and build it
  as our github pages after this commit.

- Merge branch 'feature/environments' into develop. [emsenn]

  A super-simple way of handling things having locations.

- Just Some Comments. [emsenn]

- Rough Environments. [emsenn]

  Clients can now 'look' and 'go' between rooms. Everything is real rough
  but I'm probably taking a break from this code binge so wanted to get it
  committed. It's functional, at least if you don't try to do anything
  outside of documented syntax.

0.0.1 (2016-09-07)
------------------

- Merge branch 'feature/organizing' into develop. [emsenn]

  Finished writing a base I think can be built up from, so closing this
  feature to open ones for specific additions.

- Updated Documentation & Mild Cleanup. [emsenn]

  Mostly just added documentation and cleaned up a few lines, to take
  it from "rough idea" to "workable base".

  Also to play with git flow a bit tbh

- Start of Environments & Movement. [emsenn]

  There is now a Mover service which listens for 'move' events.

  It works against the Room, Container, and Physical Qualities:

  Container - Give a thing contents, a list
  Room - If a thing doesn't have contents, give it contents
      (this'll probably be fleshed out more to have code for in-built
      exits/entrances, which is why I went ahead and did it separate
      from Container.)
  Physical - gives attributes for name, description, and location.

  Now when a client logs in, their associated thing is given the Client
  and Physical qualities, leaving them with connection information, a
  name (for now a synonym for their identity), and moved into
  qtmud.manager.back_room, a lazy little hack to give incoming clients
  someplace to be until there's proper login.

  I also added the whereami command so users can find the name of their
  location.

- Start of Documentation & Say Command. [emsenn]

  Added some linese of documentation in case I put the project down
  for a couple years and don't want to be completely lost when I
  come back.

  Also added a super basic say command, mostly so there's something to
  play with during the next step, adding physical and container qualities

- Basic Schedule Service. [emsenn]

  I haven't fully tested it but qtmud.manager.tick() should call to
  every service, and pass on any 'events' that the service 'subscribed'
  to.

  All I've tested was gettinng it so the Parser service could intercept
  incoming client commands and, well, parse them. Seems to work, but I'm
  sure there's at least a dozen things awfully wrong in it.

- Basic MUDSocket Server. [emsenn]

  a super-basic attempt at a socket server for mud clients (telnet).

  also a few jabs toward implementing a basic schedule caller. doesn't
  do anything yet, but doesn't get in the way.

  next is writing a basic parser and tying it into the scheduler

- Rough Outline. [emsenn]

  This is more of a rough outline of how the engine might be structured.

  It's going to build up Things() with Qualities(), and those will be the
  user and objects around them.

  Going to set up a subscription-based central manager for issuing game
  updates.

- Initial Commit. [emsenn]

  First commit just to set up the git repository.

- Initial commit. [emsenn]


