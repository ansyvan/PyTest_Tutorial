# PyTest-Tutorial

This tutorial was conducted during the QA Automation Course. It consists of the mandatory part and the individual tasks which I developed by myself to practice testing skills on API, Database and UI testing. That part of code is highlighted by comments.

Mandatory Part:

<h2>Project Task 1</h2>

Create the folder and file structure for the framework.

In the cloned GitHub repository, create the following hierarchy of files and folders, which we will consider as the initial structure of the framework:

Folder structure from the root directory of the project:

<br/>/config
<br/>/modules
<br/>/modules/common
<br/>/modules/ui
<br/>/modules/ui/page_objects
<br/>/modules/api
<br/>/modules/api/clients
<br/>/tests
<br/>/tests/ui
<br/>/tests/api

File structure from the root directory of the project:

<br/>/config/config.py
<br/>/modules/common/__init__.py
<br/>/modules/ui/page_objects/__init__.py
<br/>/modules/api/clients/__init__.py
<br/>/tests/ui/test_ui.py
<br/>/tests/api/test_api.py


<h2>Project Task 2</h2>

To develop tests using the `pytest` module, fixtures, and markers, follow these requirements:

1. Markers `check` and `change` are registered in the `pytest.ini` file.

2. In the `conftest.py` file, describe the `User` class:
  - Use the constructor to set the name and second_name fields with default values as `None`.
  - The class has a `create` method. This method sets the `name` and `second_name` fields with your name and surname.
  - The class has a `remove` method. This method sets the `name` and `second_name` fields to an empty string.

3. In the `conftest.py` file, describe the `user` fixture. This fixture:
  - Creates an object of the `User` class.
  - Calls the `create` method of the object.
  - Returns the object after calling the `create` method to the tests.
  - After the test execution, calls the `remove` method of the object.

4. In the `/tests/api/test_fixtures.py` file, create the test `test_change_name`:
  - The test has a `check` marker.
  - The test has a `check` marker.
  - It checks that the `name` field of the `user` object matches the expected value.

5. In the `/tests/api/test_fixtures.py` file, create the test `test_change_second_name`:
  - The test has a `check` marker.
  - It uses the `user` fixture.
  - It checks that the `second_name` field of the `user` object matches the expected value.

6. In the `/tests/api/test_api.py` file, create the test `test_remove_name`:
  - The test has a `change` marker.
  - It uses the `user` fixture.
  - As the first step, the test changes the `name` field of the `user` object to an empty string.
  - As the second step, the test checks that the changes occurred and are correct.

7. In the `/tests/api/test_api.py` file, create the test `test_name`:
  - The test has a `check` marker.
  - It uses the `user` fixture.
  - It checks that the `name` field of the `user` object matches the expected value.

8. In the `/tests/api/test_api.py` file, create the test `test_second_name`:
  - The test has a `check` marker.
  - It uses the `user` fixture.
  - It checks that the `second_name` field of the `user` object matches the expected value.


<h2>Project Task 3</h2>

Develop tests for testing the HTTP protocol using the `pytest` and requests modules, using fixtures and markers.

In the cloned GitHub repository, develop tests using the pytest and requests modules that meet the following requirements:

1. The `http` marker is registered in the `pytest.ini` file

2. In the file `/tests/test_http.py`, create the `test_first_request`:
  - The test has the `http` marker
  - As the first step, the test sends an `HTTP GET` request to the address https://api.github.com/zen and stores the server's response in a variable.
  - As the second step, the test prints the text attribute of the server's response to the screen using f-strings.

3. In the file `/tests/test_http.py`, create the test `test_second_request`:
  - The test has the `http` marker
  - As the first step, the test sends an `HTTP GET` request to the address https://api.github.com/users/defunkt and stores the server's response in a variable
  - The test checks that the name attribute of the response body from the server corresponds to the value `Chris Wanstrath`.
  - The test checks that the status code of the response from the server corresponds to the number `200`.
  - The test checks that the Server header of the response from the server corresponds to the value `GitHub.com`.

4. In the file `/tests/test_http.py`, create a test named `test_status_code_request`:
  - The test should have the `http` marker.
  - In the first step, the test sends an `HTTP GET` request to the address https://api.github.com/users/sergii_butenko and stores the server's response in a variable.
  - The test verifies that the status code of the server's response corresponds to the number `404`.


<h2>Project Task 4</h2>

Develop tests for testing the `Github API` by creating your own API client, using the GitHub API documentation https://docs.github.com/en/rest/users/users?apiVersion=2022-11-28, and the pytest and requests modules.

In the cloned repository, develop tests using the `pytest` and requests modules that meet the following requirements:

