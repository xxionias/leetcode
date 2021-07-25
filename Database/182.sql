-- 182. Duplicate Emails - Easy

-- Write a SQL query to find all duplicate emails in a table named Person.
--
-- +----+---------+
-- | Id | Email   |
-- +----+---------+
-- | 1  | a@b.com |
-- | 2  | c@d.com |
-- | 3  | a@b.com |
-- +----+---------+
-- For example, your query should return the following for the above table:
--
-- +---------+
-- | Email   |
-- +---------+
-- | a@b.com |
-- +---------+
-- Note: All emails are in lowercase.

-- Approach I: Using GROUP BY and a temporary table [Accepted]
SELECT Email
FROM (
  SELECT Email, COUNT(Email) AS num
  FROM Person
  GROUP BY Email
) AS statistic
WHERE num > 1;

-- Approach II: Using GROUP BY and HAVING condition
SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(Email) > 1;
