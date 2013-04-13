from datetime import datetime
import keys


def test_human_date():
    assert "2013-04-14" == keys.human_date(datetime(2013, 4, 14))


def test_reversed_human_date():
    assert "r7986-95-85" == keys.reversed_human_date(datetime(2013, 4, 14))