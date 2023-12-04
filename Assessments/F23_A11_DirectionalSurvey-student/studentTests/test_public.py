import hashlib
import os
import platform
from gradescope_utils.autograder_utils.decorators import weight, number

from TestingFramework import BaseTest
from StudentSubmission import StudentSubmissionExecutor
from StudentSubmission.common import PossibleResults
from StudentSubmission.Runners import MainModuleRunner

class TestPublic(BaseTest):
    DATA_DIRECTORY = "./studentTests/data/files/test_public/"
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        StudentSubmissionExecutor.dataDirectory = cls.DATA_DIRECTORY

        operatingSystem =  system if (system := platform.system().lower()) != "darwin" else "macos"
        print(f"INFO: Using {operatingSystem} assertion files.")

        if operatingSystem == "windows":
            cls.EXPECTED_DIR = os.path.join(cls.DATA_DIRECTORY, "expected_windows/")
        elif operatingSystem == "macos":
            cls.EXPECTED_DIR = os.path.join(cls.DATA_DIRECTORY, "expected_macos/")
        else:
            cls.EXPECTED_DIR = cls.DATA_DIRECTORY

    def setUp(self) -> None:
        self.exectutionEnvironment = StudentSubmissionExecutor.generateNewExecutionEnvironment(self.studentSubmission)
        # larger timeout as matplotlib is a bit slow to start some times
        self.exectutionEnvironment.timeout = 10
        self.runner = MainModuleRunner()

    def tearDown(self) -> None:
        StudentSubmissionExecutor.cleanup(self.exectutionEnvironment)


    def assertFileHash(self, expectedFile, actualFile):
        expectedHash = None

        with open(os.path.join(self.EXPECTED_DIR, expectedFile), 'rb') as rb:
            expectedHash = hashlib.md5(rb.read(), usedforsecurity=False).hexdigest()

        actualHash = StudentSubmissionExecutor.getOrAssert(self.exectutionEnvironment, PossibleResults.FILE_HASH, file=actualFile)

        if actualHash == expectedHash:
            return

        msg = \
            (
                f"'{actualFile}' did not match '{expectedFile}'.\n"\
                f"Expected hash: {expectedHash}\n"\
                f"Your hash    : {actualHash}"
            )
        
        raise AssertionError(msg)


    def runSubmission(self, stdin, files):
        self.exectutionEnvironment.stdin = stdin
        self.exectutionEnvironment.files = files

        StudentSubmissionExecutor.execute(self.exectutionEnvironment, self.runner)


    @weight(2)
    @number(1.1)
    def test_example_1(self):
        """Example 1"""

        INPUT_FILE_1 = "A11_example1.csv"
        OUTPUT_FILE_1 = "horizontal_section.png"
        OUTPUT_FILE_2 = "vertical_section.png"
        
        stdin = [
            INPUT_FILE_1,
            OUTPUT_FILE_1,
            OUTPUT_FILE_2,
        ]

        files = {
            INPUT_FILE_1:INPUT_FILE_1
        }

        self.runSubmission(stdin, files)

        self.assertFileHash("HRZ_EX_1.png", OUTPUT_FILE_1)
        self.assertFileHash("VRT_EX_1.png", OUTPUT_FILE_2)

    @weight(2)
    @number(1.2)
    def test_example_2(self):
        """Example 2"""

        INPUT_FILE_1 = "A11_example2.csv"
        OUTPUT_FILE_1 = "horizontal_section.png"
        OUTPUT_FILE_2 = "vertical_section.png"
        
        stdin = [
            INPUT_FILE_1,
            OUTPUT_FILE_1,
            OUTPUT_FILE_2,
        ]

        files = {
            INPUT_FILE_1:INPUT_FILE_1
        }

        self.runSubmission(stdin, files)

        self.assertFileHash("HRZ_EX_2.png", OUTPUT_FILE_1)
        self.assertFileHash("VRT_EX_2.png", OUTPUT_FILE_2)



    @weight(5)
    @number(1.3)
    def  test_long_file(self):
        """Long File"""

        # This test is pretty chunky, thus, larger timeout

        self.exectutionEnvironment.timeout = 15

        INPUT_FILE_1 = "A11_long_file.csv"
        OUTPUT_FILE_1 = "horizontal_section.png"
        OUTPUT_FILE_2 = "vertical_section.png"
        
        stdin = [
            INPUT_FILE_1,
            OUTPUT_FILE_1,
            OUTPUT_FILE_2,
        ]

        files = {
            INPUT_FILE_1:INPUT_FILE_1
        }

        self.runSubmission(stdin, files)

        self.assertFileHash("HRZ_LF.png", OUTPUT_FILE_1)
        self.assertFileHash("VRT_LF.png", OUTPUT_FILE_2)

