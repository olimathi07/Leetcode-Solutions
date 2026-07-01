SELECT user_id,name,mail
FROM users
WHERE mail REGEXP'^[a-z][a-z0-9._-]*@leetcode\\.com$';

