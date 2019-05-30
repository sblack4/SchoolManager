#!/bin/env python

import SchoolManager.quiz
import SchoolManager.student
import SchoolManager.seminar
from typing import List, Dict
from copy import deepcopy
from statistics import mean


class Teacher:
    def __init__(self, name: str):
        self.name = name
        self.classes = []
        self.quizzes = {}

    def create_class(self, class_name: str):
        seminar = SchoolManager.seminar.Seminar(class_name, teacher=self.name)
        self.classes.append(seminar)
        return seminar

    def create_quiz(self, name: str, questions: Dict[str, List[str]],
                    answers: List[int]):
        quiz = Quiz(name, questions, answers)
        self.quizzes[name] = quiz
        return quiz

    @staticmethod
    def assign_quiz(quiz: SchoolManager.quiz.Quiz, student: SchoolManager.student.Student):
        quiz_copy = deepcopy(quiz)
        quiz_copy.answers = []  # don't give them the answers!
        student.get_assigned_quiz(quiz_copy)

    def grade_quiz(self, quiz: SchoolManager.quiz.Quiz):
        teacher_copy_of_quiz = self.quizzes[quiz.name]
        number_correct = 0
        for answer, submission in zip(teacher_copy_of_quiz.answers, quiz.answers):
            if answer == submission:
                number_correct += 1
        grade = number_correct / float(len(teacher_copy_of_quiz.answers))
        quiz.grade = grade

    def _grade_student(self, student: SchoolManager.student.Student):
        grades = []
        for quiz in student.assigned_quizzes.items():
            self.grade_quiz(quiz)
            grades.append(quiz.grade)
        return mean(grades)

    def calculate_final_grades(self) -> Dict[str, float]:
        final_grades = {}
        set_of_students = set([student for seminar in self.classes for student in seminar])
        for student in set_of_students:
            student_grade = self._grade_student(student)
            final_grades[student.name] = student_grade
        return final_grades

