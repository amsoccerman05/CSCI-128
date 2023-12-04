import re
from typing import Pattern

from StudentSubmission.Runners import Runner


class MainModuleRunnerWithMocks(Runner):
    def run(self):
        globalOverrides = {'__name__': "__main__"}
        globalOverrides.update(self.mocks)

        exec(self.studentSubmissionCode, globalOverrides)


class FormatAssertions:
    VALID_SIDE_LENGTHS_REGEX: Pattern = re.compile(
        r"^\[(\d+\.\d+,?\s?){3}]$"
    )
    VALID_SIDE_LENGTHS_TEXT: str = "[####.####, ####.####, ####.####]"

    VALID_SIDE_LENGTHS_HELP: str = "Failed to parse side lengths.\n" \
                                   "Ensure you are printing side lengths as a list of floats.\n" \
                                   "Something like: ``print(f'OUTPUT {side_lengths}')``"

    VALID_CLASSIFICATION_REGEX: Pattern = re.compile(
        r"^(Acute|Right|Obtuse)\s(Equilateral|Isosceles|Scalene)\sTriangle$"
    )
    VALID_CLASSIFICATION_TEXT: str = "<Acute|Right|Obtuse> <Equilateral|Isosceles|Scalene> Triangle"

    def assertCorrectSideLengthOutputFormat(self, actual):
        if not re.match(self.VALID_SIDE_LENGTHS_REGEX, actual):
            raise AssertionError("Incorrect Format Output Line 1\n"
                                 f"Expected    : {self.VALID_SIDE_LENGTHS_TEXT}\n"
                                 f"Your Output : {actual}\n"
                                 f"{self.VALID_SIDE_LENGTHS_HELP}")

    def assertCorrectClassificationOutputFormat(self, actual):
        if not re.match(self.VALID_CLASSIFICATION_REGEX, actual):
            raise AssertionError("Incorrect Format for Output Line 2\n"
                                 f"Expected    : {self.VALID_CLASSIFICATION_TEXT}\n"
                                 f"Your Output : {actual}")
