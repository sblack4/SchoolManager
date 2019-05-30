#!/bin/env python

from SchoolManager.teacher import Teacher
from pytest_bdd import scenario, given, then


@scenario('teacher.feature', 'Teachers have names')
def test_name():
    pass


@given('A Teacher')
def a_teacher_exists(context):
    return Teacher(name='Forest Gump')


@then('This teacher has a name')
def a_teacher_has_a_name(teacher):
    assert hasattr(teacher, 'name')
