import unittest
from my_lambdata.assignment1 import WrangledFrame


class TestWrangledFrame(unittest.TestCase):

    def test_add_state_names(self):
        wf = WrangledFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
        # ensure the WF only has a column "abbrev"
        self.assertEqual(list(wf.columns), ['abbrev'])
        self.assertEqual(len(list(wf.columns)), 1)
        wf.add_state_names()
        # ensure there are only "abbrev" and "name" column
        self.assertEqual(list(wf.columns), ['abbrev', 'name'])
        self.assertEqual(len(list(wf.columns)), 2)
        # ensure the values of WF are specific classes / values
        self.assertEqual(wf['name'][0], 'Cali')
        self.assertEqual(wf['abbrev'][0], 'CA')


if __name__ == '__main__':
    unittest.main()
