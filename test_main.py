from main import process


def test_process():
    assert process(1) == 2
    assert process(5) == 10
    assert process(-3) == -6
