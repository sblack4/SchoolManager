Feature: Teachers
  - There are Teachers
  - Students are in classes that teachers teach
  - Teachers can create multiple quizzes with many questions (each question is multiple choice)
  - Teachers can assign quizzes to students
  - For each teacher, they can calculate each student's total grade accumulated over a semester for their classes

  Scenario: Teachers have names
    Given: A Teacher
    Then: This teacher has a name

  Scenario: Teachers teach classes

  Scenario: Teachers can create multiple quizzes with many questions (each question is multiple choice)
    Given A Teacher with multiple lists of multiple choice quesitons
    And List of lists of multiple choice questions "<quize_questions>"
    Then The Teacher can create multiple "<quizes>"

  Scenario: Teachers can assign quizzes to students


  Scenario: For each teacher, they can calculate each student's total grade accumulated over a semester for their classes
