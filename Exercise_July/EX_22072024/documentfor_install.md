**pytest** used for run the program
- **pip install pytest** for installing the pytest
- file name should be **test_name.py**
- test name **test_name_of_test():**
- Assert means assertion 
- **Assert expected result= actual result**
## Pytest command
- **pytest -h** used for help
- **pytest -k "18"** means i want the file to run who  contain 18 number
- **pytest -m "smoke" path of the file** to run specific file who has smoke in it
- to find path right click-- copy path/reference --- path from content root 
- why we mark, because if there 100 test case 20 mark as smoke, 25 sanity test case, 55 regression
- to divide test case into smoke- create, regression-put, patch, , snaity test
-  pip install allure-pytest
## how to install allure 
- 2 steps run your testcase, see your report, second command show your result, it will create  temporary directotry and it will give ip address
 #### Run the command- pytest Automation_testing_july/test_lab180.py --alluredir=allure_result
 then run this command-allure serve allure_result
- html report- basic report
- allure report- its an open source report, used in java,python,js, ruby and many more
- newman report - is applicable only for postman only, its a commandlin tool used to run postman collection, newman html extra- report plugin


- pytest
- easy test creation
- plugin- pytest html -allure report
- assertions ar=er
# how to add request module to the project
- pip install requests
its created 1995
- pip is python package  it means we only want pytest module only, or if csv file, excel, machine learning, vpn,selenium, playwrite, performance related module 1000 -1000 is there
- 
- pytest Automation_testing_july/test_lab180.py --alluredir=allure_result -s
- -s helps you to print the details by print command
-  allure generate --clean - for clearing the data
- 