SELECT * 
FROM attendance;

ALTER TABLE attendance
DROP COLUMN first_name;

ALTER TABLE attendance
DROP COLUMN last_name;

SELECT COUNT(DISTINCT user_id)
FROM attendance;
-- Answer: 73

---------------------------------------
SELECT * 
FROM leave_requests;

ALTER TABLE leave_requests
DROP COLUMN first_name;

ALTER TABLE leave_requests
DROP COLUMN last_name;

ALTER TABLE leave_requests
DROP COLUMN time_start;

ALTER TABLE leave_requests
DROP COLUMN time_end;

ALTER TABLE leave_requests
DROP COLUMN timezone;

CREATE TABLE leave_reqs_cleaned AS
SELECT *, 
UNNEST(STRING_TO_ARRAY(REPLACE(REPLACE(dates,'[',''),']',''),',')) AS dates_cleaned 
FROM leave_requests;

SELECT * 
FROM leave_reqs_cleaned;

ALTER TABLE leave_reqs_cleaned
DROP COLUMN dates;

SELECT COUNT(user_id)
FROM leave_reqs_cleaned;
-- Answer: 90

-------------------------------
SELECT * 
FROM payroll;

ALTER TABLE payroll
DROP COLUMN first_name;

ALTER TABLE payroll
DROP COLUMN last_name;

--------------------------------
SELECT * 
FROM schedules;

CREATE TABLE schedules_dates_cleaned AS
SELECT *, 
UNNEST(STRING_TO_ARRAY(REPLACE(REPLACE(dates,'[',''),']',''),',')) AS dates_cleaned 
FROM schedules;

SELECT * 
FROM schedules_dates_cleaned;

CREATE TABLE sched_cleaned AS
SELECT *, 
UNNEST(STRING_TO_ARRAY(REPLACE(REPLACE(user_id,'{',''),'}',''),',')) AS user_id_cleaned 
FROM schedules_dates_cleaned;

SELECT * 
FROM sched_cleaned;

ALTER TABLE sched_cleaned
DROP COLUMN dates;

ALTER TABLE sched_cleaned
DROP COLUMN user_id;

SELECT COUNT(*) 
FROM sched_cleaned;
-- Answer: 195189

--------------------------------

SELECT * 
FROM users;

ALTER TABLE users
DROP COLUMN first_name;

ALTER TABLE users
DROP COLUMN last_name;

UPDATE users
SET department = 'Support Centre'
WHERE position = 'Admin Bisnis';

SELECT position, location, department
FROM users
WHERE position = 'Admin Bisnis'

UPDATE users
SET department = 'Medical'
WHERE location = 'Clinic';

SELECT position, location, department
FROM users
WHERE location = 'Clinic';

SELECT position, location, department
FROM users
WHERE location = 'Clinic';

UPDATE users
SET department = 'Pharmacy'
WHERE location = 'Nu Orange';

SELECT position, location, department
FROM users
WHERE location = 'Nu Orange';


