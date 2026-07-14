import pytest

@pytest.mark.smoke
def test_m2():
    print("Inside test m2")


@pytest.mark.smoke
#@pytest.mark.sample1
def test_m3():
    print("insdie test m3")



@pytest.mark.smoke
@pytest.mark.order(1)   #we can execute test cases in order by giving order number
def test_m4():
    print("Inside test m4")


@pytest.mark.smoke
def test_m5():
    print("Inside test m5")