1. The `api` marker is registered in the `pytest.ini file`.

2. In the file `/modules/api/clients/github.py`, create a class `GitHub`.
  - The method description includes a mandatory parameter `username`.
  - In the body of the method, the `URL` to which the HTTP request should be sent is formed. The logic of forming the URL is to concatenate two strings:
      - https://api.github.com/users/
      - The value of the `username` parameter
      - In the body of the method, an HTTP request with the `GET` method is sent to the `URL` from the previous step.
      - The method returns the body of the response from the server in json format.
  - The method description includes a mandatory parameter `name`.
  - In the body of the method, an `HTTP` request with the `GET` method is sent to the `URL` "https://api.github.com/search/repositories" with the query string parameter `q`, the value of which is equal to the value of the name parameter of the method.
  - The method returns the body of the response from the server in json format.
    1. The class has an object method `get_user`
    2. The class has an object method `search_repo`
    
3. In the `conftest.py` file, describe the `github_api` fixture. This fixture:
  - Creates an object of the `GitHub` class.
  - Returns the created object to the tests.

4. In the file `/tests/api/test_github_api.py`, create the test `test_user_exists`:
  - The test has the `api` marker.
  - Uses the `github_api` fixture.
  - In the body of the test, use the `get_user` method of the `github_api` fixture.
  - Use the `username` for the search: `defunkt`.
  - Verify that the body of the response from the server has an attribute `login`, the value of which should be equal to `defunkt`.

5. In the file `/tests/api/test_github_api.py`, create the test `test_user_not_exists`:
  - The test has the `api` marker.
  - Uses the `github_api` fixture.
  - In the body of the test, use the `get_user` method of the `github_api` fixture.
  - Use the `username` for the search: `butenkosergii`.
  - Verify that the body of the response from the server has an attribute message, and its value should be equal to `Not Found`.

6. In the file `/tests/api/test_github_api.py`, create the test `test_repo_can_be_found`:
  - The test has the `api` marker.
  - Uses the `github_api` fixture.
  - In the body of the test, use the `search_repo` method of the `github_api` fixture.
  - Use the repository `name` for the search: `become-qa-auto`.
  - Verify that the body of the response from the server has an attribute `total_count`, and its value should be equal to the expected value at the time of test creation, for example, `25`.

7. In the file `/tests/api/test_github_api.py`, create the test `test_repo_cannot_be_found`:
  - The test has the `api` marker.
  - Uses the `github_api` fixture.
  - In the body of the test, use the `search_repo` method of the `github_api` fixture.
  - Use a repository `name` for the search that does not exist at the time of test creation, for example, `sergiibutenko_repo_non_exist`.
  - Verify that the body of the response from the server has an attribute `total_count`, and its value should be `0`.

8. In the file `/tests/api/test_github_api.py`, create the test `test_repo_with_single_char_be_found`:
  - The test has the `api` marker.
  - Uses the `github_api` fixture.
  - In the body of the test, use the `search_repo` method of the `github_api` fixture.
  - Use the repository `name` for the search: `s` or any other name consisting of a single character.
  - Verify that the body of the response from the server has an attribute `total_count`, and its value should not be `0`.


<h2>Project Task 5</h2>

In the cloned repository, develop tests using the `pytest` and `sqlite3` modules, meeting the following requirements:

1. The marker `database` is registered in the `pytest.ini` file.

2. In the file `/modules/common/database.py`, create the `Database` class.
  - The class has a constructor where two object attributes are initialized:
    1. `self.connection` - an object that implements a connection to the database
    2. `self.cursor` - the cursor of the `self.connection` object
  - The class has an object method `test_connection`:
    1. The method executes an SQL query `SELECT` `sqlite_version();`
    2. The result of the method is the version of the database printed to the terminal.
  - The class has an object method `get_all_users`:
    1. The method should return the values of the `name`, `address`, and `city` fields for all users from the customers table.
  - The class has an object method `get_user_address_by_name`:
    1. The method has a mandatory parameter `name`.
    2. The method should return the values of the `address`, `city`, `postalCode`, and `country` fields for the user with the specified name from the `customers` table.
  - The class has an object method `update_product_qnt_by_id`:
    1. The method has mandatory parameters `product_id`, `qnt`.
    2. The method should change the quantity of the product with the specified `product_id` in the products table to the value specified in the `qnt` parameter.
  - The class has an object method `select_product_qnt_by_id`:
    1. The method has a mandatory parameter `product_id`.
    2. The method should return the quantity of the product with the specified `product_id`, a unique value from the products table.
  - The class has an object method `insert_product`:
    1. The method has mandatory parameters `product_id`, `name`, `description`, `qnt`.
    2. The method should insert or replace data in the `products` table for the `id`, `name`, `description`, and `quantity` columns. Data should be taken from the `product_id`, `name`, `description`, and `qnt` parameters.
  - The class has an object method `delete_product_by_id`:
    1. The method has a mandatory parameter `product_id`.
    2. The method should delete the product with the specified `product_id`, a unique value, from the products table.
  - The class has an object method `get_detailed_orders`:
    1. Using the `JOIN` command and tables `orders`, `customers`, `products`, return the following information from the `orders` table in the corresponding order: `unique order number`, `customer name`, `ordered product name`, `ordered product description`, `order date`.

