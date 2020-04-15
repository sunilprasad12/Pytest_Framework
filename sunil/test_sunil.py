from pytest import mark

a = 100
@mark.smoke
@mark.H1
@mark.skipif(a > 101, reason = " don't wanna to run on this build")
def test_sunil_H1():
    assert True

@mark.reg
def test_sunil_Job():
    assert True
