# test functions

import pytest

from Assignment_5 import height_process, bmi_process, report_process


def test_height_process():
    assert height_process(5, 10) == 70


def test_bmi_process():
    assert bmi_process(130, 66) == pytest.approx(21, abs=.1)


def test_report_under():
    assert report_process(18) == "Underweight"


def test_report_normal():
    assert report_process(22) == "within the normal range"


def test_report_over():
    assert report_process(28) == "Overweight"