import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)


cursor = db.cursor(dictionary=True)


def create_data(cursor):
    cursor.execute("insert into students (name, second_name) values ('The Last', 'One')")
    student_id = cursor.lastrowid

    cursor.execute(f"insert into books (title, taken_by_student_id) "
                   f"values ('New_book', {student_id}), ('Nature and we', {student_id})")
    cursor.execute("insert into `groups` (title, start_date, end_date) "
                   "values ('Final', 'Sep 1, 2024', 'Aug 31, 2034')")
    group_id = cursor.lastrowid

    cursor.execute(f"update students set group_id = {group_id} where id = {student_id}")

    cursor.execute("insert into subjets (title) values ('Math in English')")
    math_id = cursor.lastrowid

    cursor.execute("insert into subjets (title) values ('English reading')")
    english_id = cursor.lastrowid

    cursor.execute("insert into subjets (title) values ('Biology for you')")
    biology_id = cursor.lastrowid

    cursor.execute(f"insert into lessons (title, subject_id) values ('Math part 1', {math_id})")
    lesson1_id = cursor.lastrowid
    cursor.execute(f"insert into lessons (title, subject_id) values ('Math part 2', {math_id})")
    lesson2_id = cursor.lastrowid
    cursor.execute(f"insert into lessons (title, subject_id) values ('English part 1', {english_id})")
    lesson3_id = cursor.lastrowid
    cursor.execute(f"insert into lessons (title, subject_id) values ('English part 2', {english_id})")
    lesson4_id = cursor.lastrowid
    cursor.execute(f"insert into lessons (title, subject_id) values ('Biology part 1', {biology_id})")
    lesson5_id = cursor.lastrowid
    cursor.execute(f"insert into lessons (title, subject_id) values ('Biology part 2', {biology_id})")
    lesson6_id = cursor.lastrowid

    insert_query = "insert into marks (value, lesson_id, student_id) values (%s, %s, %s)"
    values = [
        (8, lesson1_id, student_id),
        (9, lesson2_id, student_id),
        (10, lesson3_id, student_id),
        (10, lesson4_id, student_id),
        (9, lesson5_id, student_id),
        (8, lesson6_id, student_id)
    ]
    cursor.executemany(insert_query, values)
    return student_id


student_id = create_data(cursor)

db.commit()


def get_student_marks(cursor, student_id):
    cursor.execute(f"select * from marks m where student_id = {student_id}")
    print("Student's marks: ")
    print(cursor.fetchall())


def get_student_books(cursor, student_id):
    cursor.execute(f"select * from books b  where taken_by_student_id  = {student_id}")
    print("Student took the following books: ")
    print(cursor.fetchall())


def get_student_data(cursor, student_id):
    query = '''
    select s.name, s.second_name, 
    g.title as group_title,
    b.title as book_title,
    m.value as mark,
    l.title as lesson,
    s2.title as subject
    from students s
    join `groups` g on s.group_id = g.id
    join books b on s.id  = b.taken_by_student_id
    join marks m on s.id = m.student_id
    join lessons l on l.id = m.lesson_id
    join subjets s2 on s2.id = l.subject_id
    where s.id = %s
    '''
    cursor.execute(query, (student_id,))
    for row in cursor.fetchall():
        print(row)


get_student_marks(cursor, student_id)
get_student_books(cursor, student_id)
get_student_data(cursor, student_id)

db.close()
