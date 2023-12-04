from gradescope_utils.autograder_utils.decorators import weight, number, visibility

from TestingFramework import BaseTest
from StudentSubmission import StudentSubmissionAssertions
from StudentSubmission import StudentSubmissionExecutor
from StudentSubmission.Runners import MainModuleRunner, FunctionRunner
from StudentSubmission.common import PossibleResults


class RobotMovementPublicTests(BaseTest, StudentSubmissionAssertions):
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

    def assertFunctionIO(self, runner: FunctionRunner, expectedOutput: list[str]):
        StudentSubmissionExecutor.execute(self.executionEnvironment, runner)
        actualOutput = StudentSubmissionExecutor.getOrAssert(self.executionEnvironment, PossibleResults.RETURN_VAL)
        self.assertEqual(expectedOutput, actualOutput)

    @number(1.1)
    @weight(.33)
    @visibility("visible")
    def test_1(self):
        """Example Execution 1"""
        inputs = ["1 0", "2 1", "2 0", "3 0", "3 1"]
        expectedOutput = ["-31.460 71.460 108.385 73.787"]

        self.assertStdIO(inputs, expectedOutput, 1)

    @number(1.2)
    @weight(.33)
    @visibility("visible")
    def test_2(self):
        """Example Execution 2"""
        inputs = ["2 1", "2 0", "3 1", "2 0", "3 1"]
        expectedOutput = ["44.323 3.677 147.359 11.305"]

        self.assertStdIO(inputs, expectedOutput, 1)

    @number(1.3)
    @weight(.34)
    @visibility("visible")
    def test_3(self):
        """Example Execution 3"""
        inputs = ["1 0", "0 1", "2 1", "3 1", "2 0"]
        expectedOutput = ["-1.162 45.162 70.000 7.875"]

        self.assertStdIO(inputs, expectedOutput, 1)

    @number(1.4)
    @weight(.33)
    @visibility("visible")
    def test_4(self):
        """Random Execution 1"""
        inputs = ["1 0", "2 0", "3 1", "4 1", "5 0"]
        expectedOutput = ["8.755 25.245 109.130 45.853"]

        self.assertStdIO(inputs, expectedOutput, 1)

    @number(1.5)
    @weight(.33)
    @visibility("visible")
    def test_5(self):
        """Random Execution 2"""
        inputs = ["-9 0", "8 1", "-7 0", "4 0", "-1 1"]
        expectedOutput = ["25.323 12.677 70.000 73.787"]

        self.assertStdIO(inputs, expectedOutput, 1)

    @number(1.6)
    @weight(.34)
    @visibility("visible")
    def test_6(self):
        """Random Execution 3"""
        inputs = ["10 1", "30 0", "50 1", "70 0", "90 0"]
        expectedOutput = ["595.323 -557.323 70.000 100.000"]

        self.assertStdIO(inputs, expectedOutput, 1)

    @number(1.7)
    @weight(.66)
    def test_7(self):
        """Example Execution 1 - location_decision Function"""

        runner = FunctionRunner("location_decision", 50, 70, 1, [5,5], 0)
        expectedOutput = [-13, 23]

        self.assertFunctionIO(runner, expectedOutput)

    @number(1.8)
    @weight(.67)
    def test_8(self):
        """Example Execution 2 - battery_level_change Function"""

        runner = FunctionRunner("battery_level_change", 30, 8)
        expectedOutput = 1

        self.assertFunctionIO(runner, expectedOutput)

    @number(1.9)
    @weight(.67)
    def test_9(self):
        """Example Execution 3 - heat_change Function"""

        runner = FunctionRunner("heat_change", 100, 10)
        expectedOutput = 123.0

        self.assertFunctionIO(runner, expectedOutput)
