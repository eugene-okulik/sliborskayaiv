import os
import csv
import mysql.connector as mysql
import dotenv


dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)
query = '''
SELECT s.name, s.second_name,
       g.title as group_title,
       b.title as book_title,
       m.value as mark,
       l.title as lesson_title,
       s2.title as subject_title
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjets s2 ON s2.id = l.subject_id
'''
cursor.execute(query)
db_rows = cursor.fetchall()
db_data = {
    (
        row['name'],
        row['second_name'],
        row['group_title'],
        row['book_title'],
        row['subject_title'],
        row['lesson_title'],
        str(row['mark'])
    )
    for row in db_rows
}

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
data_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

csv_data = set()
with open(data_file_path, newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        csv_data.add((
            row['name'],
            row['second_name'],
            row['group_title'],
            row['book_title'],
            row['subject_title'],
            row['lesson_title'],
            row['mark_value']
        ))

missing = []
for row in csv_data:
    if row not in db_data:
        missing.append(row)

print(missing)
