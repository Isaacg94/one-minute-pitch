import unittest
from app.models import Pitch

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Pitch(1,'Ransom','Lyric','I got black, I got white, what you want?')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))


