from gradescope_utils.autograder_utils.decorators import weight, number

from TestingFramework import BaseTest, SingleFunctionMock
from StudentSubmission import StudentSubmissionExecutor
from StudentSubmission.common import PossibleResults
from StudentSubmission.Runners import MainModuleRunner, Runner


class MainModuleRunnerWithMocks(Runner):
    def run(self):
        globalOverrides = {'__name__': "__main__"}
        globalOverrides.update(self.mocks)

        exec(self.studentSubmissionCode, globalOverrides)


class TestPublicFullExecutions(BaseTest):

    def setUp(self) -> None:
        self.executionEnvironment = StudentSubmissionExecutor.generateNewExecutionEnvironment(self.studentSubmission)
        self.executionEnvironment.timeout = 10000
        self.runner = MainModuleRunner()

    def tearDown(self) -> None:
        StudentSubmissionExecutor.cleanup(self.executionEnvironment)

    def assertStdio(self, stdin, expected):
        self.executionEnvironment.stdin = stdin

        StudentSubmissionExecutor.execute(self.executionEnvironment, self.runner)

        actual = StudentSubmissionExecutor.getOrAssert(self.executionEnvironment, PossibleResults.STDOUT)
        self.assertCorrectNumberOfOutputLines(expected, actual)

        for i in range(len(expected)):
            self.assertEqual(expected[i], actual[i], f"Failed on output line {i + 1} of {len(expected)}")

    @weight(.25)
    @number(3.1)
    def test_example_1(self):
        """Full Execution - Example 1"""

        stdin = [
            "1",
            "Hello World!",
            "31",
        ]

        expected = [
            "Mjqqt Btwqi!",
        ]

        self.assertStdio(stdin, expected)

    @weight(.25)
    @number(3.2)
    def test_example_2(self):
        """Full Execution - Example 2"""
        stdin = [
            "2",
            "Mjqqt Btwqi!",
            "World",
        ]

        expected = [
            "Hello World!",
            "5",
        ]

        self.assertStdio(stdin, expected)

    @weight(0.25)
    @number(3.3)
    def test_example_3(self):
        """Full Execution - Example 3"""
        stdin = [
            "2",
            "Mjqqt Btwqi!",
            "Mines",
        ]

        expected = [
            "ERROR"
        ]

        self.assertStdio(stdin, expected)

    @weight(0.25)
    @number(3.4)
    def test_example_4(self):
        """Full Execution - Example 4"""
        stdin = [
            "3",
        ]

        self.executionEnvironment.stdin = stdin

        StudentSubmissionExecutor.execute(self.executionEnvironment, self.runner)

        exceptions = StudentSubmissionExecutor.getOrAssert(self.executionEnvironment, PossibleResults.EXCEPTION)

        self.assertIsNone(exceptions)

    @weight(0.5)
    @number(4.1)
    def test_long_encryption(self):
        """Full Execution - Encrypt long sentence with negative shift"""
        stdin = [
            "1",
            """Hello, it's me I was wondering if after all these years you'd like to meet To go over everything They say that time's supposed to heal ya, but I ain't done much healing Hello, can you hear me? I'm in California dreaming about who we used to be When we were younger and free I've forgotten how it felt before the world fell at our feet There's such a difference between us And a million miles Hello from the other side I must've called a thousand times To tell you I'm sorry for everything that I've done But when I call, you never seem to be home Hello from the outside At least I can say that I've tried To tell you I'm sorry for breaking your heart But it don't matter, it clearly doesn't tear you apart anymore""",
            "-109",
        ]

        expected = [
            """Czggj, do'n hz D rvn rjiyzmdib da vaozm vgg ocznz tzvmn tjp'y gdfz oj hzzo Oj bj jqzm zqzmtocdib Oczt nvt ocvo odhz'n npkkjnzy oj czvg tv, wpo D vdi'o yjiz hpxc czvgdib Czggj, xvi tjp czvm hz? D'h di Xvgdajmidv ymzvhdib vwjpo rcj rz pnzy oj wz Rczi rz rzmz tjpibzm viy amzz D'qz ajmbjoozi cjr do azgo wzajmz ocz rjmgy azgg vo jpm azzo Oczmz'n npxc v ydaazmzixz wzorzzi pn Viy v hdggdji hdgzn Czggj amjh ocz joczm ndyz D hpno'qz xvggzy v ocjpnviy odhzn Oj ozgg tjp D'h njmmt ajm zqzmtocdib ocvo D'qz yjiz Wpo rczi D xvgg, tjp izqzm nzzh oj wz cjhz Czggj amjh ocz jpondyz Vo gzvno D xvi nvt ocvo D'qz omdzy Oj ozgg tjp D'h njmmt ajm wmzvfdib tjpm czvmo Wpo do yji'o hvoozm, do xgzvmgt yjzni'o ozvm tjp vkvmo vithjmz"""
        ]

        self.assertStdio(stdin, expected)

    @weight(0.5)
    @number(4.2)
    def test_long_decryption(self):
        """Full Execution - Decrypt long sentence"""
        stdin = [
            "2",
            """Czggj, do'n hz D rvn rjiyzmdib da vaozm vgg ocznz tzvmn tjp'y gdfz oj hzzo Oj bj jqzm zqzmtocdib Oczt nvt ocvo odhz'n npkkjnzy oj czvg tv, wpo D vdi'o yjiz hpxc czvgdib Czggj, xvi tjp czvm hz? D'h di Xvgdajmidv ymzvhdib vwjpo rcj rz pnzy oj wz Rczi rz rzmz tjpibzm viy amzz D'qz ajmbjoozi cjr do azgo wzajmz ocz rjmgy azgg vo jpm azzo Oczmz'n npxc v ydaazmzixz wzorzzi pn Viy v hdggdji hdgzn Czggj amjh ocz joczm ndyz D hpno'qz xvggzy v ocjpnviy odhzn Oj ozgg tjp D'h njmmt ajm zqzmtocdib ocvo D'qz yjiz Wpo rczi D xvgg, tjp izqzm nzzh oj wz cjhz Czggj amjh ocz jpondyz Vo gzvno D xvi nvt ocvo D'qz omdzy Oj ozgg tjp D'h njmmt ajm wmzvfdib tjpm czvmo Wpo do yji'o hvoozm, do xgzvmgt yjzni'o ozvm tjp vkvmo vithjmz""",
            "Hello, it's me",
        ]
        expected = [
            """Hello, it's me I was wondering if after all these years you'd like to meet To go over everything They say that time's supposed to heal ya, but I ain't done much healing Hello, can you hear me? I'm in California dreaming about who we used to be When we were younger and free I've forgotten how it felt before the world fell at our feet There's such a difference between us And a million miles Hello from the other side I must've called a thousand times To tell you I'm sorry for everything that I've done But when I call, you never seem to be home Hello from the outside At least I can say that I've tried To tell you I'm sorry for breaking your heart But it don't matter, it clearly doesn't tear you apart anymore""",
            "21",
        ]

        self.assertStdio(stdin, expected)
