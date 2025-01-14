"""
Objectives
improving the student's skills in reading and writing CSV files;
using the writer function or the DictWriter class.

Scenario
Have you ever prepared a report? Your task will be to prepare a report
summarizing the results of exams in maths, physics and biology. The report
should include the name of the exam, the number of candidates, the number of
passed exams, the number of failed exams, and the best and the worst scores.
All the data necessary to create the report is in the exam_results.csv file.

Note that one candidate may have several results for the same exam. The number
of candidates should express the number of unique people in each exam
identified by Candidate ID. The final report should look like this:

Exam Name,Number of Candidates,Number of Passed Exams,Number of Failed Exams,
Best Score,Worst Score
Maths,8,4,6,90,33
Physics,3,0,3,66,50
Biology,5,2,3,88,23

NOTE: The exam_results.csv file is available in your working directory in Edube
Interactive. If you want to download the file and work with it locally, you can
do it here: exam_results.csv
"""

import csv

class ExamData:
    def __init__(self, exam_name):
        self.exam_name = exam_name
        self.candidates = []
        self.number_of_passed_exams = 0
        self.number_of_failed_exams = 0
        self.best_score = 0
        self.worst_score = 100

    def get_number_of_candidates(self):
        return len(set(self.candidates))

class ExamResultReader:
    def __init__(self, filename):
        self.filename = filename
        self.data = {}

    def prepare_data(self):
        with open(self.filename, newline='') as csvfile:
            fieldnames = ['Exam Name', 'Candidate ID', 'Score', 'Grade']
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)

            row_count = 0
            for row in reader:
                row_count += 1
                if row_count == 1:
                    continue

                # Get exam data object
                exam_data = self.get_exam_data(row['Exam Name'])
                exam_data.candidates.append(row['Candidate ID'])

                if row['Grade'] == 'Pass':
                    exam_data.number_of_passed_exams += 1
                else:
                    exam_data.number_of_failed_exams += 1

                exam_data.best_score = max(int(row['Score']), exam_data.best_score)
                exam_data.worst_score = min(int(row['Score']), exam_data.worst_score)

        return self.data

    def get_exam_data(self, exam_name):
        if exam_name not in self.data:
            exam_data = ExamData(exam_name)
            self.data[exam_name] = exam_data
        return self.data[exam_name]


class ExamReport:
    def __init__(self, data):
        self.data = data

    def generate(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = [
                'Exam Name',
                'Number of Candidates',
                'Number of Passed Exams',
                'Number of Failed Exams',
                'Best Score',
                'Worst Score'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for key, exam_data in self.data.items():
                number_of_candidates = exam_data.get_number_of_candidates()
                writer.writerow({
                    'Exam Name': exam_data.exam_name,
                    'Number of Candidates': number_of_candidates,
                    'Number of Passed Exams': exam_data.number_of_passed_exams,
                    'Number of Failed Exams': exam_data.number_of_failed_exams,
                    'Best Score': exam_data.best_score,
                    'Worst Score': exam_data.worst_score
                })



exam_result_reader = ExamResultReader('exam_results.csv')
data = exam_result_reader.prepare_data()
exam_report = ExamReport(data)
exam_report.generate('exam_report.csv')