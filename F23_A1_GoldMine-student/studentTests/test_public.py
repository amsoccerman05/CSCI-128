from gradescope_utils.autograder_utils.decorators import weight, number, visibility

from StudentSubmission.Runners import MainModuleRunner
from StudentSubmission.common import PossibleResults
from TestingFramework import BaseTest
from StudentSubmission import StudentSubmissionAssertions, StudentSubmissionExecutor


class GoldmineStdIOTests(BaseTest, StudentSubmissionAssertions):

    def setUp(self):
        self.runner = MainModuleRunner()
        self.executionEnvironment = StudentSubmissionExecutor.generateNewExecutionEnvironment(self.studentSubmission)

    def tearDown(self):
        StudentSubmissionExecutor.cleanup(self.executionEnvironment)

    def assertStdIO(self, inputs: list[str], expectedOutput: list[str], timeout: int):
        self.executionEnvironment.stdin = inputs
        self.executionEnvironment.timeout = timeout
        StudentSubmissionExecutor.execute(self.executionEnvironment, self.runner)
        actualOutput = StudentSubmissionExecutor.getOrAssert(self.executionEnvironment, PossibleResults.STDOUT)

        self.assertEquals(self.reformatOutput([expectedOutput[0]]), self.reformatOutput([actualOutput[0]]))

        for i, el in enumerate(expectedOutput):
            if i == 0:
                continue
            # Account for rounding errors
            self.assertAlmostEquals(float(el), float(actualOutput[i]), _delta=.025)

    @number(1.1)
    @weight(.5)
    @visibility("visible")
    def test_sampleExecutionOne(self):
        """Cripple Creek: Sample Execution One"""

        inputs = ["Cripple Creek", "2200"]

        expectedOutput = ["Investment Planning Report of Cripple Creek Mine in Colorado Springs",
                          "676934744.2680776",
                          "12840764885.361553",
                          "20702916560.84656"]

        self.assertStdIO(inputs, expectedOutput, 1)

    @number(1.2)
    @weight(.5)
    @visibility("visible")
    def test_sampleExecutionTwo(self):
        """Cripple Creek: Sample Execution Two"""

        inputs = ["Cripple Creek", "1000"]

        expectedOutput = ["Investment Planning Report of Cripple Creek Mine in Colorado Springs",
                          "234606701.94003528",
                          "3994204038.800706",
                          "6106091164.021164"]

        self.assertStdIO(inputs, expectedOutput, 1)

    @number(2.1)
    @weight(1)
    @visibility("visible")
    def test_negativeFortyYearROI(self):
        """Singpora Springs: Negative 40 Year ROI"""

        inputs = ["Singpora Springs", "489"]

        expectedOutput = ["Investment Planning Report of Singpora Springs Mine in Colorado Springs",
                          "46248677.24867725",
                          "227043544.97354507",
                          "-109723650.79365039"]

        self.assertStdIO(inputs, expectedOutput, 1)

    @number(2.2)
    @weight(1)
    @visibility("visible")
    def test_negativeTwentyYearROI(self):
        """Victor Mine: Negative 20 Year ROI"""

        inputs = ["Victor", "402"]

        expectedOutput = ["Investment Planning Report of Victor Mine in Colorado Springs",
                          "14179894.17989418",
                          "-414332116.4021164",
                          "-1167993492.0634918"]

        self.assertStdIO(inputs, expectedOutput, 1)

    @number(3.1)
    @weight(2)
    @visibility("visible")
    def test_positiveStarWars(self):
        """In a galaxy far, far away: Positive ROI"""

        inputs = ["In a galaxy far far away", "1000"]

        expectedOutput = ["Investment Planning Report of In a galaxy far far away Mine in Colorado Springs",
                          "234606701.94003528",
                          "3994204038.800706",
                          "6106091164.021164"]

        self.assertStdIO(inputs, expectedOutput, 1)

    @number(3.2)
    @weight(2)
    @visibility("visible")
    def test_negativeStarWars(self):
        """In a galaxy far, far away: Negative ROI"""

        inputs = ["In a galaxy far far away", "100"]

        expectedOutput = ["Investment Planning Report of In a galaxy far far away Mine in Colorado Springs",
                          "-97139329.80599648",
                          "-2640716596.1199293",
                          "-4841527883.597883"]

        self.assertStdIO(inputs, expectedOutput, 1)
