#!/bin/env python

import SchoolManager.quiz
from typing import List


class Student:
    """ """
    def __init__(self, name: str):
        self.name = name
        self.assigned_quizzes = {}

    def get_assigned_quiz(self, assigned_quiz: SchoolManager.quiz.Quiz):
        self.assigned_quizzes[assigned_quiz.name] = assigned_quiz

    def complete_quiz(self, quiz_name: str, answers: List[int]):
        completed_quiz = self.assigned_quizzes[quiz_name]
        # keeps answers from last time allowing incremental completion
        completed_quiz.answers = completed_quiz.answers + answers
        completed_quiz.submit()

