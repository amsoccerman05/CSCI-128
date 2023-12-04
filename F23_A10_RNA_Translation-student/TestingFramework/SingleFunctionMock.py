from typing import Callable


class SingleFunctionMock:
    """
    This is a simple static mock interface that allows a single function to be mocked.
    It is also pickleable, which is why the ref:`unittest.mock.Mock` could not be used in this application
    """

    def __init__(self, name: str, sideEffect: list[object] | None = None, spy: bool = False):
        self.called: bool = False
        self.calledTimes: int = 0
        self.calledWithArgs: list[tuple] = []
        self.calledWithKwargs: list[dict[str, object]] = []
        self.mockName: str = name
        self.spyFunction: Callable = self
        self.sideEffect: list[object] | None = sideEffect
        self.spy = spy

    def setSpyFunction(self, initalFunctionName: Callable):
        self.spyFunction = initalFunctionName


    def __call__(self, *args, **kwargs):
        self.called = True
        self.calledTimes += 1
        self.calledWithArgs.append(args)
        self.calledWithKwargs.append(kwargs)

        if self.spy:
            return self.spyFunction(*args, **kwargs)

        if self.sideEffect is None:
            return None

        if (self.calledTimes - 1) >= len(self.sideEffect):
            return self.sideEffect[len(self.sideEffect) - 1]

        return self.sideEffect[self.calledTimes - 1]

    def assertCalled(self):
        if not self.called:
            raise AssertionError(f"Function: {self.mockName} was not called.\nExpected to be called")

    def assertNotCalled(self):
        if self.called:
            raise AssertionError(f"Function: {self.mockName} was called.\nExpected not to be called.")

    def assertCalledWith(self, *args):
        self.assertCalled()
        for calledWithArgs in self.calledWithArgs:
            if calledWithArgs == args:
                return

        raise AssertionError(f"Function: {self.mockName} was not called with arguments: {args}.")

    def assertCalledTimes(self, _times: int):
        if _times != self.calledTimes:
            raise AssertionError(
                f"Function: {self.mockName} was called {self.calledTimes}.\nExpected to be called {_times} times")

    def assertCalledAtLeast(self, _times: int):
        if _times > self.calledTimes:
            raise AssertionError(
                f"Function: {self.mockName} was called {self.calledTimes}.\nExpected to be called at least {_times} times")
