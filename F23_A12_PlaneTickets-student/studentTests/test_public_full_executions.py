from gradescope_utils.autograder_utils.decorators import number, weight

from StudentSubmission import StudentSubmissionExecutor
from StudentSubmission.Runners import MainModuleRunner
from StudentSubmission.common import PossibleResults
from TestingFramework import BaseTest

class TestPublicFullExecutions(BaseTest):
    DATA_DIRECTORY = "./studentTests/data/files/test_public/"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        StudentSubmissionExecutor.dataDirectory = cls.DATA_DIRECTORY

    def setUp(self) -> None:
        self.executionEnvironment = StudentSubmissionExecutor.generateNewExecutionEnvironment(self.studentSubmission)
        self.runner = MainModuleRunner()


    def tearDown(self) -> None:
        StudentSubmissionExecutor.cleanup(self.executionEnvironment)


    def assertStdIO(self, filename, expected):
        self.executionEnvironment.stdin = [
            filename
        ]

        self.executionEnvironment.files = {
            filename : filename
        }

        StudentSubmissionExecutor.execute(self.executionEnvironment, self.runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.executionEnvironment, PossibleResults.STDOUT)

        self.assertCorrectNumberOfOutputLines(expected, actual)

        self.assertMultiLineEqual(expected[0], actual[0])


    @weight(0.33)
    @number(3.1)
    def test_example_1(self):
        """Full Execution - Example 1"""
        filename = "one_week_1.txt"
        expected = ["10000"]

        self.assertStdIO(filename, expected)
        

    @weight(0.33)
    @number(3.2)
    def test_example_2(self):
        """Full Execution - Example 2"""
        filename = "one_week_2.txt"
        expected = ["81"]

        self.assertStdIO(filename, expected)

    @weight(0.34)
    @number(3.3)
    def test_example_3(self):
        """Full Execution - Example 3"""
        filename = "two_weeks_1.txt"
        expected = ["9005"]

        self.assertStdIO(filename, expected)


    @weight(1)
    @number(4.1)
    def test_varying_pricing_options(self):
        """Full Execution - Various pricing options"""
        filename = "varying_pricing_options.txt"
        expected = ["11118"]

        self.assertStdIO(filename, expected)




