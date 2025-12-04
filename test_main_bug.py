from main_bug import process


def test_odd():
    assert process(3) == 9
    assert process(11) == 33
    assert process(-5) == -15
