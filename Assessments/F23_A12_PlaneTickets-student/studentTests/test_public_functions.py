from unittest import runner
from gradescope_utils.autograder_utils.decorators import number, weight

from StudentSubmission import StudentSubmissionExecutor
from StudentSubmission.Runners import FunctionRunner
from StudentSubmission.common import PossibleResults
from TestingFramework import BaseTest



class TestPublicFunctions(BaseTest):
    DATA_DIRECTORY = "./studentTests/data/files/test_public/"


    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        StudentSubmissionExecutor.dataDirectory = cls.DATA_DIRECTORY

    def setUp(self):
        self.executionEnvironment = StudentSubmissionExecutor.generateNewExecutionEnvironment(self.studentSubmission)


    def tearDown(self) -> None:
        StudentSubmissionExecutor.cleanup(self.executionEnvironment)


    def assertFunctionReturn(self, runner, expected):
        StudentSubmissionExecutor.execute(self.executionEnvironment, runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.executionEnvironment, PossibleResults.RETURN_VAL)

        self.assertEqual(expected, actual)

    @weight(0.5)
    @number(1.1)
    def test_example_1(self):
        """`parse_price_file` - Example 1"""

        self.executionEnvironment.files = {
            "one_week_1.txt": "one_week_1.txt"
        }

        expected = [[["10,999", "100,999", "1000,999"]], 10]

        runner = FunctionRunner("parse_price_file", "one_week_1.txt")

        self.assertFunctionReturn(runner, expected)


    @weight(0.5)
    @number(1.2)
    def test_example_2(self):
        """`parse_price_file`- Example 2"""

        self.executionEnvironment.files = {
            "two_weeks_1.txt": "two_weeks_1.txt"
        }

        expected = [[['375,5', '676,15', '830,6'], ['45,57', '355,20', '575,8']], 13]

        runner = FunctionRunner("parse_price_file", "two_weeks_1.txt")

        self.assertFunctionReturn(runner, expected)

    @weight(0.20)
    @number(1.3)
    def test_example_3(self):
        """`ticket_pricing` - Example 1"""

        priceData = [['10,999', '100,999', '1000,999']]

        runner = FunctionRunner("ticket_pricing", priceData, 1, 5)

        expected = 5000

        self.assertFunctionReturn(runner, expected)

    @weight(0.20)
    @number(1.4)
    def test_example_4(self):
        """`ticket_pricing` - Example 2"""

        priceData = [['375,5', '676,15', '830,6'], ['45,57', '355,20', '575,8']]

        runner = FunctionRunner("ticket_pricing", priceData, 2, 13)

        expected = 9005

        self.assertFunctionReturn(runner, expected)


    @weight(0.20)
    @number(1.5)
    def test_example_5(self):
        """`ticket_pricing` - Example 3"""

        priceData = [['375,5', '676,15', '830,6'], ['45,57', '355,20', '575,8']]

        runner = FunctionRunner("ticket_pricing", priceData, 1, 7)

        expected = 4025

        self.assertFunctionReturn(runner, expected)


    @weight(0.20)
    @number(1.6)
    def test_example_6(self):
        """`ticket_pricing` - Example 4"""
        
        priceData = [['375,5', '676,15', '830,6'], ['45,57', '355,20', '575,8']]

        runner = FunctionRunner("ticket_pricing", priceData, 0, 10000)

        expected = 0

        self.assertFunctionReturn(runner, expected)

    
    @weight(0.20)
    @number(1.7)
    def test_example_7(self):
        """`ticket_pricing` - Example 5"""

        priceData = [['375,5', '676,15', '830,6'], ['45,57', '355,20', '575,8']]

        runner = FunctionRunner("ticket_pricing", priceData, 2, 0)

        expected = 0

        self.assertFunctionReturn(runner, expected)



    @weight(2.0)
    @number(2.1)
    def test_large_number_of_options(self):
        """`ticket_pricing` - Large number of options"""
            
        priceData = [["391,15", "367,1", "416,0", "361,10", "317,15", "428,11", "340,23", "330,14", "351,0", "347,23", "324,11", "429,21", "424,18", "388,3", "392,0"]]
        
        runner = FunctionRunner("ticket_pricing", priceData, 1, 5)

        expected = 2145

        self.assertFunctionReturn(runner, expected)


    @weight(2.0)
    @number(2.2)
    def test_large_number_of_options_and_weeks(self):
        """`ticket_pricing` - Large number of options and weeks"""

        priceData = [
            ["391,15", "367,1", "416,0", "361,10", "317,15", "428,11", "340,23", "330,14", "351,0", "347,23", "324,11", "429,21", "424,18", "388,3", "392,0"],
            ["173,15", "212,12", "90,47", "183,17", "128,23", "155,18", "194,24", "118,30", "226,16", "186,15", "220,18", "176,9", "164,21", "146,18", "116,20"],
            ["112,25", "90,27", "51,1399", "111,27", "51,1388", "98,36", "86,40", "66,104", "109,24", "122,32", "156,14", "97,23", "104,29", "128,13", "215,10"],
            ["205,20", "103,38", "101,41", "130,20", "77,61", "131,17", "57,199", "51,1390", "51,1390", "138,27", "123,32", "113,36", "141,26", "90,45", "109,21"],
            ["69,88", "132,28", "108,30", "129,23", "126,32", "100,26", "61,140", "98,41", "144,20", "132,32", "70,78", "97,43", "89,42", "63,119", "147,23"],
        ]

        runner = FunctionRunner("ticket_pricing", priceData, 5, 19)

        expected = 8151 

        self.assertFunctionReturn(runner, expected)

    @weight(2.0)
    @number(2.3)
    def test_varying_number_of_options(self):
        """`ticket_pricing` - Varying number of options per week"""

        priceData = [
            ["479,18", "352,9", "456,9"],
            ["174,21", "245,22"],
            ["82,44"],
        ]

        runner = FunctionRunner("ticket_pricing", priceData, 3, 27)

        expected = 10827 

        self.assertFunctionReturn(runner, expected)


    @weight(2.0)
    @number(2.4)
    def test_recursion_limit(self):
        """`ticket_pricing` - Large recusion depth"""
        
        priceData = [
            ["1069,0", "1000,10", "1071,13", "1042,9", "1013,11", "1089,12", "1103,0", "997,0", "977,2", "992,0", "1038,3", "997,0", "970,1", "975,0", "1073,9", "1005,0", "974,1", "1051,10", "1053,3", "1014,7", "1036,15", "1097,5", "1047,7", "1089,0", "1017,0"],
            ["455,10", "436,15", "609,11", "636,13", "540,6", "510,11", "591,1", "542,6", "543,6", "484,6", "538,4", "581,8", "434,0", "504,0", "617,0", "516,0", "507,0", "550,10", "513,0", "521,1", "518,8", "499,10", "509,6", "553,5", "458,1"],
            ["416,7", "351,17", "336,0", "272,17", "373,6", "309,3", "294,22", "373,20", "314,0", "255,7", "393,8", "274,19", "419,6", "328,2", "415,0", "398,15", "330,13", "409,7", "424,15", "336,5", "392,12", "415,7", "403,14", "372,7", "419,21"],
            ["214,12", "220,0", "182,21", "206,15", "160,10", "268,13", "197,8", "207,18", "221,33", "226,19", "169,17", "167,23", "280,10", "259,4", "239,6", "231,15", "251,16", "283,2", "183,17", "227,14", "228,17", "202,14", "181,10", "232,9", "144,24"],
            ["174,10", "253,8", "180,2", "187,16", "133,32", "102,33", "172,2", "210,1", "254,19", "206,16", "300,0", "181,20", "212,15", "185,17", "233,12", "255,0", "243,5", "178,12", "259,6", "178,19", "221,5", "211,24", "187,14", "262,7", "129,23"],
        ]

        runner = FunctionRunner("ticket_pricing", priceData, 5, 300)

        self.executionEnvironment.timeout = 20

        expected = 44964

        self.assertFunctionReturn(runner, expected)







    
