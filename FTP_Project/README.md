# File Transfer, Validation and Storage Project
## Project background
<p>I completed this project as part of a team of 4 during an internship placement between years 1 and 2 of my Computer Science undergraduate degree. </p>
<p>On the instruction of the internship hosts, I have sanitised the content within this project folder, removing reference to whom the project was for and details of the other team members</p>

## Project overview
This project seeks to fulfil the requirements, as laid out in the specification provided, in order to produce a system that downloads requested csv files containing medical research data from an external FTP server, validate the format and contents of the files, and stores them in a calendar-based directory system. To do this, we have used python to create:
1. A [GUI](./main), which is used to request files for a particular date and report any errors with those files to the user.
2. An [FTP server](./server) to serve the files.
3. An [FTP client](./client) script used by the main GUI script of the program to request files from a specified date that match a valid file name format.
4. A [script](./validate_file) that checks the contents of the file meet the requirements laid out in the specification and fixes errors where possible.  This script creates an "info" file which is stored alongside each csv file to report any errors encountered, and sorts the files into an archive system based on their validity and the date on which they were created.
5. A thorough [testing suite](./test_plans), to ensure the robustness of our system.

An in-depth look into created classes and the functions that they entail can be found [here](./class_function_descriptors)

## My role / contribution
My main technical role during this project was to act as tester. I wrote the test plans and test scripts for all code produced as part of the main system. I then, if the fix was simple such as altering variable type, etc, either fixed the issue myself or worked with the owner of the erroneous peice of code to implement the most appropriate fix for our system.
The test plan which also contains the links to the scripts I created (which can also be found in this folder) can be found [here](./test_plans)

## Further information:
The below sections outline some useful information to reference if you were to run the system.

### Assumptions
<p>When interpreting the brief provided, the team member working on the file validation and archiving portion of the project, found that they needed to make some assumptions about what a "valid" file consisted of, based on the test data provided.  They are included below for clarity, and the code has been designed to be easily adaptable to any changes in requirements.</p>
<ol>
<li> Assume all files must have 10 rows (not including  the header)</li>

<li> Assume readings do not need ending 0s (e.g. 6 does not need to be stored as 6.000) - readings under 3dp are valid but above 3dp are not and should be rounded </li>

<li> Assume 0 and 10 are not valid readings (range is 0 < reading < 10, rather than 0<= reading <= 10) </li>

<li> Assume bad filenames handled by server</li>

<li> Assume batch_id can be 0</li>
</ol>
ile Transfer, Validation and Storage Project
## Project background
<p>I completed this project as part of a team of 4 during an internship placement between years 1 and 2 of my Computer Science undergraduate degree. </p>
<p>On the instruction of the internship hosts, I have sanitised the content within this project folder, removing reference to whom the project was for and details of the other team members</p>

## Project overview
This project seeks to fulfil the requirements, as laid out in the specification provided, in order to produce a system that downloads requested csv files containing medical research data from an external FTP server, validate the format and contents of the files, and stores them in a calendar-based directory system. To do this, we have used python to create:
1. A [GUI](./main), which is used to request files for a particular date and report any errors with those files to the user.
2. An [FTP server](./server) to serve the files.
3. An [FTP client](./client) script used by the main GUI script of the program to request files from a specified date that match a valid file name format.
4. A [script](./validate_file) that checks the contents of the file meet the requirements laid out in the specification and fixes errors where possible.  This script creates an "info" file which is stored alongside each csv file to report any errors encountered, and sorts the files into an archive system based on their validity and the date on which they were created.
5. A thorough [testing suite](./test_plans), to ensure the robustness of our system.

An in-depth look into created classes and the functions that they entail can be found [here](./class_function_descriptors)

## My role / contribution
My main technical role during this project was to act as tester. I wrote the test plans and test scripts for all code produced as part of the main system. I then, if the fix was simple such as altering variable type, etc, either fixed the issue myself or worked with the owner of the erroneous piece of code to implement the most appropriate fix for our system.
The test plan which also contains the links to the scripts I created (which can also be found in this folder) can be found [here](./test_plans)

## Further information:
The below sections outline some useful information to reference if you were to run the system.

### Assumptions
<p>When interpreting the brief provided, the team member working on the file validation and archiving portion of the project, found that they needed to make some assumptions about what a "valid" file consisted of, based on the test data provided.  They are included below for clarity, and the code has been designed to be easily adaptable to any changes in requirements.</p>
<ol>
<li> Assume all files must have 10 rows (not including  the header)</li>

<li> Assume readings do not need ending 0s (e.g. 6 does not need to be stored as 6.000) - readings under 3dp are valid but above 3dp are not and should be rounded </li>

<li> Assume 0 and 10 are not valid readings (range is 0 < reading < 10, rather than 0<= reading <= 10) </li>

<li> Assume bad filenames handled by server</li>

<li> Assume batch_id can be 0</li>
</ol>

### Error Code System
<p>In order to better inform a user on why a file was rejected or modified by the validation program, as well as to allow any issues to be reported by the GUI, a system of "error codes" was devised, as included below.  These codes are displayed to the user by the GUI, as well as included in an "info.txt" file stored in the archive alongside the files.</p>

- 000 - Valid File (Logged without preceding "Error")
- 100 - Empty File
- 101 - Header Only
- 200 - Incorrect Header
- 201 - Fatal Incorrect Header
- 300 - Missing Values
- 400 - Incorrect Number of Rows
- 500 - Invalid Batch ID
- 600 - Too Many Values (deprecated)
- 700 - Incorrect Timestamp
- 800 - Int, Not Float
- 801 - Incorrect Data Type
- 802 - Incorrect Rounding
- 803 - Value Out of Range

### Error Code System
<p>In order to better inform a user on why a file was rejected or modified by the validation program, as well as to allow any issues to be reported by the GUI, a system of "error codes" was devised, as included below.  These codes are displayed to the user by the GUI, as well as included in an "info.txt" file stored in the archive alongside the files.</p>

- 000 - Valid File (Logged without preceding "Error")
- 100 - Empty File
- 101 - Header Only
- 200 - Incorrect Header
- 201 - Fatal Incorrect Header
- 300 - Missing Values
- 400 - Incorrect Number of Rows
- 500 - Invalid Batch ID
- 600 - Too Many Values (deprecated)
- 700 - Incorrect Timestamp
- 800 - Int, Not Float
- 801 - Incorrect Data Type
- 802 - Incorrect Rounding
- 803 - Value Out of Range