from was_run import WasRun


class TestCase:
    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def run(self):
        result = TestResult()
        result.test_started()
        self.set_up()

        try:
            method = getattr(self, self.name)
            method()
        except Exception:
            result.test_failed()

        self.tear_down()
        return result

    def tear_down(self):
        pass


class TestResult:
    def __init__(self):
        self.run_count = 0
        self.failure_count = 0

    def test_started(self):
        self.run_count += 1

    def test_failed(self):
        self.failure_count += 1

    def summary(self):
        return f"{self.run_count} run, {self.failure_count} failed"


class TestCaseTest(TestCase):
    def set_up(self):
        self.test = WasRun("test_method")

    def test_template_method(self):
        test = WasRun("test_method")
        test.run()
        assert "set_up test_method tear_down " == test.log

    def test_result(self):
        test = WasRun("test_method")
        result = test.run()
        assert "1 run, 0 failed" == result.summary()

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        result = test.run()
        assert "1 run, 1 failed" == result.summary()

    def test_failed_result_formatting(self):
        result = TestResult()
        result.test_started()
        result.test_failed()
        assert "1 run, 1 failed" == result.summary()


if __name__ == '__main__':
    TestCaseTest("test_template_method").run()

