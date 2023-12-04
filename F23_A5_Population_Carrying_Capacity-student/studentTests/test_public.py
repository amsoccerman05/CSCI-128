from gradescope_utils.autograder_utils.decorators import weight, number, visibility

from TestingFramework import BaseTest
from StudentSubmission import StudentSubmissionAssertions
from StudentSubmission import StudentSubmissionExecutor
from StudentSubmission.Runners import MainModuleRunner
from StudentSubmission.common import PossibleResults


class PopulationCarryingCapacityPublicTests(BaseTest, StudentSubmissionAssertions):

    def setUp(self):
        self.executionEnvironment = StudentSubmissionExecutor.generateNewExecutionEnvironment(self.studentSubmission)
        self.runner = MainModuleRunner()

    def tearDown(self):
        StudentSubmissionExecutor.cleanup(self.executionEnvironment)

    def assertStdIO(self, inputs: list[str], expectedOutput: list[float], timeout: int):
        self.executionEnvironment.stdin = inputs
        self.executionEnvironment.timeout = timeout
        StudentSubmissionExecutor.execute(self.executionEnvironment, self.runner)

        actualOutput = StudentSubmissionExecutor.getOrAssert(self.executionEnvironment, PossibleResults.STDOUT)
        self.assertCorrectNumberOfOutputLines(expectedOutput, actualOutput)

        self.assertListAlmostEqual(expectedOutput, actualOutput, allowedDelta=0.000025)

    @number(1.1)
    @weight(.25)
    @visibility("visible")
    def test_example_1(self):
        """Example Execution 1"""

        inputs = ["0.2", "2.343"]

        expectedOutput = [0.573197]

        self.assertStdIO(inputs, expectedOutput, 1)

    @number(1.2)
    @weight(.25)
    @visibility("visible")
    def test_example_2(self):
        """Example Execution 2"""

        inputs = ["0.7", "3.2"]

        expectedOutput = [0.799455, 0.513045]

        self.assertStdIO(inputs, expectedOutput, 1)

    @number(1.3)
    @weight(.25)
    @visibility("visible")
    def test_example_3(self):
        """Example Execution 3"""

        inputs = ["0.9", "3.1"]

        expectedOutput = [0.764565, 0.558017]

        self.assertStdIO(inputs, expectedOutput, 1)

    @number(1.4)
    @weight(.25)
    @visibility("visible")
    def test_example_4(self):
        """Example Execution 4"""

        inputs = ["0.1", "2.111"]

        expectedOutput = [0.526291]

        self.assertStdIO(inputs, expectedOutput, 1)




    @number(2.1)
    @weight(1.25)
    def test_large_cycle(self):
        """Large Cycle"""

        inputs = [
                    "0.999",
                    "4",
                ]

        expectedOutput = [
                0.711539, 0.821005, 0.587823, 0.969148, 0.119601, 0.421186, 0.975153, 0.096919,0.350103, 0.910124, 0.327193, 0.880551, 0.420724, 0.974861, 0.098028, 0.353674, 
                0.914355, 0.31324, 0.860483, 0.480208, 0.998433, 0.006258, 0.024875, 0.097025, 0.350445, 0.910533, 0.325851, 0.878689, 0.426379, 0.97832, 0.08484, 0.310569, 
                0.856464, 0.491734, 0.999727, 0.001092, 0.004363, 0.017376, 0.068296, 0.254527, 0.758972, 0.731734, 0.785197, 0.674651, 0.877988, 0.4285, 0.979551, 0.080123, 0.294813, 0.831593, 0.560184, 0.985512,
                0.057112, 0.215401, 0.676014, 0.876076, 0.434267, 0.982717, 0.067937, 0.253286, 0.756529, 0.736771, 0.775758, 0.69583, 0.846602, 0.519468, 0.998484, 0.006055, 0.024073, 0.093974, 0.340572, 0.898331, 0.36533,
                0.927456, 0.269125, 0.786787, 0.671013, 0.883018, 0.413189, 0.969855, 0.116945, 0.413075, 0.969776, 0.117242, 0.413985, 0.970406, 0.114873, 0.406709, 0.965187, 0.134404, 0.465358, 0.9952, 0.019108, 0.074972,
                0.277405, 0.801806, 0.635653, 0.926393, 0.272756, 0.793441, 0.65557, 0.903192, 0.349745, 0.909694, 0.328603, 0.882492, 0.414799, 0.970963, 0.112775, 0.400227, 0.960181, 0.152934, 0.518181, 0.998678,
                0.005281, 0.021012, 0.082282, 0.302047, 0.843258, 0.528696, 0.996706, 0.013133, 0.051842, 0.196618, 0.631837, 0.930476, 0.258762, 0.767217, 0.71438, 0.816165, 0.600159, 0.959873, 0.154067, 0.521321, 0.998182,
                0.007259, 0.028825, 0.111976, 0.39775, 0.95818, 0.160284, 0.538372, 0.99411, 0.023421, 0.09149, 0.332478, 0.887746, 0.398612, 0.958882, 0.157709, 0.531347, 0.996069, 0.015662, 0.061667, 0.231457, 
            ]


        self.assertStdIO(inputs, expectedOutput, 1)


    @number(2.2)
    @weight(1.25)
    def test_growth_at_carrying_capacity(self):
        """Growth at Carrying Capacity"""

        inputs = [
                "1",
                "1.5",
            ]

        expectedOutput = [
                0.0,
            ]

        self.assertStdIO(inputs, expectedOutput, 1)

        
    @number(2.3)
    @weight(1.25)
    def test_no_growth(self):
        """No Growth"""

        inputs = [
                ".999",
                "1",
            ]

        expectedOutput = [
                0.000707,
            ]

        self.assertStdIO(inputs, expectedOutput, 1)


    @number(2.4)
    @weight(1.25)
    def test_stable_growth(self):
        """Stable Growth"""

        inputs = [
                "0.05",
                "1.2",
            ]

        expectedOutput = [
                0.166665,
            ]

        self.assertStdIO(inputs, expectedOutput, 1)










