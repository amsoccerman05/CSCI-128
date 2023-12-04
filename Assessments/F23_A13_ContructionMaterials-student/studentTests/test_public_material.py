from gradescope_utils.autograder_utils.decorators import weight, number

from StudentSubmission import StudentSubmissionExecutor
from StudentSubmission.common import PossibleResults
from test_public_common import ClassRunner
from TestingFramework import BaseTest


class TestMaterial(BaseTest):
    DATA_DIRECTORY = "./studentTests/data/files/test_public/"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        StudentSubmissionExecutor.dataDirectory = cls.DATA_DIRECTORY
        cls.RESULT_CLASS = ClassRunner.EXPECTED_CLASS_NAME
    
    def setUp(self) -> None:
        self.environment = StudentSubmissionExecutor.generateNewExecutionEnvironment(self.studentSubmission)
        self.environment.timeout = 1
        self.runner = ClassRunner()

    def tearDown(self) -> None:
        StudentSubmissionExecutor.cleanup(self.environment)


    @weight(.5)
    @number(1.1)
    def test_initalization(self):
        """`Material Class` - Initalization"""

        ID = 54321
        # this is really bad practice. my own smooth brainness is the reason we have to do this :(
        # i really hate this. This needs to be fixed for future semesters.
        code = f"mat = Material({ID}); {self.RESULT_CLASS} = mat.getID()"

        self.runner.setSetupCode(code)

        StudentSubmissionExecutor.execute(self.environment, self.runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.RETURN_VAL)

        self.assertEqual(ID, actual)


    @weight(.5)
    @number(1.2)
    def test_set_price(self):
        """`Material Class` - Set Price"""
            
        PRICE = 100
        code = f"mat = Material(0); mat.setPrice({PRICE}); {self.RESULT_CLASS} = mat.getPrice()"

        self.runner.setSetupCode(code)

        StudentSubmissionExecutor.execute(self.environment, self.runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.RETURN_VAL)

        self.assertEqual(PRICE, actual)


    @weight(.5)
    @number(1.3)
    def test_set_material_type(self):
        """`Material Class` - Set Material"""
        MATERIAL = "WOOD"

        code = f"mat = Material(0); mat.setMaterialType('{MATERIAL}'); {self.RESULT_CLASS} = mat.getMaterialType()"

        self.runner.setSetupCode(code)

        StudentSubmissionExecutor.execute(self.environment, self.runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.RETURN_VAL)

        self.assertEqual(MATERIAL, actual)


    @weight(.5)
    @number(1.4)
    def test_type_is_not_determined(self):
        """`Material Class` - MaterialType is Not Determined when unset"""

        expected = "Not Determined"
        
        code = f"mat = Material(0); {self.RESULT_CLASS} = mat.getMaterialType()"

        self.runner.setSetupCode(code)

        StudentSubmissionExecutor.execute(self.environment, self.runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.RETURN_VAL)

        self.assertEqual(expected, actual)


    @weight(1)
    @number(1.5) 
    def test_example_1(self):
        """`Material Class` - Example Execution 1"""

        code = "mat = Material(1)\n"\
            "print('OUTPUT', mat.getPrice())\n"\
            "print('OUTPUT', mat.getMaterialType())\n"\
            "print('OUTPUT', mat.getID())"


        expected = [
            "0",
            "Not Determined",
            "1",
        ]

        self.runner.setSetupCode(code)

        StudentSubmissionExecutor.execute(self.environment, self.runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.STDOUT)

        self.assertCorrectNumberOfOutputLines(expected, actual)

        self.assertEqual(expected, actual)


    @weight(1)
    @number(1.6)
    def test_example_2(self):
        """`Material Class` - Example Execution 2"""

        code = "mat = Material(23)\n"\
            "mat.setPrice(1000)\n"\
            "mat.setMaterialType('WOOD')\n"\
            "mat.setID(999)\n"\
            "print('OUTPUT', mat.getPrice())\n"\
            "print('OUTPUT', mat.getMaterialType())\n"\
            "print('OUTPUT', mat.getID())"

        expected = [
            "1000",
            "WOOD",
            "999",
        ]

        self.runner.setSetupCode(code)

        StudentSubmissionExecutor.execute(self.environment, self.runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.STDOUT)

        self.assertCorrectNumberOfOutputLines(expected, actual)

        self.assertEqual(expected, actual)



    


