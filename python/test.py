from was_run import WasRun, TestCase


class TestCaseTest(TestCase):
    def set_up(self):
        self.test = WasRun("test_method")

    def test_template_method(self):
        test = WasRun("test_method")
        test.run()
        assert "set_up test_method tear_down " == test.log


if __name__ == '__main__':
    TestCaseTest("test_template_method").run()

