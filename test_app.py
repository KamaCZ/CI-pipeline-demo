import app


class TestCalculator:
    def test_addition(self):
        assert app.add(2, 2) == 4

    def test_subtraction(self):
        assert app.subtract(4, 2) == 2
