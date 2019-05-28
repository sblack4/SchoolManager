#!/bin/env python


from pytest_bdd import scenarios, given, then, parsers


scenarios('../features/teacher.feature')

@given()
