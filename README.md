To run this program:
1. python3 -m venv venv
2. source venv/bin/activate
3. Install pip, if you do not have it
4. pip install -r requirements.txt 
5. mysql -u root -p
6. (Enter a password)
7. CREATE DATABASE securepassDB;
8. ctrl + d
9. mysql -u root -p securepassDB < database/DDL.sql
10. python3 app.py


Problem Statement:

A small biotech company discovered a security breach that occurred over the weekend.
Following an investigation, it was found that the backup sample chamber was exposed due to a
weak user password within the login portal. Fortunately the consequences of the breach were
minimal, the company decided to place password standards for all employees and company
devices. Requirements such as: the use of a special character, combination of numbers and
letters, & a minimum length were discussed. Based on NordPass, an average individual
typically maintains around 100 passwords. Accounting for 100 employees and the average of
100 passwords, the database would have to handle 100,000+ entries. Recognizing that the
increased complexity demanded by the new standards would be difficult to remember, the
management team decided to develop an internal tool for generating passwords.


A password can only be created if the specified username already exists.

Example run:


<img width="915" alt="Screenshot 2025-01-19 at 10 36 12 PM" src="https://github.com/user-attachments/assets/af500597-d6b2-4701-928c-0ba6cd079f44" />
<img width="915" alt="Screenshot 2025-01-19 at 10 36 36 PM" src="https://github.com/user-attachments/assets/f2e62f14-702f-43b3-967a-ef58dee94608" />
<img width="906" alt="Screenshot 2025-01-20 at 12 18 44 AM" src="https://github.com/user-attachments/assets/b8299519-08bb-4b19-9f80-1ec3091154ee" />
<img width="881" alt="Screenshot 2025-01-20 at 12 27 16 AM" src="https://github.com/user-attachments/assets/71bf8d91-57eb-4b6e-9b93-8c3c40a5fbc5" />
<img width="916" alt="Screenshot 2025-01-20 at 12 27 31 AM" src="https://github.com/user-attachments/assets/04585160-0135-42dd-8229-958cff07eaa1" />
<img width="1023" alt="Screenshot 2025-01-20 at 12 27 50 AM" src="https://github.com/user-attachments/assets/3c541959-c4ae-4daa-aeff-65a681155022" />
<img width="1023" alt="Screenshot 2025-01-20 at 12 28 08 AM" src="https://github.com/user-attachments/assets/8a9023d5-55a1-4d29-9d47-36815662997c" />
<img width="1023" alt="Screenshot 2025-01-20 at 12 28 17 AM" src="https://github.com/user-attachments/assets/f5b91704-4399-4dec-b191-9951437f4598" />
<img width="915" alt="Screenshot 2025-01-19 at 10 40 51 PM" src="https://github.com/user-attachments/assets/0011af46-e13a-4fb0-9860-0538a4f2cc66" />
<img width="915" alt="Screenshot 2025-01-19 at 10 41 10 PM" src="https://github.com/user-attachments/assets/410ad916-5b6e-439c-ae77-20ba276f23de" />
<img width="915" alt="Screenshot 2025-01-19 at 10 41 17 PM" src="https://github.com/user-attachments/assets/a807c821-8aec-4fc7-849e-f623f67418b0" />




Some of the Database Tables:

<img width="245" alt="Screenshot 2025-01-19 at 10 47 48 PM" src="https://github.com/user-attachments/assets/95e13afa-6245-4e61-959a-0eb6013f8dd3" />
<img width="538" alt="Screenshot 2025-01-19 at 10 45 52 PM" src="https://github.com/user-attachments/assets/ab058950-d09a-4f65-980f-45514640c0d2" />
<img width="538" alt="Screenshot 2025-01-19 at 10 46 16 PM" src="https://github.com/user-attachments/assets/7f5c52ce-1359-4462-b3ae-000fc24de0af" />
<img width="538" alt="Screenshot 2025-01-19 at 10 46 41 PM" src="https://github.com/user-attachments/assets/4855b7d1-f737-4000-b687-98ea768c2d55" />
<img width="423" alt="Screenshot 2025-01-20 at 12 22 13 AM" src="https://github.com/user-attachments/assets/dc3d9dc6-f18d-426c-84da-08b6d42bae0b" />
<img width="491" alt="Screenshot 2025-01-20 at 12 20 39 AM" src="https://github.com/user-attachments/assets/ced1f600-aa30-45c9-b9cf-9f6242302eaf" />
<img width="488" alt="Screenshot 2025-01-19 at 10 49 08 PM" src="https://github.com/user-attachments/assets/cb62ae03-0ccd-4024-af39-62fa26a877fb" />



Key and ERD:


<img width="897" alt="Screenshot 2025-01-16 at 2 54 10 AM" src="https://github.com/user-attachments/assets/06f2a361-f502-49aa-ad5b-a70c0bf38573" />
<img width="884" alt="Screenshot 2025-01-16 at 2 54 50 AM" src="https://github.com/user-attachments/assets/37c2b116-bd9a-4005-84f3-bda64bb3f184" />
<img width="884" alt="Screenshot 2025-01-16 at 2 55 11 AM" src="https://github.com/user-attachments/assets/1d5aa04a-64f6-4a0e-86af-5d5c78d763bf" />
<img width="937" alt="Screenshot 2025-01-16 at 2 53 23 AM" src="https://github.com/user-attachments/assets/0f64638b-515b-4f60-b0ec-83d8b6833080" />
