import unittest
import main1


class Test(unittest.TestCase):
    def test(self):
#        answer = {'OUTPUT': [{'region': 'New York', 'total_cost': 11000, 'machines': [('8XLarge', 1), ('2XLarge', 1), ('XLarge', 1), ('Large', 1)]}, {'region': 'India', 'total_cost': 10665, 'machines': [('8XLarge', 1), ('2XLarge', 1), ('Large', 3)]}, {'region': 'China', 'total_cost': 9450, 'machines': [('8XLarge', 1), ('XLarge', 3), ('Large', 1)]}]}
        answer = {'OUTPUT': [{'region': 'New York', 'total_cost': 10150, 'machines': [('8XLarge', 7),('XLarge', 1), ('Large', 1)]}, {'region': 'India', 'total_cost': 9520, 'machines': [('8XLarge', 7), ('Large', 3)]}, {'region': 'China', 'total_cost': 8570, 'machines': [('8XLarge', 7), ('XLarge', 1), ('Large', 1)]}]}

        predict = main1.Cost(1150, 1)

        self.assertEqual(answer, predict)
        OUTPUT_FILE = ''
        OUTPUT_FILE += '\n\n' + "ANSWER: " + str(answer) +'\n'
        OUTPUT_FILE += '\n\n' + 'PREDICT: ' + str(predict) + '\n'
        print(OUTPUT_FILE)
        with open('test.txt','w') as file:
            file.write(OUTPUT_FILE)


if __name__ == '__main__':
    unittest.main()