3. In the file `/tests/database/test_database.py`, create the test `test_database_connection`:
  - The test has the `database` marker.
  - In the test body, create an instance of the `Database` class.
  - In the test body, execute the `test_connection` object method.

4. In the file `/tests/database/test_database.py`, create the test `test_check_all_users`:
  - The test has the `database` marker.
  - In the test body, create an instance of the `Database` class.
  - In the test body, execute the `get_all_users` object method.
  - Print the result of executing the `get_all_users` object method to the terminal.

5. In the file `/tests/database/test_database.py`, create the test `test_check_user_sergii`:
  - The test has the `database` marker.
  - In the test body, create an instance of the `Database` class.
  - In the test body, execute the `get_user_address_by_name` object method with the parameter `name = Sergii`.
  - Verify that the data returned by the `get_user_address_by_name` method corresponds to the following data:
    ```
    1. Maydan Nezalezhnosti 1
    2. Kyiv
    3. 3127
    4. Ukraine
    ```

6. In the file `/tests/database/test_database.py`, create the test `test_product_qnt_update`:
  - The test has the `database` marker.
  - In the test body, create an instance of the `Database` class.
  - In the test body, execute the `update_product_qnt_by_id` object method with the parameter `values product_id = 1` and `qnt = 25`.
  - Verify that after updating the data, the quantity of the product with the unique number `1` is equal to `25`.

7. In the file `/tests/database/test_database.py`, create the test `test_product_insert`:
  - The test has the `database` marker.
  - In the test body, create an instance of the `Database` class.
  - In the test body, execute the `insert_product` object method with the parameter values `product_id = 4`, `name = печиво`, `description = солодке`, `qnt = 30`.
  - Verify that after updating the data, the quantity of the product with the unique number `4` is equal to `30`.

8. In the file `/tests/database/test_database.py`, create the `test test_product_delete`:
  - The test has the `database` marker.
  - In the test body, create an instance of the `Database` class.
  - In the test body, create test data by creating a product in the `products` table with the parameter values `product_id = 99`, `name = тестові`, `description = дані`, `qnt = 999`.
  - In the test body, delete data from the `products` table with the parameter value `product_id = 99`.
  - Verify that the number of rows found is equal to `0`.

9. In the file `/tests/database/test_database.py`, create the test `test_detailed_orders`:
  - The test has the `database` marker.
  - In the test body, create an instance of the `Database` class.
  - In the test body, print to the terminal the result of executing the `get_detailed_orders` method of the `Database` class object. 
  - Verify that the number of found results is equal to `1`.
  - Verify that the data returned by the `get_detailed_orders` method corresponds to the following data:
    ```
    1. 1
    2. Sergii
    3. солодка вода
    4. з цукром
    ```

<h2>Project Task 6</h2>

In the cloned repository, develop tests using the `pytest` and `selenium` modules that meet the following requirements:

1. The `ui` marker is registered in the `pytest.ini` file.

2. In the `modules/ui/page_object` directory, create a file named `base_page.py`, and define a class named `BasePage` in it. 
  - In the class constructor, initialize an object for communication with the web driver.
  - The class should have a close method whose task is to close the open browser.

3. In the `modules/ui/page_object` directory, create a file named `sign_in_page.py`, and in it, define a class named `SignInPage`. 
  - The `SignInPage` class should inherit from the `BasePage` class.
  - In the class constructor, call the constructor of the parent class.
  - Implement a method of the object that takes `username` and `password` as parameters. The task of the method is to enter the `username` into the email field, the `password` into the password field, and click the sign-in button.
  - Implement a method of the object that checks whether the page title matches the expected title.

4. In the `tests/ui` directory, create a file named `test_ui_page_object.py`. In this file, create a test that:
  - Has the `ui` marker.
  - Performs the following steps:
    1. Opens the `Sign In` page.
    2. Enters incorrect data into the `username` and `password` fields.
    3. Checks whether the page title matches the expected title.
    4. Closes the browser.
