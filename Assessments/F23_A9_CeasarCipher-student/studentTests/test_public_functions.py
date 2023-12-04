import string

from gradescope_utils.autograder_utils.decorators import weight, number
from TestingFramework import BaseTest
from StudentSubmission import StudentSubmissionExecutor
from StudentSubmission.common import PossibleResults
from StudentSubmission.Runners import FunctionRunner


class TestPublicFunctions(BaseTest):

    def setUp(self) -> None:
        self.executionEnvironment = StudentSubmissionExecutor.generateNewExecutionEnvironment(self.studentSubmission)
        self.executionEnvironment.timeout = 1

    def tearDown(self) -> None:
        StudentSubmissionExecutor.cleanup(self.executionEnvironment)

    def assertFunctionReturn(self, runner: FunctionRunner, expected):
        StudentSubmissionExecutor.execute(self.executionEnvironment, runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.executionEnvironment, PossibleResults.RETURN_VAL)

        if isinstance(actual, tuple):
            actual = list(actual)

        self.assertEqual(expected, actual)

    @weight(0.33)
    @number(1.1)
    def test_example_1(self):
        """`encrypt` - Example Execution 1"""
        runner = FunctionRunner('encrypt', "My secret message", 10)
        expected = "Wi combod wocckqo"

        self.assertFunctionReturn(runner, expected)

    @weight(0.33)
    @number(1.2)
    def test_example_2(self):
        """`encrypt` - Example Execution 2"""
        runner = FunctionRunner('encrypt', "N0t numb3r5", 7)
        expected = "U0a ubti3y5"

        self.assertFunctionReturn(runner, expected)

    @weight(0.34)
    @number(1.3)
    def test_example_3(self):
        """`encrypt` - Example Execution 3"""
        runner = FunctionRunner('encrypt', "Large negative shift", -82)
        expected = "Hwnca jacwpera odebp"

        self.assertFunctionReturn(runner, expected)

    @weight(0.33)
    @number(1.4)
    def test_example_4(self):
        """`decrypt` - Example Execution 1"""
        runner = FunctionRunner('decrypt', "Ger csy vieh xlmw?", "read")
        expected = ["Can you read this?", 4]

        self.assertFunctionReturn(runner, expected)

    @weight(0.33)
    @number(1.5)
    def test_example_5(self):
        """`decrypt` - Example Execution 2"""
        runner = FunctionRunner('decrypt', "Ujqhlgyjshzq ak fwsl!", "is")
        expected = ["Cryptography is neat!", 18]

        self.assertFunctionReturn(runner, expected)

    @weight(0.34)
    @number(1.6)
    def test_example_6(self):
        """`decrypt` - Example Execution 3"""
        runner = FunctionRunner('decrypt', "Ujqhlgyjshzq ak fwsl!", "message")
        expected = "ERROR"

        self.assertFunctionReturn(runner, expected)

    @weight(0.5)
    @number(2.1)
    def test_test_encrypt_success(self):
        """`test_encrypt` - Verify no assertion error on success"""
        runner = FunctionRunner('test_encrypt', "quizzes", 1, "rvjaaft")

        StudentSubmissionExecutor.execute(self.executionEnvironment, runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.executionEnvironment, PossibleResults.EXCEPTION)

        self.assertIsNone(actual)

    @weight(0.5)
    @number(2.2)
    def test_test_encrypt_fail(self):
        """`test_encrypt`  - Verify assertion error on fail"""
        runner = FunctionRunner("test_encrypt", "quizzes", 1, "not the right answer")

        with self.assertRaises(AssertionError):
            StudentSubmissionExecutor.execute(self.executionEnvironment, runner)

    @weight(0.5)
    @number(2.3)
    def test_test_decrypt_success(self):
        """`test_decrypt` - Verify no assertion error on success"""
        runner = FunctionRunner("test_decrypt", "rvjaaft", "quizzes", "quizzes", 1)

        StudentSubmissionExecutor.execute(self.executionEnvironment, runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.executionEnvironment, PossibleResults.EXCEPTION)

        self.assertIsNone(actual)

    @weight(0.5)
    @number(2.4)
    def test_test_decrypt_fail(self):
        """`test_decrypt` - Verify assertion error on fail"""
        runner = FunctionRunner("test_decrypt", "rvjaaft", "quizzes", "not the right answer", 5)

        with self.assertRaises(AssertionError):
            StudentSubmissionExecutor.execute(self.executionEnvironment, runner)

    @weight(1)
    @number(2.5)
    def test_test_decrypt_one_output(self):
        """`test_decrypt` - Verify pass with 'ERROR' as expected output"""
        runner = FunctionRunner("test_decrypt", "pink", "love", "ERROR", 0)

        StudentSubmissionExecutor.execute(self.executionEnvironment, runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.executionEnvironment, PossibleResults.EXCEPTION)

        self.assertIsNone(actual)

    @weight(1)
    @number(2.6)
    def test_encrypt_all_numbers(self):
        """`encrypt` - Test encrypt all numbers"""
        expected = "98495165498124189165154561544312461231361"
        runner = FunctionRunner("encrypt", expected, 15)

        self.assertFunctionReturn(runner, expected)

    @weight(1)
    @number(2.7)
    def test_encrypt_all_symbols(self):
        """`encrypt` - Test encrypt all symbols"""
        expected = string.punctuation * 2
        runner = FunctionRunner("encrypt", expected, 5)

        self.assertFunctionReturn(runner, expected)

    @weight(1)
    @number(2.8)
    def test_decrypt_mixed_symbols(self):
        """`decrypt` - Test decrypt with mixed numbers and symbols"""
        keyword = "1234567890"
        expected_str = string.punctuation + string.whitespace + keyword

        runner = FunctionRunner("decrypt", expected_str, keyword)

        expected = [expected_str, 0]

        self.assertFunctionReturn(runner, expected)

    @weight(1)
    @number(2.9)
    def test_decrypt_no_shift(self):
        """`decrypt` - Test decrypt with no shift"""
        expected_str = "CSCI 128 is my favorite class and A9 is the bestest assignment"
        keyword = "bestest"

        runner = FunctionRunner("decrypt", expected_str, keyword)

        expected = [expected_str, 0]

        self.assertFunctionReturn(runner, expected)

