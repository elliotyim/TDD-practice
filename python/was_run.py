class TestCase:
    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def run(self):
        self.set_up()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name):
        self.was_run = None
        TestCase.__init__(self, name)

    def set_up(self):
        self.was_run = None
        self.was_set_up = 1

    def test_method(self):
        self.was_run = 1
