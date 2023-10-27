SELECT * FROM Student WHERE rating >= 50;


SELECT * FROM Student WHERE balans = 0;


SELECT * FROM Student WHERE age BETWEEN 18 AND 30;


SELECT * FROM Student WHERE firstname LIKE 'A%';


SELECT student_id FROM Attendance WHERE add_date = CURRENT_DATE AND info = 'kelmadi';


SELECT * FROM Payment ORDER BY add_date DESC LIMIT 10;


