import os
import re
from gradescope_utils.autograder_utils.decorators import weight, number
from StudentSubmission.common import PossibleResults

from StudentSubmission import StudentSubmissionExecutor
from StudentSubmission.Runners import MainModuleRunner
from TestingFramework import BaseTest

REQUIREMENTS_FILE_REGEX = re.compile(r"^requirements.txt$")
PYTHON_FILE_REGEX = re.compile(r"^(\w|\s)+\.py$")
STDIN = re.compile(r"^STDIN$")


class TestFinalProject(BaseTest):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        StudentSubmissionExecutor.dataDirectory = cls.submissionDirectory

        workingDirectory = os.getcwd()

        os.chdir(cls.submissionDirectory)
        cls.dataFiles = []
        cls.stdin = []

        cls.discoverSubmittedDataFiles("./")

        os.chdir(workingDirectory)

    def setUp(self) -> None:
        self.executionEnvironment = StudentSubmissionExecutor.generateNewExecutionEnvironment(self.studentSubmission)
        self.executionEnvironment.timeout = 60
        self.runner = MainModuleRunner()

    def tearDown(self) -> None:
        StudentSubmissionExecutor.cleanup(self.executionEnvironment)

    @classmethod
    def discoverSubmittedDataFiles(cls, directoryToSearch):
        # this is a recurive search method.

        if "__" in directoryToSearch:
            return

        if directoryToSearch == "." or directoryToSearch == "..":
            return

        for file in os.listdir(directoryToSearch):
            if PYTHON_FILE_REGEX.match(file) or REQUIREMENTS_FILE_REGEX.match(file):
                continue

            path = os.path.join(directoryToSearch, file)

            if not cls.stdin and STDIN.match(file):
                with open(path, "r") as r:
                    cls.stdin = r.readlines()
                    for i in range(len(cls.stdin)):
                        cls.stdin[i] = cls.stdin[i].strip()

            elif os.path.isfile(path) and not PYTHON_FILE_REGEX.match(file) and not REQUIREMENTS_FILE_REGEX.match(file):
                cls.dataFiles.append(path)
            elif os.path.isdir(path):
                cls.discoverSubmittedDataFiles(os.path.dirname(path))

    @staticmethod
    def create_file_map(files):
        fileMap = {}

        for file in files:
            fileMap[file] = file

        return fileMap

    @weight(3.0)
    @number(1.1)
    def test_verify_data_files(self):
        """Verify using at least one data file"""
        msg = (
            "No data files found.\n"
            f"Ensure that you have at least one data file in {self.submissionDirectory}"
        )

        self.assertTrue(len(self.dataFiles) > 0, msg=msg)

    @weight(6.0)
    @number(1.2)
    def test_verify_submission_runs_without_error(self):
        """Verify submission runs without error"""
        self.executionEnvironment.files = self.create_file_map(self.dataFiles)
        self.executionEnvironment.stdin = self.stdin

        try:
            StudentSubmissionExecutor.execute(self.executionEnvironment, self.runner)
        except:
            pass

        actualExeception = StudentSubmissionExecutor.getOrAssert(self.executionEnvironment, PossibleResults.EXCEPTION)

        if actualExeception is EOFError:
            msg = (
                "EOF error occurred when running submission.\n"
                "Did you define a STDIN file correctly? Do you have correct number of input lines?\n"
                f"Contents of STDIN are: {self.stdin}\n"
            )
            raise AssertionError(msg)

        self.assertIsNone(actualExeception)

    @weight(3.0)
    @number(1.3)
    def test_verify_creates_at_least_one_line_of_output(self):
        """Verify submission creates at least one line of output"""
        self.executionEnvironment.files = self.create_file_map(self.dataFiles)
        self.executionEnvironment.stdin = self.stdin

        StudentSubmissionExecutor.execute(self.executionEnvironment, self.runner)

        actualOutput = StudentSubmissionExecutor.getOrAssert(self.executionEnvironment, PossibleResults.STDOUT)

        msg = (
            f"{len(actualOutput)} output lines generated. Expected > 0"
        )

        self.assertTrue(len(actualOutput) > 0, msg=msg)

    @weight(3.0)
    @number(1.4)
    def test_verify_creates_at_least_one_plot(self):
        """Verify creates at least one plot"""
        self.executionEnvironment.files = self.create_file_map(self.dataFiles)
        self.executionEnvironment.stdin = self.stdin

        StudentSubmissionExecutor.execute(self.executionEnvironment, self.runner)

        generated_files = self.executionEnvironment.resultData[PossibleResults.FILE_OUT]

        msg = (
            f"{len(generated_files)} output files generated. Expected > 0"
        )

        self.assertTrue(len(generated_files) > 0, msg=msg)
