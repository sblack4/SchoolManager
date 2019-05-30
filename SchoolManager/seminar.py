#!/bin/env python


class Seminar:
    """ Seminar because class is a reserved word """
    def __init__(self, name: str, teacher: str):
        self.name = name
        self.teacher = teacher
        self.enrolled_students = []
