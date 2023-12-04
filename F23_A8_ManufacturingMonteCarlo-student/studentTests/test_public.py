from gradescope_utils.autograder_utils.decorators import number, weight

from StudentSubmission import StudentSubmissionExecutor
from StudentSubmission.common import PossibleResults
from StudentSubmission.Runners import MainModuleRunner
from TestingFramework import BaseTest


class TestPublicSimulation(BaseTest):
    def setUp(self) -> None:
        self.executionEnvironment = StudentSubmissionExecutor.generateNewExecutionEnvironment(self.studentSubmission)
        self.executionEnvironment.timeout = 1
        self.runner = MainModuleRunner()

    def tearDown(self) -> None:
        StudentSubmissionExecutor.cleanup(self.executionEnvironment)

    def assertStdIO(self, inputs: list[str], expected: str):
        self.executionEnvironment.stdin = inputs

        StudentSubmissionExecutor.execute(self.executionEnvironment, self.runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.executionEnvironment, PossibleResults.STDOUT)

        self.assertCorrectNumberOfOutputLines([expected], actual)

        self.assertEqual(expected, actual[0], msg="Failed on output line 1")

    @weight(.33)
    @number(1.3)
    def test_sample_1(self):
        """Full Execution - Example Execution 1"""
        stdin = [
            "10000 abc",
            "3 0.09",
            "22.5 0.03",
            "0.3 0.6",
        ]

        expected = "0.08"

        self.assertStdIO(stdin, expected)

    @weight(.33)
    @number(1.4)
    def test_sample_2(self):
        """Full Execution - Example Execution 2"""
        stdin = [
            "1 one",
            "3 0.09",
            "22.5 0.03",
            "0.3 0.6"
        ]

        expected = "0.00"
        self.assertStdIO(stdin, expected)

    @weight(.34)
    @number(1.5)
    def test_sample_3(self):
        """Full Execution - Example Execution 3"""
        stdin = [
            "10000 smaller",
            "3 0.09",
            "22.5 0.03",
            "0.4 0.5",
        ]

        expected = "49.46"
        self.assertStdIO(stdin, expected)

    @weight(1.5)
    @number(3.1)
    def test_very_long_cycle_1(self):
        """Full Execution - Very long cycle - mostly failures"""
        stdin = [
            "1000000 longboi",
            "3 0.04",
            "22.25 0.03",
            "0.3 0.6",
        ]

        expected = "99.87"
        # increase timelimit for this test be it's a bit... long
        self.executionEnvironment.timeout = 60
        self.assertStdIO(stdin, expected)

    @weight(1.5)
    @number(3.2)
    def test_very_long_cycle_2(self):
        """Full Execution - Very long cycle - no failures"""
        stdin = [
            "1000000 longboi",
            "3 0",
            "22 0",
            "0.0 0.0",
        ]

        expected = "0.00"
        self.executionEnvironment.timeout = 60
        self.assertStdIO(stdin, expected)
