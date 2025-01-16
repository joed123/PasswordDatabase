SELECT * FROM Users;

SELECT * FROM Passwords;

SELECT * FROM Password_Generator_Rules;

SELECT * FROM Password_Categories;

SELECT * FROM Password_Histories;


-- Insert a new user

INSERT INTO Users (user_id, email, username, last_login_date) 
VALUES (:user_id, :email, :username, :last_login_date)

--Insert password_generator_rules

INSERT INTO Password_Generator_Rules (password_length, allowed_characters, require_uppercase, require_lowercase, require_digits, require_special_characters) 
VALUES (:password_length, :allowed_characters, :require_uppercase, :require_lowercase, :require_digits, :require_special_characters)

--Insert a new password

INSERT INTO Passwords (password_id, password_value, created_at, strength, user_id) 
VALUES (:password_value, :created_at, :strength, :user_id)

-- Insert Password_Categories 

INSERT INTO Password_Categories (category_id, category_name) 
VALUES (:category_name)

-- Insert Password_Categories_Junction

INSERT INTO Password_Categories_Junction (password_id, category_id) 
VALUES (:password_id, :category_id)

--Insert password_history

INSERT INTO Password_Histories (historyid, user_id, password_id, old_password_value, change_date, user_user_id) 
VALUES (:old_password_value, :change_date)

-- update Password_Generator_Rules rules 

UPDATE Password_Generator_Rules SET password_length = :password_length_Input, allowed_characters
= :allowed_characters_Input, require_uppercase = :require_uppercase_Input, require_lowercase = :require_lowercase_Input, require_digits = :require_digits_Input, require_special_characters = :require_special_characters_Input 
WHERE user_id = :password_idInput;

-- update Passwords

UPDATE Passwords SET password_id = :password_id_Input, password_value = :password_value_Input, created_at = :created_at_Input, strength = :strength_Input 
WHERE password_id = :password_idInput;

--Update Password_Categories

UPDATE Password_categories SET category_id = :category_id_Input, category_name
= :category_name_Input 
WHERE category_id = :category_idInput;

--Update Password_Categories_Junction

UPDATE Password_Categories_Junction SET category_id = :category_id_Input, password_id_name= :password_id_Input 
WHERE password_id = :password_idInput, category_id = :category_idinput;

-- Delete Users

DELETE FROM Users 
WHERE user_id = :user_idInput
-- Delete Passwords 

DELETE FROM Passwords 
WHERE password_id = :password_idInput

-- Delete Password_Categories

DELETE FROM Password_Categories 
WHERE :category_id = category_id_Input

-- Delete Password_Generator_Rules

DELETE FROM Password_Generator_Rules
WHERE user_id = :user_idInput

-- Grab Password and its category 

SELECT Passwords.password_value, Password_Categories.category_name FROM Passwords 
INNER JOIN Password_Categories_Junction  
ON Passwords.password_id = Password_Categories_Junction.passwords_password_id 
WHERE Password_Categories.category_id = :inputid