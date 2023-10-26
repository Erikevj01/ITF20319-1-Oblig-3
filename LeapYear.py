def LeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def test_leap_year():
    assert LeapYear(2000) == True
    assert LeapYear(1600) == True
    assert LeapYear(2400) == True

def test_non_leap_year():
    assert LeapYear(1700) == False
    assert LeapYear(1800) == False
    assert LeapYear(1900) == False

def test_normal_leap_year():
    assert LeapYear(2008) == True
    assert LeapYear(2012) == True
    assert LeapYear(2016) == True

def test_non_leap_years():
    assert LeapYear(2017) == False
    assert LeapYear(2018) == False
    assert LeapYear(2019) == False

def test_negative_year():
    assert LeapYear(-2000) == True
    assert LeapYear(-2004) == True
    assert LeapYear(-1700) == False
    assert LeapYear(-1800) == False

def test_invalid_input():
    assert LeapYear("test") == False
    assert LeapYear(3.14) == False
    assert LeapYear(True) == False
