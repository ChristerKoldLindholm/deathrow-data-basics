import unittest
import deathrow
import csv

class TestDeathrow(unittest.TestCase):
    def test_get_data(self):
        self.assertEqual(deathrow.get_data()[0]['Execution'], '553')
    
    def test_to_metric(self):
        self.assertEqual(deathrow.to_metric(deathrow.get_data())[0]['Weight'], '98.0 kg')
        # Tests if original data set is preserved after to_metric.
        self.assertEqual(deathrow.get_data()[0]['Height'], '6\' 1"')

    def test_county_statistics(self):
        self.assertEqual(len(deathrow.county_statistics(deathrow.get_data()))
        , 92)

    def test_native_statistics(self):
        self.assertEqual(len(deathrow.native_statistics(deathrow.get_data()))
        , 219)

    def test_last_words_search(self):
        self.assertEqual(deathrow.last_words_search(
            deathrow.get_data(), ['burns', 'soldier'])
            , [('Erick Daniel', '1987-04-04', "Yes, I would like to say nephew it burns huh. You know I might have lost the fight but I'm still a soldier. I still love you all. To my supporters and family y'all hold it down. Ten Toes down right. That's all.")]
            )

if __name__ == '__main__':
    unittest.main()


