import sys

from gradescope_utils.autograder_utils.decorators import weight, number, visibility

from TestingFramework import BaseTest
from StudentSubmission import StudentSubmissionAssertions
from StudentSubmission import StudentSubmissionExecutor
from StudentSubmission.Runners import MainModuleRunner
from StudentSubmission.common import PossibleResults


class BloodBankPublicTests(BaseTest, StudentSubmissionAssertions):
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

        self.assertCorrectNumberOfOutputLines(expectedOutput, actualOutput)

        for i, expectedOutputLine in enumerate(expectedOutput):
            self.assertEquals(expectedOutputLine, actualOutput[i],
                              msg=f"Failed on line {i + 1} of {len(expectedOutput)}")

    @number(1.1)
    @weight(0.5)
    def test_sample_1(self):
        """Sample Execution 1"""
        inputs = ["PSPSPSPS", "ISISISPP", "AB-"]
        expectedOutput = ["AB- in the primary blood bank stocks is plenty.",
                          "AB- in the secondary blood bank stocks is plenty."]
        self.assertStdIO(inputs, expectedOutput, 1)

    @number(1.2)
    @weight(0.5)
    def test_sample_2(self):
        """Sample Execution 2"""
        inputs = ["PSIIPSPP", "SPSPPPII", "A-"]
        expectedOutput = ["A- in the primary blood bank stocks is insufficient.",
                          "A- in the secondary blood bank stocks is scarce."]
        self.assertStdIO(inputs, expectedOutput, 1)

    @number(2.1)
    @weight(1.0)
    @visibility("visible")
    def test_1(self):
        """Test 1: A-"""
        inputs = ["PSIIPSPP", "SPSPPPII", "A-"]
        expectedOutput = ["A- in the primary blood bank stocks is insufficient.",
                          "A- in the secondary blood bank stocks is scarce."]
        self.assertStdIO(inputs, expectedOutput, 1)

    @number(2.2)
    @weight(2.0)
    @visibility("visible")
    def test_2(self):
        """Test 2: AB+"""
        inputs = ["PPPPSSSS", "IIIISSSS", "AB+"]
        expectedOutput = ["AB+ in the primary blood bank stocks is scarce.",
                          "AB+ in the secondary blood bank stocks is scarce."]
        self.assertStdIO(inputs, expectedOutput, 1)

    @number(2.3)
    @weight(2.0)
    @visibility("visible")
    def test_3(self):
        """Test 3: O+"""
        inputs = ["PPPPPPPP", "IIIIIIII", "O+"]
        expectedOutput = ["O+ in the primary blood bank stocks is plenty.",
                          "O+ in the secondary blood bank stocks is insufficient."]
        self.assertStdIO(inputs, expectedOutput, 1)

    @number(2.4)
    @weight(2.0)
    @visibility("visible")
    def test_4(self):
        """Test 4: B-"""
        inputs = ["PISISIPI", "SIPSIPSI", "B-"]
        expectedOutput = ["B- in the primary blood bank stocks is scarce.",
                          "B- in the secondary blood bank stocks is insufficient."]
        self.assertStdIO(inputs, expectedOutput, 1)
