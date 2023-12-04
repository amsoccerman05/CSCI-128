from gradescope_utils.autograder_utils.decorators import weight, number

from TestingFramework import BaseTest
from StudentSubmission import StudentSubmissionExecutor
from StudentSubmission.Runners import MainModuleRunner
from StudentSubmission.common import PossibleResults


class MetalDensitiesPublic(BaseTest):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.runner = MainModuleRunner()

    def setUp(self):
        self.environment = StudentSubmissionExecutor.generateNewExecutionEnvironment(self.studentSubmission)

    # Expect <Metal> <Property> <Value to three decimal places>

    def assertCorrectFormat(self, actualOutput):
        if not isinstance(actualOutput, list):
            actualOutput = actualOutput.split()

        if len(actualOutput) == 3:
            return

        raise AssertionError("Incorrect output format.\n"
                             "Expected: <metal> <property> <value>\n"
                             f"Received: {actualOutput}")

    def assertCorrectOutput(self, expectedOutput, actualOutput):
        self.assertCorrectNumberOfOutputLines(expectedOutput, actualOutput)

        for i in range(len(expectedOutput)):
            splitExpected = expectedOutput[i].split()
            splitActual = actualOutput[i].split()

            self.assertCorrectFormat(actualOutput[i])

            self.assertEquals(
                splitExpected[0] + " " + splitExpected[1],
                splitActual[0] + " " + splitActual[1])

            self.assertAlmostEquals(
                float(splitExpected[2]),
                float(splitActual[2]),
                _delta=.005
            )

    @weight(.33)
    @number(1.1)
    def test_sample_execution_1(self):
        """Sample Execution 1"""

        inputs = [
            "Copper 0010 Aluminum 0100 Silver 1000",
            "Copper",
        ]

        expectedOutput = [
            "Copper Weight 25796289.024",
            "Copper Price 257962890.240",
            "Copper Resistivity 5324539.233",
        ]

        self.environment.stdin = inputs

        StudentSubmissionExecutor.execute(self.environment, self.runner)
        actualOutput = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.STDOUT)
        self.assertCorrectOutput(expectedOutput, actualOutput)

    @number(1.2)
    @weight(0.34)
    def test_sample_execution_2(self):
        """Sample Execution 2"""
        inputs = [
            "Copper 0010 Aluminum 0100 Silver 1000",
            "Aluminum",
        ]

        expectedOutput = [
            "Aluminum Weight 7767748.296",
            "Aluminum Price 776774829.600",
            "Aluminum Resistivity 8390183.034",
        ]

        self.environment.stdin = inputs

        StudentSubmissionExecutor.execute(self.environment, self.runner)
        actualOutput = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.STDOUT)
        self.assertCorrectOutput(expectedOutput, actualOutput)

    @number(1.3)
    @weight(0.33)
    def test_sample_execution_3(self):
        """Sample Execution 3"""
        inputs = [
            "Silver 0034 Copper 0001 Aluminum 0022",
            "Silver"
        ]

        expectedOutput = [
            "Silver Weight 30175288.704",
            "Silver Price 1025959815.936",
            "Silver Resistivity 5082514.722",
        ]

        self.environment.stdin = inputs

        StudentSubmissionExecutor.execute(self.environment, self.runner)
        actualOutput = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.STDOUT)
        self.assertCorrectOutput(expectedOutput, actualOutput)

    @number(2.1)
    @weight(1)
    def test_correct_output_format_1(self):
        """Output has three components"""
        inputs = [
            "Silver 0001 Copper 0001 Aluminum 0001",
            "Copper",
        ]

        self.environment.stdin = inputs

        StudentSubmissionExecutor.execute(self.environment, self.runner)
        actualOutput = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.STDOUT)

        self.assertCorrectNumberOfOutputLines(range(3), actualOutput)
        self.assertCorrectFormat(actualOutput[0])

    @number(2.2)
    @weight(1)
    def test_correct_output_format_2(self):
        """Rounded to correct number of decimal places"""
        inputs = [
            "Silver 0001 Copper 0001 Aluminum 0001",
            "Copper",
        ]

        self.environment.stdin = inputs

        StudentSubmissionExecutor.execute(self.environment, self.runner)
        actualOutput = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.STDOUT)

        self.assertCorrectNumberOfOutputLines(range(3), actualOutput)

        splitLine = actualOutput[0].split()
        decimalIndex = splitLine[2].index('.')

        if len(splitLine[2][decimalIndex + 1:]) != 3:
            raise AssertionError("Incorrect number of decimal places.\n"
                                 "Expected: 3\n"
                                 f"Actual : {len(splitLine[2][decimalIndex + 1:])}\n")

    @number(3.1)
    @weight(1.5)
    def test_zero_price_copper(self):
        """Basic Test: Free Copper"""
        inputs = [
            "Copper 0000 Silver 5100 Aluminum 1029",
            "Copper",
        ]

        expectedOutput = [
            "Copper Weight 25796289.024",
            "Copper Price 0.000",
            "Copper Resistivity 5324539.233",
        ]

        self.environment.stdin = inputs

        StudentSubmissionExecutor.execute(self.environment, self.runner)
        actualOutput = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.STDOUT)
        self.assertCorrectOutput(expectedOutput, actualOutput)

    @number(3.2)
    @weight(1.5)
    def test_high_price_silver(self):
        """Basic Test: Expensive Silver"""
        inputs = [
            "Copper 0000 Silver 9999 Aluminum 1280",
            "Silver"
        ]

        expectedOutput = [
            "Silver Weight 30175288.704",
            "Silver Price 301722711751.296",
            "Silver Resistivity 5082514.722",
        ]

        self.environment.stdin = inputs

        StudentSubmissionExecutor.execute(self.environment, self.runner)
        actualOutput = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.STDOUT)
        self.assertCorrectOutput(expectedOutput, actualOutput)
