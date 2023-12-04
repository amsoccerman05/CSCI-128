from gradescope_utils.autograder_utils.decorators import number, weight

from TestingFramework import BaseTest
from StudentSubmission import StudentSubmissionExecutor
from StudentSubmission.Runners import FunctionRunner
from StudentSubmission.common import PossibleResults
from TestingFramework import SingleFunctionMock


class TestPublicFunctions(BaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        StudentSubmissionExecutor.dataDirectory = "./studentTests/data/files/"

    def setUp(self) -> None:
        self.executionEnvironment = StudentSubmissionExecutor.generateNewExecutionEnvironment(self.studentSubmission)
        self.executionEnvironment.timeout = 1

    def tearDown(self) -> None:
        StudentSubmissionExecutor.cleanup(self.executionEnvironment)

    def assertFunctionReturn(self, runner: FunctionRunner, expectedOutput):
        StudentSubmissionExecutor.execute(self.executionEnvironment, runner)
        actual = StudentSubmissionExecutor.getOrAssert(self.executionEnvironment, PossibleResults.RETURN_VAL)

        if expectedOutput == actual:
            return
        
        msg = (f"Expected   : {runner.functionToCall}{runner.args} => {expectedOutput}\n" \
               f"Your output: {runner.functionToCall}{runner.args} => {actual}")

        raise AssertionError(msg)

    @number(1.1)
    @weight(0.33)
    def test_example_1(self):
        """`dna_to_rna` - Example Execution 1"""
        runner = FunctionRunner("dna_to_rna", "A")
        expected = "U"

        self.assertFunctionReturn(runner, expected)
        

    @number(1.2)
    @weight(0.33)
    def test_example_2(self):
        """`dna_to_rna` - Example Execution 2"""
        runner = FunctionRunner("dna_to_rna", "CGTAAGCT")
        expected = "GCAUUCGA"

        self.assertFunctionReturn(runner, expected)

    @number(1.3)
    @weight(0.34)
    def test_example_3(self):
        """`parse_file_into_acids` - Example Execution 1"""

        self.executionEnvironment.files = {"test_public/test.txt": "test.txt"}

        runner = FunctionRunner("parse_file_into_acids", "test.txt")
        expected = [['AAA', 'Lys', 'K', 'Lysine'], ['AAC', 'Asn', 'N', 'Asparagine'], ['AAG', 'Lys', 'K', 'Lysine']]

        self.assertFunctionReturn(runner, expected)

    

    @number(1.4)
    @weight(1)
    def test_parse_full_file(self):
        """`parse_file_into_acids` - Parse Full File"""
        self.executionEnvironment.files = {"test_public/codons.txt" : "codons.txt"}

        runner = FunctionRunner("parse_file_into_acids", "codons.txt")
        expected = [['AAA', 'Lys', 'K', 'Lysine'], ['AAC', 'Asn', 'N', 'Asparagine'], ['AAG', 'Lys', 'K', 'Lysine'], ['AAU', 'Asn', 'N', 'Asparagine'], ['ACA', 'Thr', 'T', 'Threonine'], ['ACC', 'Thr', 'T', 'Threonine'], ['ACG', 'Thr', 'T', 'Threonine'], ['ACU', 'Thr', 'T', 'Threonine'], ['AGA', 'Arg', 'R', 'Arginine'], ['AGC', 'Ser', 'S', 'Serine'], ['AGG', 'Arg', 'R', 'Arginine'], ['AGU', 'Ser', 'S', 'Serine'], ['AUA', 'Ile', 'I', 'Isoleucine'], ['AUC', 'Ile', 'I', 'Isoleucine'], ['AUG', 'Met', 'M', 'Methionine'], ['AUU', 'Ile', 'I', 'Isoleucine'], ['CAA', 'Gln', 'Q', 'Glutamine'], ['CAC', 'His', 'H', 'Histidine'], ['CAG', 'Gln', 'Q', 'Glutamine'], ['CAU', 'His', 'H', 'Histidine'], ['CCA', 'Pro', 'P', 'Proline'], ['CCC', 'Pro', 'P', 'Proline'], ['CCG', 'Pro', 'P', 'Proline'], ['CCU', 'Pro', 'P', 'Proline'], ['CGA', 'Arg', 'R', 'Arginine'], ['CGC', 'Arg', 'R', 'Arginine'], ['CGG', 'Arg', 'R', 'Arginine'], ['CGU', 'Arg', 'R', 'Arginine'], ['CUA', 'Leu', 'L', 'Leucine'], ['CUC', 'Leu', 'L', 'Leucine'], ['CUG', 'Leu', 'L', 'Leucine'], ['CUU', 'Leu', 'L', 'Leucine'], ['GAA', 'Glu', 'E', 'Glutamic_acid'], ['GAC', 'Asp', 'D', 'Aspartic_acid'], ['GAG', 'Glu', 'E', 'Glutamic_acid'], ['GAU', 'Asp', 'D', 'Aspartic_acid'], ['GCA', 'Ala', 'A', 'Alanine'], ['GCC', 'Ala', 'A', 'Alanine'], ['GCG', 'Ala', 'A', 'Alanine'], ['GCU', 'Ala', 'A', 'Alanine'], ['GGA', 'Gly', 'G', 'Glycine'], ['GGC', 'Gly', 'G', 'Glycine'], ['GGG', 'Gly', 'G', 'Glycine'], ['GGU', 'Gly', 'G', 'Glycine'], ['GUA', 'Val', 'V', 'Valine'], ['GUC', 'Val', 'V', 'Valine'], ['GUG', 'Val', 'V', 'Valine'], ['GUU', 'Val', 'V', 'Valine'], ['UAA', 'Stp', 'O', 'Stop'], ['UAC', 'Tyr', 'Y', 'Tyrosine'], ['UAG', 'Stp', 'O', 'Stop'], ['UAU', 'Tyr', 'Y', 'Tyrosine'], ['UCA', 'Ser', 'S', 'Serine'], ['UCC', 'Ser', 'S', 'Serine'], ['UCG', 'Ser', 'S', 'Serine'], ['UCU', 'Ser', 'S', 'Serine'], ['UGA', 'Stp', 'O', 'Stop'], ['UGC', 'Cys', 'C', 'Cysteine'], ['UGG', 'Trp', 'W', 'Tryptophan'], ['UGU', 'Cys', 'C', 'Cysteine'], ['UUA', 'Leu', 'L', 'Leucine'], ['UUC', 'Phe', 'F', 'Phenylalanine'], ['UUG', 'Leu', 'L', 'Leucine'], ['UUU', 'Phe', 'F', 'Phenylalanine']] 

        self.assertFunctionReturn(runner, expected)


    @number(1.5)
    @weight(0.5)
    def test_test_my_functions_pass(self):
        """`test_my_functions` - Verify no error on pass"""

        # Im pulling in both of the files into the execution environment for this test
        # that way we know that its not myfault if the students have a failure :)

        self.executionEnvironment.files = {
            "test_public/codons.txt": "codons.txt", 
            "test_public/test.txt": "test.txt"
        }
        
        runner = FunctionRunner("test_my_functions")
        
        StudentSubmissionExecutor.execute(self.executionEnvironment, runner)

        exception = StudentSubmissionExecutor.getOrAssert(self.executionEnvironment, PossibleResults.EXCEPTION)

        self.assertIsNone(exception)


    @number(1.6)
    @weight(0.5)
    def test_test_my_functions_fail(self):
        """`test_my_functions` - Verify AssertionError on failure"""

        # This time this test will actually work :)
        
        self.executionEnvironment.files = {
            "test_public/codons.txt": "codons.txt", 
            "test_public/test.txt": "test.txt"
        }
        
        # we are mocking the function that we require students to test as we dont know any other details
        #  of the other functions that they wrote

        mocks = {"dna_to_rna": SingleFunctionMock("dna_to_rna", None)}

        runner = FunctionRunner("test_my_functions")
        runner.setMocks(mocks)

        # Last time this error would be raised if *any* error occured bc of how the executor is set up
        #  But now, my brain has grown 5 sizes.
        with self.assertRaises(AssertionError):
            StudentSubmissionExecutor.execute(self.executionEnvironment, runner)

        # Huzzah, now you actually have to raise an assertion error! 

        actual = StudentSubmissionExecutor.getOrAssert(self.executionEnvironment, PossibleResults.EXCEPTION)

        self.assertIsInstance(actual, AssertionError, msg="Ensure that you are using the `assert` keyword in your tests")


    @number(1.7)
    @weight(1.0)
    def test_test_min_number_of_tests(self):
        """`test_my_functions` - Verify at least 3 tests of dna_to_rna"""

        # i had to add a whole new feature for this oof

        self.executionEnvironment.files = {
            "test_public/codons.txt": "codons.txt", 
            "test_public/test.txt": "test.txt"
        }

        mocks = {"dna_to_rna": SingleFunctionMock("dna_to_rna", spy=True)}

        runner = FunctionRunner("test_my_functions")
        runner.setMocks(mocks)

        StudentSubmissionExecutor.execute(self.executionEnvironment, runner)

        dna_to_rna_mock: SingleFunctionMock = \
                StudentSubmissionExecutor.getOrAssert(self.executionEnvironment, 
                                                      PossibleResults.MOCK_SIDE_EFFECTS, mock="dna_to_rna")
        
        dna_to_rna_mock.assertCalledAtLeast(3)


    @number(1.8)
    @weight(1.0)
    def test_long_dna_sequence(self):
        """`dna_to_rna` - Long sequence"""

        dna_sequence = "CGCACGGGTCCCATATAATGCAATCGTAGTCTACCTGACTGTACTTAGAAATGTGGCTTCGCCTTTGCCCACGCACCTGATCGCTCCTCGTTTGCTTTTAAGGACCGGACGAACCACAGAGCATTAGAAGAATCTCTAGCTGCTTTACAAAGTGCTGGTTCCTTTTCCAGCGGGATGTTTTATCTAAACGCAATGAGAGAGGTATTCCTCAGGCCACATCGCTTCCTAGTTCCGCTGGGATCCATCGTTGGCGGCCGAAGCCGCCATTCCATAGTGAGTTCTTCGTCTGAGTCATTCTGTGCCAGATCGACTGACAGATAGCGGATCCAGTTTATCCCTCGAAACTATAGACGTACAGGTCGAAATCTTAAGTCAAATCGCGCGTCTAGACTCAGCTCTATTTTAGTGGTCATGGGTTCTGGTCCCCCCGAGCGGCGCAACCGATTAGGACCATGTAGAACATTACTTATAAGTCATCTTTTAAACACAATCTTCCTGCTCAGTGGTACATGGTTTTCGCTATTGCTAGCCAGCCTCATAAGTAACACCACTACTGCGACCCAAATGCACCCTTTCCACGAACACAGGGTTGTCCGATCCTATATTACGACTCCGGGAAGGGGTTCGCAAGTCGCACCCTAAACGATGTTGAAGGCTCAGGATGCACAGGCACAAGTACAATATATACGTGTTCCGGCTCTTATCCTGCATCGAAAGCTCAATCATGCATCGTACCAGTGTGTTCGTGTCATCTAGGAGGGGCGCGTAGGATAAATAATTCAATTAAGATTACGTTATGCTACTGTACACCTACCCGTCACCGGCCAACAATGTGCGGATGGCGCCACGACTTACTGGGCCTGATTTCACCGCTTCTAATACCGCACACTGGGCAATACGAGGTCAAGCCAGTCACGCAGTAACGTTCATCAGCTAACGTAACAGTTAGAGGCTCGCTAAATCGCACTGTCGGCGTCCCTTGGGTATTTTACGCTAGCAT"
        runner = FunctionRunner("dna_to_rna", dna_sequence)

        expected = "GCGUGCCCAGGGUAUAUUACGUUAGCAUCAGAUGGACUGACAUGAAUCUUUACACCGAAGCGGAAACGGGUGCGUGGACUAGCGAGGAGCAAACGAAAAUUCCUGGCCUGCUUGGUGUCUCGUAAUCUUCUUAGAGAUCGACGAAAUGUUUCACGACCAAGGAAAAGGUCGCCCUACAAAAUAGAUUUGCGUUACUCUCUCCAUAAGGAGUCCGGUGUAGCGAAGGAUCAAGGCGACCCUAGGUAGCAACCGCCGGCUUCGGCGGUAAGGUAUCACUCAAGAAGCAGACUCAGUAAGACACGGUCUAGCUGACUGUCUAUCGCCUAGGUCAAAUAGGGAGCUUUGAUAUCUGCAUGUCCAGCUUUAGAAUUCAGUUUAGCGCGCAGAUCUGAGUCGAGAUAAAAUCACCAGUACCCAAGACCAGGGGGGCUCGCCGCGUUGGCUAAUCCUGGUACAUCUUGUAAUGAAUAUUCAGUAGAAAAUUUGUGUUAGAAGGACGAGUCACCAUGUACCAAAAGCGAUAACGAUCGGUCGGAGUAUUCAUUGUGGUGAUGACGCUGGGUUUACGUGGGAAAGGUGCUUGUGUCCCAACAGGCUAGGAUAUAAUGCUGAGGCCCUUCCCCAAGCGUUCAGCGUGGGAUUUGCUACAACUUCCGAGUCCUACGUGUCCGUGUUCAUGUUAUAUAUGCACAAGGCCGAGAAUAGGACGUAGCUUUCGAGUUAGUACGUAGCAUGGUCACACAAGCACAGUAGAUCCUCCCCGCGCAUCCUAUUUAUUAAGUUAAUUCUAAUGCAAUACGAUGACAUGUGGAUGGGCAGUGGCCGGUUGUUACACGCCUACCGCGGUGCUGAAUGACCCGGACUAAAGUGGCGAAGAUUAUGGCGUGUGACCCGUUAUGCUCCAGUUCGGUCAGUGCGUCAUUGCAAGUAGUCGAUUGCAUUGUCAAUCUCCGAGCGAUUUAGCGUGACAGCCGCAGGGAACCCAUAAAAUGCGAUCGUA"

        self.assertFunctionReturn(runner, expected)









