from gradescope_utils.autograder_utils.decorators import weight, number
from TestingFramework import BaseTest
from StudentSubmission import StudentSubmissionExecutor
from StudentSubmission.Runners import FunctionRunner
from StudentSubmission.common import PossibleResults


class TestPublicSimulateFunction(BaseTest):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # to the students who are reading this file, this is terrible practice.
        # don't write dynamic code unless you absolutely have to.
        # in this case, this is the only way to seed the random number generator for your random.normalvarient in the
        # simulate function with the way that the autograder runs your functions
        cls.setupCode = \
            "def autograder_setup():\n" \
            "   random.seed('abc')\n"

    def setUp(self) -> None:
        self.executionEnvironment = StudentSubmissionExecutor.generateNewExecutionEnvironment(self.studentSubmission)
        self.executionEnvironment.timeout = 1

    def tearDown(self) -> None:
        StudentSubmissionExecutor.cleanup(self.executionEnvironment)

    def assertFunctionExecution(self, expectedOutput: bool, *args):
        runner = FunctionRunner("simulate", *args)
        runner.setSetupCode(self.setupCode)

        StudentSubmissionExecutor.execute(self.executionEnvironment, runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.executionEnvironment, PossibleResults.RETURN_VAL)

        if expectedOutput == actual:
            return

        msg = f"Expected: simulate{args} => {expectedOutput}\n" \
              f"Actual  : simulate{args} => {actual}"

        raise AssertionError(msg)

    @weight(.5)
    @number(1.1)
    def test_sample_1(self):
        """`simulate` - Example Execution 1"""
        args = (
            3, 0.09,
            22.5, 0.03,
            0.3, 0.6
        )

        expected = True
        self.assertFunctionExecution(expected, *args)

    @weight(.5)
    @number(1.2)
    def test_sample_2(self):
        """`simulate` - Example Execution 2"""

        args = (
            3, 0.09,
            22.5, 0.03,
            0.4, 0.5
        )

        expected = False
        self.assertFunctionExecution(expected, *args)

    @weight(1)
    @number(2.2)
    def test_no_oring_variation_1(self):
        """`simulate` - No o-ring variation 1"""
        args = (
            3, 0,
            22.5, 0.01,
            0.4, 0.6
        )

        expected = True
        self.assertFunctionExecution(expected, *args)

    @weight(1)
    @number(2.2)
    def test_no_oring_variation_2(self):
        """`simulate` - No o-ring variation 2"""
        args = (
            1, 0,
            24, 0.02,
            0.0, 0.15
        )

        expected = True
        self.assertFunctionExecution(expected, *args)

    @weight(1.34)
    @number(2.3)
    def test_no_variation(self):
        """`simulate` - No variation"""
        args = (
            5, 0,
            20, 0,
            0.0, 0.0
        )

        # If you are failing this test, make sure your allowed ranges are inclusive

        expected = True
        self.assertFunctionExecution(expected, *args)

    @weight(1.33)
    @number(2.4)
    def test_very_small_oring(self):
        """`simulate` - Very small o-ring"""
        args = (
            0.01, 0,
            25, 0,
            0.0, .02
        )

        expected = True
        self.assertFunctionExecution(expected, *args)

    @weight(1.33)
    @number(2.5)
    def test_very_small_piston_groove(self):
        """`simulate` - very small piston groove"""
        args = (
            25, 0,
            .25, .125,
            0.2, .3
        )

        expected = True
        self.assertFunctionExecution(expected, *args)

