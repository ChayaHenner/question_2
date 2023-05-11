# question_2

Flask Server for COVID Vaccination Data
This Flask server provides endpoints for retrieving COVID vaccination and diagnosis data of employees in a database. The server has the following endpoints:

/covid_vacs/<id>
This endpoint retrieves vaccination information of an employee with a specific ID. The response includes the vaccine number, date of vaccination, and manufacturer of each vaccine the employee received, if any.

/covid_dates/<id>
This endpoint retrieves the date range of positive COVID diagnosis and recovery of an employee with a specific ID.

/get_column/<id>/<request_num>
This endpoint retrieves a specific column from the employee table in the database. The request_num parameter specifies which column to retrieve, and id specifies the employee ID.

/all/<code>
This endpoint retrieves all employee data in the database. The code parameter should be set to 8068 to retrieve the data.

/new_employee
This endpoint is used for adding a new employee to the database. The employee data is passed in the request parameters.

The server uses SQLite to connect to the database and retrieve data. The database path is set to C:\Users\This_user\Desktop\hadassim_project\question_2_update\server.db and can be modified as needed.

Note that the server responds with error messages and appropriate HTTP status codes if invalid data or database errors occur.
  ![Screenshot 2023-05-11 212943](https://github.com/ChayaHenner/question_2/assets/132666389/e0a9a004-14c7-4567-a27e-d73e045bb76b)

  screenshots
  adding new employee to database
  ![image](https://github.com/ChayaHenner/question_2/assets/132666389/037aa11f-13c2-49f3-b27c-d85e208466db)
  
  
