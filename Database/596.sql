-- 596. Classes More Than 5 Students - Easy

-- There is a table courses with columns: student and class
--
-- Please list out all classes which have more than or equal to 5 students.
--
-- For example, the table:
--
-- +---------+------------+
-- | student | class      |
-- +---------+------------+
-- | A       | Math       |
-- | B       | English    |
-- | C       | Math       |
-- | D       | Biology    |
-- | E       | Math       |
-- | F       | Computer   |
-- | G       | Math       |
-- | H       | Math       |
-- | I       | Math       |
-- +---------+------------+
-- Should output:
--
-- +---------+
-- | class   |
-- +---------+
-- | Math    |
-- +---------+
--
--
-- Note:
-- The students should not be counted duplicate in each course.

-- Solution 1:
SELECT class
FROM courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5
;

-- Solution 2:
SELECT
    class
FROM
    (SELECT
        class, COUNT(DISTINCT student) AS num
    FROM
        courses
    GROUP BY class) AS temp_table
WHERE
    num >= 5
;

-- Note: Make an alias of COUNT(student) ('num' in this case) so that you can use 
-- in the WHERE clause because it cannot be used directly over there.
