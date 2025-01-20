To run this program:
1. python3 -m venv venv
2. source venv/bin/activate
3. Install pip if you do not have it
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


A password can only be created if the user already exists.

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

<img width="245" alt="Screenshot 2025-01-19 at 10 47 48 PM" src="https://github.com/user-attachments/assets/95e13afa-6245-4e61-959a-0eb6013f8dd3" />
<img width="538" alt="Screenshot 2025-01-19 at 10 45 52 PM" src="https://github.com/user-attachments/assets/ab058950-d09a-4f65-980f-45514640c0d2" />
<img width="538" alt="Screenshot 2025-01-19 at 10 46 16 PM" src="https://github.com/user-attachments/assets/7f5c52ce-1359-4462-b3ae-000fc24de0af" />
<img width="538" alt="Screenshot 2025-01-19 at 10 46 41 PM" src="https://github.com/user-attachments/assets/4855b7d1-f737-4000-b687-98ea768c2d55" />
<img width="423" alt="Screenshot 2025-01-19 at 10 48 24 PM" src="https://github.com/user-attachments/assets/686483b8-5227-4b47-b183-ed43c48032fd" />
<img width="488" alt="Screenshot 2025-01-19 at 10 48 49 PM" src="https://github.com/user-attachments/assets/a979b269-d32d-485c-9661-963349944746" />
<img width="488" alt="Screenshot 2025-01-19 at 10 49 08 PM" src="https://github.com/user-attachments/assets/cb62ae03-0ccd-4024-af39-62fa26a877fb" />



Key and ERD:


<img width="897" alt="Screenshot 2025-01-16 at 2 54 10 AM" src="https://github.com/user-attachments/assets/06f2a361-f502-49aa-ad5b-a70c0bf38573" />
<img width="884" alt="Screenshot 2025-01-16 at 2 54 50 AM" src="https://github.com/user-attachments/assets/37c2b116-bd9a-4005-84f3-bda64bb3f184" />
<img width="884" alt="Screenshot 2025-01-16 at 2 55 11 AM" src="https://github.com/user-attachments/assets/1d5aa04a-64f6-4a0e-86af-5d5c78d763bf" />
<img width="937" alt="Screenshot 2025-01-16 at 2 53 23 AM" src="https://github.com/user-attachments/assets/0f64638b-515b-4f60-b0ec-83d8b6833080" />
