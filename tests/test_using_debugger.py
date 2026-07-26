import unittest

def silly_things(things):
    sillier_things = []

    for thing in things:
        sillier_things.append("silly " + str(thing))

    return sillier_things


class TestUsingDebugger(unittest.TestCase):
    def test_silly_thing(self):
        things = [
                "rabbit",
                "kitten",
                "duck",
                27,
                "",
        ]
        sillier_things = silly_things(things)
        self.assertEqual(sillier_things[2], "silly duck")
