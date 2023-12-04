from gradescope_utils.autograder_utils.decorators import weight, number

from StudentSubmission import StudentSubmissionExecutor
from StudentSubmission.common import PossibleResults
from test_public_common import ClassRunner
from TestingFramework import BaseTest


class TestConstructionSite(BaseTest):
    DATA_DIRECTORY = "./studentTests/data/test_public/"

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
    
    @weight(1.0)
    @number(2.1)
    def test_initalization(self):
        """`ConstructionSite` - Initalization"""

        code = f"site = ConstructionSite('a', 'b');{self.RESULT_CLASS} = site.findMaterial(10)"
        expected = -1

        self.runner.setSetupCode(code)

        StudentSubmissionExecutor.execute(self.environment, self.runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.RETURN_VAL)

        self.assertEqual(expected, actual)

    @weight(1.0)
    @number(2.2)
    def test_add_material(self):
        """`ConstructionSite` - Add Material"""

        ID = 1001
        code = f"mat = Material({ID});site = ConstructionSite('a', 'b');"\
                f"site.addMaterial(mat);{self.RESULT_CLASS} = site.findMaterial({ID}).getID()"

        self.runner.setSetupCode(code)

        StudentSubmissionExecutor.execute(self.environment, self.runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.RETURN_VAL)

        self.assertEqual(ID, actual)


    @weight(1.0)
    @number(2.3)
    def test_caculate_price(self):
        """`ConstructionSite` - Calculate Price"""

        code = f"site = ConstructionSite('a', 'b');{self.RESULT_CLASS} = site.calculatePrice()"

        self.runner.setSetupCode(code)

        StudentSubmissionExecutor.execute(self.environment, self.runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.RETURN_VAL)

        self.assertIsNone(actual)


    @weight(1.0)
    @number(2.4)
    def test_count_materials(self):
        """`ConstructionSite` - Count Materials"""
        code = f"matTypes = ['WOOD', 'WOOD', 'WOOD', 'BRICK']\n"\
               f"mats = [Material(i) for i in range(len(matTypes))]\n"\
               f"for i, el in enumerate(mats):\n"\
               f"  el.setMaterialType(matTypes[i])\n"\
               f"site = ConstructionSite('a','b')\n"\
               f"for el in mats:\n"\
               f"  site.addMaterial(el)\n"\
               f"{self.RESULT_CLASS} = site.countMaterials()"
        
        expected = [3, 0, 1]
        self.runner.setSetupCode(code)

        StudentSubmissionExecutor.execute(self.environment, self.runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.RETURN_VAL)

        self.assertEqual(expected, actual)

    
    @weight(.5)
    @number(2.5)
    def test_example_1(self): 
        """`ConstructionSite` - Example 1"""

        code = ""\
            "site = ConstructionSite('Colorado School of Memes', 'Golden')\n"\
            "print('OUTPUT', site)"

        expected = ["Colorado School of Memes site in Golden has 0 materials, with a value of 0."]


        self.runner.setSetupCode(code)

        StudentSubmissionExecutor.execute(self.environment, self.runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.STDOUT)

        self.assertCorrectNumberOfOutputLines(expected, actual)

        self.assertEqual(expected, actual)


        
    @weight(0.5)
    @number(2.6)
    def test_example_2(self):
        """`ConstructionSite` - Example 2"""
        code = ""\
            "site = ConstructionSite('New York', 'New York')\n"\
            "mat = Material(12)\n"\
            "mat.setMaterialType('STEEL')\n"\
            "mat.setPrice(10000)\n"\
            "site.addMaterial(mat)\n"\
            "print('OUTPUT', site.findMaterial(7))\n"\
            "print('OUTPUT', site.findMaterial(12) == mat)"

        expected = [
            "-1",
            "True",
        ]

        self.runner.setSetupCode(code)

        StudentSubmissionExecutor.execute(self.environment, self.runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.STDOUT)

        self.assertCorrectNumberOfOutputLines(expected, actual)

        self.assertEqual(expected, actual)
        

    @weight(0.5)
    @number(2.7)
    def test_example_3(self):
        """`ConstructionSite` - Example 3"""

        code = ""\
            "site = ConstructionSite('New York', 'New York')\n"\
            "mat = Material(12)\n"\
            "mat.setMaterialType('STEEL')\n"\
            "mat.setPrice(10000)\n"\
            "site.addMaterial(mat)\n"\
            "print('OUTPUT', site.countMaterials())"

        expected = [
            "[0, 1, 0]"
        ]

        self.runner.setSetupCode(code)

        StudentSubmissionExecutor.execute(self.environment, self.runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.STDOUT)

        self.assertCorrectNumberOfOutputLines(expected, actual)

        self.assertEqual(expected, actual)

    @weight(0.5)
    @number(2.8)
    def test_example_4(self):
        """`ConstructionSite` - Example 4"""

        code = ""\
            "site = ConstructionSite('New York', 'New York')\n"\
            "mat = Material(12)\n"\
            "mat.setMaterialType('STEEL')\n"\
            "mat.setPrice(10000)\n"\
            "site.addMaterial(mat)\n"\
            "site.calculatePrice()\n"\
            "print('OUTPUT', site)"

        expected = [
            "New York site in New York has 1 materials, with a value of 10000."
        ]

        self.runner.setSetupCode(code)

        StudentSubmissionExecutor.execute(self.environment, self.runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.STDOUT)

        self.assertCorrectNumberOfOutputLines(expected, actual)

        self.assertEqual(expected, actual)
