from gradescope_utils.autograder_utils.decorators import weight, number

from StudentSubmission import StudentSubmissionExecutor
from StudentSubmission.common import PossibleResults
from TestingFramework import BaseTest
from StudentSubmission.Runners import MainModuleRunner

class TestFullExecutions(BaseTest):
    DATA_DIRECTORY = "./studentTests/data/files/test_public/"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        StudentSubmissionExecutor.dataDirectory = cls.DATA_DIRECTORY
    
    def setUp(self) -> None:
        self.environment = StudentSubmissionExecutor.generateNewExecutionEnvironment(self.studentSubmission)
        self.environment.timeout = 1
        self.runner = MainModuleRunner()

    def tearDown(self) -> None:
        StudentSubmissionExecutor.cleanup(self.environment)


    def assertStdio(self, stdin, expected):
        self.environment.stdin = stdin

        StudentSubmissionExecutor.execute(self.environment, self.runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.STDOUT)

        self.assertCorrectNumberOfOutputLines(expected, actual)

        for i in range(len(expected)):
            self.assertEqual(expected[i], actual[i], msg=f"Failed on output line {i+1} of {len(expected)}")

    @weight(1)
    @number(3.1)
    def test_example_1(self):
        """`Full Execution` - Example 1"""

        self.environment.files = {
            "materialList.txt": "materialList.txt"
        }

        stdin = [
            "Beck",
            "Golden",
            "materialList.txt",
        ]

        expected = [
            "Beck site in Golden has 19 materials, with a value of 549.",
            "WOOD:7 STEEL:6 BRICK:6",
        ]

        self.assertStdio(stdin, expected)


    @weight(1)
    @number(3.2)
    def test_example_2(self):
        """`Full Execution` - Example 2"""

        self.environment.files = {
            "mat1.txt": "mat1.txt"
        }

        stdin = [
            "Bloom",
            "Arvada",
            "mat1.txt",
        ]

        expected = [
            "Bloom site in Arvada has 333 materials, with a value of 164160.",
            "WOOD:105 STEEL:119 BRICK:109",
        ]

        self.assertStdio(stdin, expected)


    @weight(1)
    @number(3.3)
    def test_example_3(self):
        """`Full Execution` - Example 3"""

        self.environment.files = {
            "long.txt": "long.txt"
        }

        self.environment.timeout = 3

        stdin = [
            "Crazy",
            "Longmont",
            "long.txt",
        ]

        expected = [
            "Crazy site in Longmont has 100000 materials, with a value of 49993483.",
            "WOOD:33361 STEEL:33350 BRICK:33289",
        ]

        self.assertStdio(stdin, expected)
