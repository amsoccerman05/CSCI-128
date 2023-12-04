from gradescope_utils.autograder_utils.decorators import weight, number, visibility

from TestingFramework import BaseTest
from StudentSubmission import StudentSubmissionAssertions
from StudentSubmission import StudentSubmissionExecutor
from StudentSubmission.Runners import MainModuleRunner
from StudentSubmission.common import PossibleResults


class InvestmentPublicTests(BaseTest, StudentSubmissionAssertions):
    def setUp(self):
        self.executionEnvironment = StudentSubmissionExecutor.generateNewExecutionEnvironment(self.studentSubmission)
        self.runner = MainModuleRunner()

    def tearDown(self):
        StudentSubmissionExecutor.cleanup(self.executionEnvironment)

    def assertStdIO(self, inputs: list[str], expectedOutput: list[str], timeout: int):
        self.executionEnvironment.stdin = inputs
        self.executionEnvironment.timeout = timeout
        StudentSubmissionExecutor.execute(self.executionEnvironment, self.runner)

        actualOutput = StudentSubmissionExecutor.getOrAssert(self.executionEnvironment, PossibleResults.STDOUT)
        self.assertCorrectNumberOfOutputLines(expectedOutput, actualOutput)

        self.assertEquals(self.reformatOutput(expectedOutput), self.reformatOutput(actualOutput))

    @number(1.1)
    @weight(.34)
    @visibility("visible")
    def test_1(self):
        """Example Execution 1"""
        inputs = ["abc", "120", "0.003", "1"]
        expectedOutput = ["289236.56"]

        self.assertStdIO(inputs, expectedOutput, 1)

    @number(1.2)
    @weight(.33)
    @visibility("visible")
    def test_2(self):
        """Example Execution 2"""
        inputs = ["dull", "1", "0.003", "2"]
        expectedOutput = ["2000.00"]

        self.assertStdIO(inputs, expectedOutput, 1)

    @number(1.3)
    @weight(.33)
    @visibility("visible")
    def test_3(self):
        """Example Execution 3"""
        inputs = ["jackpot", "12", "0.02", "3"]
        expectedOutput = ["74284.56"]

        self.assertStdIO(inputs, expectedOutput, 1)

    @number(1.4)
    @weight(.33)
    @visibility("visible")
    def test_4(self):
        """Savings One Month"""
        inputs = ["abcdef", "1", "0.07", "1"]
        expectedOutput = ["2140.00"]

        self.assertStdIO(inputs, expectedOutput, 1)

    @number(1.5)
    @weight(.33)
    @visibility("visible")
    def test_5(self):
        """Fund One Month"""
        inputs = ["abcdef", "1", "0.07", "2"]
        expectedOutput = ["2000.00"]

        self.assertStdIO(inputs, expectedOutput, 1)

    @number(1.6)
    @weight(.34)
    @visibility("visible")
    def test_6(self):
        """Gambling One Month"""
        inputs = ["abcdef", "1", "0.07", "3"]
        expectedOutput = ["0.00"]

        self.assertStdIO(inputs, expectedOutput, 1)

    @number(1.7)
    @weight(.33)
    @visibility("visible")
    def test_7(self):
        """Savings Random"""
        inputs = ["hello", "4", "0.09", "1"]
        expectedOutput = ["9969.42"]

        self.assertStdIO(inputs, expectedOutput, 1)

    @number(1.8)
    @weight(.33)
    @visibility("visible")
    def test_8(self):
        """Fund Random"""
        inputs = ["somecoolseed", "9", "0.5", "2"]
        expectedOutput = ["18035.96"]

        self.assertStdIO(inputs, expectedOutput, 1)

    @number(1.9)
    @weight(.34)
    @visibility("visible")
    def test_9(self):
        """Gambling Random"""
        inputs = ["gonebust", "5", "0.9", "3"]
        expectedOutput = ["0.00"]

        self.assertStdIO(inputs, expectedOutput, 1)
