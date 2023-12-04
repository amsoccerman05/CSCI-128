from gradescope_utils.autograder_utils.decorators import weight, number

from StudentSubmission import StudentSubmissionExecutor
from StudentSubmission.common import PossibleResults
from TestingFramework import BaseTest
from TestingFramework import SingleFunctionMock
from test_public_common import MainModuleRunnerWithMocks, FormatAssertions


class PublicOutputFormatTests(BaseTest, FormatAssertions):
    def setUp(self) -> None:
        self.environment = StudentSubmissionExecutor.generateNewExecutionEnvironment(self.studentSubmission)
        self.runner = MainModuleRunnerWithMocks()
        roundMock = SingleFunctionMock("round", [1000.0002, 1124.9209, 1832.1921])
        self.runner.setMocks({'round': roundMock})

        self.environment.stdin = [
            "1 0",
            "0 1",
            "1 1"
        ]

        self.environment.timeout = 1

    def tearDown(self) -> None:
        StudentSubmissionExecutor.cleanup(self.environment)

    @weight(.667)
    @number(1.1)
    def test_is_using_round(self):
        """Verify Using `round` to Round to Four Decimal Places"""

        StudentSubmissionExecutor.execute(self.environment, self.runner)

        roundMock: SingleFunctionMock = StudentSubmissionExecutor.getOrAssert(
            self.environment,
            PossibleResults.MOCK_SIDE_EFFECTS,
            mock="round"
        )

        roundMock.assertCalled()
        roundMock.assertCalledWith(
            1, 4, message="Ensure that you are using round to round to 4 decimal places.\n"
                          "For example: ``round(3.14159, 4) == 3.1416``"
        )

    @weight(.667)
    @number(1.2)
    def test_correct_side_length_output_format(self):
        """Verify Printing List of Side Lengths"""

        StudentSubmissionExecutor.execute(self.environment, self.runner)

        actualOutput = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.STDOUT)

        self.assertCorrectNumberOfOutputLines(range(2), actualOutput)

        self.assertCorrectSideLengthOutputFormat(actualOutput[0])

    @weight(.666)
    @number(1.3)
    def test_correct_classification_output_format(self):
        """Verify Format for Triangle Classification"""

        StudentSubmissionExecutor.execute(self.environment, self.runner)

        actualOutput = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.STDOUT)

        self.assertCorrectNumberOfOutputLines(range(2), actualOutput)

        self.assertCorrectClassificationOutputFormat(actualOutput[1])
