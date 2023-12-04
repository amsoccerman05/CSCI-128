import sys
import copy
import importlib
from types import FunctionType, ModuleType
from StudentSubmission.Runners import Runner


class ClassRunner(Runner):
    EXPECTED_CLASS_NAME = "result_class"

    @staticmethod
    def applyImports(_imports):
        currentModule = sys.modules[__name__]

        for moduleName in _imports:
            library = importlib.import_module(moduleName)
            setattr(currentModule, moduleName, library)

    @staticmethod
    def applyMethods(_functions):
        currentModule = sys.modules[__name__]

        for functionName, function in _functions:
            setattr(currentModule, functionName, function)

    @staticmethod
    def applyClasses(_classes):
        currentModule = sys.modules[__name__]

        for className, classValue in _classes:
            setattr(currentModule, className, classValue)


    def run(self):
        exec(self.studentSubmissionCode)

        # all of these hacky workarounds make me want to refactor this :(
        # That should be done for v2 :(
        importedModules = [localName for localName, localValue in locals().items() if
                           isinstance(localValue, ModuleType)]
        definedFunctions = [(localName, localValue) for localName, localValue in locals().items() if
                            isinstance(localValue, FunctionType)]

        definedClasses = [(localName, localValue) for localName, localValue in locals().items() if
                            isinstance(localValue, type)]

        self.applyImports(importedModules)
        self.applyMethods(definedFunctions)
        self.applyClasses(definedClasses)

        exec(self.setupCode)


        if self.EXPECTED_CLASS_NAME not in locals().keys():
            return None

        result = copy.deepcopy(locals()[self.EXPECTED_CLASS_NAME])

        return result

    
