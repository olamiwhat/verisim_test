
## Install dependencies

`pip install -r requirements.txt`

## Tools
 -python
 -sqlite3
 -flask

## Done
 - Application was created in a virtual env (verisim)
 - database was set up
 - application runs on localhost:5000
 - basic front end was setup to enter drug information
 - post functionality was defined
 - read functionality was defined
 
 ## Still To Do
 - Delete functionality

 This will be achieved by:
 1. have a delete link on each drug component
 2. have the link forwarded to the delete_drug.html page taking along the drug_name
 3. on the delete route handler check, query the database and check if the drug name is in the database
 4. if drug name in database, delete drug and redirect to home page
 5. if delete unsuccessful, send message and redirect to homepage

 - update functionality
 This will be achieved by:
 1. have a edit link on each drug component
 2. have the link forwarded to the edit_drug page taking along the drug_name
 3. on the edit route handler, check what attributes were sent to be edited
 4. update the database with these attributes
 5, redirect to home page
 6. if update unsuccessful, send a message and redirect to edit page.


 ## stretch
  - Revisit database schema. I know some of the drug attributes will exhibit a one to many relationship, so table will need to be normalized.
