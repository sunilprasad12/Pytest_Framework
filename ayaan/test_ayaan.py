from pytest import mark

a = 100

@mark.smoke
class TestAyaan:

    def test_ayaan_toy(self):
        pass

    def test_ayaan_firetruck(self):
        pass

@mark.skip
def test_ayaan_car():
    pass

