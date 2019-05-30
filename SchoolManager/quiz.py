#!/bin/env python

from typing import List, Dict


class Quiz:
    """ """
    def __init__(self, name: str, teacher,
                 questions: Dict[str, List[str]],
                 answers: List[int]):
        self.name = name
        self.teacher = teacher
        self.questions = questions
        self.answers = answers
        self.grade = 0.0
        self.completely_graded = False

    def add_question(self, question: str, choices: List[str],
                     answer: int) -> None:
        self.questions[question] = choices
        self.answers.append(answer)

    def submit(self):
        self.teacher.grade_quiz(self)
