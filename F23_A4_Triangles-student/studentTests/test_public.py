from gradescope_utils.autograder_utils.decorators import weight, number
from StudentSubmission import StudentSubmissionExecutor
from StudentSubmission.common import PossibleResults
from StudentSubmission.Runners import MainModuleRunner
from TestingFramework import BaseTest


class TestTriangleTypesPublic(BaseTest):

    def setUp(self) -> None:
        self.environment = StudentSubmissionExecutor.generateNewExecutionEnvironment(self.studentSubmission)
        self.runner = MainModuleRunner()

    def tearDown(self) -> None:
        StudentSubmissionExecutor.cleanup(self.environment)

    def assertStdIO(self, stdin, expectedOutput):
        self.environment.stdin = stdin
        self.environment.timeout = 1

        StudentSubmissionExecutor.execute(self.environment, self.runner)

        actualOutput = StudentSubmissionExecutor.getOrAssert(self.environment, PossibleResults.STDOUT)

        self.assertCorrectNumberOfOutputLines(expectedOutput, actualOutput)

        self.assertListEqual(expectedOutput[0], actualOutput[0], msg="Failed on Output Line 1")
        self.assertEqual(expectedOutput[1], actualOutput[1], msg="Failed on Output Line 2")

    @weight(.2)
    @number(2.1)
    def test_sample_execution_1(self):
        """Sample Execution 1"""

        stdin = [
            "0 0",
            "0 4",
            "3 0",
        ]

        expectedOutput = [
            [3.0, 4.0, 5.0],
            "Right Scalene Triangle",
        ]

        self.assertStdIO(stdin, expectedOutput)

    @weight(.2)
    @number(2.2)
    def test_sample_execution_2(self):
        """Sample Execution 2"""

        stdin = [
            "0 0",
            "12 3",
            "23 66",
        ]

        expectedOutput = [
            [12.3693, 63.9531, 69.8928],
            "Obtuse Scalene Triangle",
        ]

        self.assertStdIO(stdin, expectedOutput)

    @weight(.2)
    @number(2.3)
    def test_sample_execution_3(self):
        """Sample Execution 3"""

        stdin = [
            "100 0",
            "0 0",
            "50 86.6025403784",
        ]

        expectedOutput = [
            [100.0, 100.0, 100.0],
            "Acute Equilateral Triangle",
        ]

        self.assertStdIO(stdin, expectedOutput)

    @weight(.2)
    @number(2.4)
    def test_sample_execution_4(self):
        """Sample Execution 4"""

        stdin = [
            "0 2",
            "0 2",
            "3 1",
        ]

        expectedOutput = [
            [0.0, 3.1623, 3.1623],
            "Duplicate Point",
        ]

        self.assertStdIO(stdin, expectedOutput)

    @weight(.2)
    @number(2.5)
    def test_sample_execution_5(self):
        """Sample Execution 5"""

        stdin = [
            "1 1",
            "0 0",
            "2 2",
        ]

        expectedOutput = [
            [1.4142, 1.4142, 2.8284],
            "Collinear",
        ]

        self.assertStdIO(stdin, expectedOutput)

    @weight(2)
    @number(3.1)
    def test_negative_coords_1(self):
        """Test 1: Negative Coordinates Acute Isosceles"""

        stdin = [
            "-1 0",
            "0 -2",
            "-3 -1",
        ]

        expectedOutput = [
            [2.2361, 2.2361, 3.1623],
            "Acute Isosceles Triangle",
        ]

        self.assertStdIO(stdin, expectedOutput)

    @weight(2)
    @number(3.2)
    def test_negative_coords_2(self):
        """Test 2: Negative Coordinates Obtuse Scalene"""

        stdin = [
            "-50.4562 0",
            "0 0",
            "19.4549217407 -18.2170737582"
        ]

        expectedOutput = [
            [26.6525, 50.4562, 72.2456],
            "Obtuse Scalene Triangle",
        ]

        self.assertStdIO(stdin, expectedOutput)

    @weight(1)
    @number(4.1)
    def test_isosceles_1(self):
        """Test 3: Obtuse Isosceles"""

        stdin = [
            "15 0",
            "0 0",
            "7.5 6.6143782777",
        ]

        expectedOutput = [
            [10.0, 10.0, 15.0],
            "Obtuse Isosceles Triangle"
        ]

        self.assertStdIO(stdin, expectedOutput)

    @weight(1)
    @number(4.2)
    def test_isosceles_2(self):
        """Test 4: Acute Isosceles"""

        stdin = [
            "5 0",
            "0 0",
            "2.5 4.5184805706",
        ]

        expectedOutput = [
            [5.0, 5.164, 5.164],
            "Acute Isosceles Triangle",
        ]

        self.assertStdIO(stdin, expectedOutput)

    @weight(2)
    @number(4.3)
    def test_isosceles_3(self):
        """Test 5: Almost Isosceles"""

        stdin = [
            "25 0",
            "0 0",
            "10.48 48.8893608058",
        ]

        expectedOutput = [
            [25.0, 50.0, 51.0],
            "Acute Scalene Triangle",
        ]

        self.assertStdIO(stdin, expectedOutput)
