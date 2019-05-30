# School Manager
An OOP Python exercise for TDD and Gherkin 

## About 
Python for OOP exercise 
- pytest for TDD
- Gherkin feature files for test scenario exercise
- think from user perspective 
- write good test scenarios 
- show how much you care about understanding functional requirements and user value

## Requirements 
- There are Teachers
- There are Students
- Students are in classes that teachers teach
- Teachers can create multiple quizzes with many questions (each question is multiple choice)
- Teachers can assign quizzes to students
- Students solve/answer questions to complete the quiz, but they don't have to complete it at once. (Partial submissions can be made).
- Quizzes need to get graded
- For each teacher, they can calculate each student's total grade accumulated over a semester for their classes

## Running

Install packages 
```bash
pip install -r requirements.txt
```

Run Tests 
```bash
pytest test
```