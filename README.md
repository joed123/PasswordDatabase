To run this program:
1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt 
4. mysql -u root -p
5. (Enter a password)
6. CREATE DATABASE securepassDB;
7. ctrl + d
7. mysql -u root -p securepassDB < database/DDL.sql
8. python3 app.py



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




Example run:


<img width="915" alt="Screenshot 2025-01-19 at 10 36 12 PM" src="https://github.com/user-attachments/assets/af500597-d6b2-4701-928c-0ba6cd079f44" />
<img width="915" alt="Screenshot 2025-01-19 at 10 36 36 PM" src="https://github.com/user-attachments/assets/f2e62f14-702f-43b3-967a-ef58dee94608" />
<img width="915" alt="Screenshot 2025-01-19 at 10 36 57 PM" src="https://github.com/user-attachments/assets/9876d810-735a-4088-8f0f-ba70cf5e8df1" />
<img width="915" alt="Screenshot 2025-01-19 at 10 39 25 PM" src="https://github.com/user-attachments/assets/5df7fd8e-fd40-499b-a819-2a50dd71d51e" />
<img width="915" alt="Screenshot 2025-01-19 at 10 39 39 PM" src="https://github.com/user-attachments/assets/e237cab4-39ea-4174-806e-4ea6735f700a" />
<img width="915" alt="Screenshot 2025-01-19 at 10 39 50 PM" src="https://github.com/user-attachments/assets/3c2230a0-83d3-4fd6-923c-c337baba0a4c" />
<img width="915" alt="Screenshot 2025-01-19 at 10 40 00 PM" src="https://github.com/user-attachments/assets/a2482a1a-85b5-4dba-ba10-abc1219025de" />
<img width="915" alt="Screenshot 2025-01-19 at 10 40 17 PM" src="https://github.com/user-attachments/assets/d222dd28-be64-4707-aa93-f39877de3bcf" />
<img width="915" alt="Screenshot 2025-01-19 at 10 40 27 PM" src="https://github.com/user-attachments/assets/a7b189d8-8f41-4ff0-8cea-b855f99f550f" />
<img width="915" alt="Screenshot 2025-01-19 at 10 40 51 PM" src="https://github.com/user-attachments/assets/0011af46-e13a-4fb0-9860-0538a4f2cc66" />
<img width="915" alt="Screenshot 2025-01-19 at 10 41 10 PM" src="https://github.com/user-attachments/assets/410ad916-5b6e-439c-ae77-20ba276f23de" />
<img width="915" alt="Screenshot 2025-01-19 at 10 41 17 PM" src="https://github.com/user-attachments/assets/a807c821-8aec-4fc7-849e-f623f67418b0" />












Some of the Database Tables:


<img width="253" alt="Screenshot 2025-01-19 at 8 08 34 PM" src="https://github.com/user-attachments/assets/87a30098-3823-455e-9ff0-fd42b09dd693" />
<img width="529" alt="Screenshot 2025-01-19 at 8 12 32 PM" src="https://github.com/user-attachments/assets/1b67dd90-86f6-462e-a7cd-78267fea3af4" />
<img width="530" alt="Screenshot 2025-01-19 at 8 09 58 PM" src="https://github.com/user-attachments/assets/71660d62-7032-4042-aa59-e8e36fe33184" />
<img width="524" alt="Screenshot 2025-01-19 at 8 42 21 PM" src="https://github.com/user-attachments/assets/82589863-109e-4cef-9e7c-52631f34ee25" />
<img width="417" alt="Screenshot 2025-01-19 at 8 13 01 PM" src="https://github.com/user-attachments/assets/0b4bf7e9-07f4-415d-afa7-065fcdf7ba5a" />
<img width="517" alt="Screenshot 2025-01-19 at 8 13 10 PM" src="https://github.com/user-attachments/assets/4c5bed22-844e-45cf-8a70-0bc44cdf79f7" />
<img width="354" alt="Screenshot 2025-01-19 at 8 41 51 PM" src="https://github.com/user-attachments/assets/8b7f38ea-9760-4947-8c71-e4d39a5db0b6" />






Key and ERD:


<img width="897" alt="Screenshot 2025-01-16 at 2 54 10 AM" src="https://github.com/user-attachments/assets/06f2a361-f502-49aa-ad5b-a70c0bf38573" />
<img width="884" alt="Screenshot 2025-01-16 at 2 54 50 AM" src="https://github.com/user-attachments/assets/37c2b116-bd9a-4005-84f3-bda64bb3f184" />
<img width="884" alt="Screenshot 2025-01-16 at 2 55 11 AM" src="https://github.com/user-attachments/assets/1d5aa04a-64f6-4a0e-86af-5d5c78d763bf" />
<img width="937" alt="Screenshot 2025-01-16 at 2 53 23 AM" src="https://github.com/user-attachments/assets/0f64638b-515b-4f60-b0ec-83d8b6833080" />
