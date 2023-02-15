-- This converts the databse from utf8 to utf8mb4
ALTER TABLE first_table
CHANGE name name varchar(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
ALTER TABLE  first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
ALTER DATABASE hbtn_0c_0
CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;
