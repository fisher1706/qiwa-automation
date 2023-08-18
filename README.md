Description
---
Automated UI and API tests for Qiwa project

    .
    ├── fixtures                # Fixture files related to all test types
    ├── helpers                 # Support methods to work with side libraries 
    ├── infrastructure          # DevOps config files
    ├── src                     # Test framework source files with tests implementation
    │   ├── api                 # API tests source files
    │   └── ui                  # UI tests source files
    ├── test_data               # Methods and files for generating various test data
    ├── tests                   # test files
    │   ├── api                 # API tests
    │   └── ui                  # UI tests
    ├── .env             # Environment variables for local run 
    ├── .gitignore              # List files and dirs ignored by git
    ├── .gitlab-ci.yml          # Config file for gitlab ci with pipeline for tests repository
    ├── .pylintrc               # Pylint code formatting rules
    ├── CHANGELOG.md            # List of changes after each commit (not supported for a long time)
    ├── conftest.py             # Key config file for pytest project
    ├── docker-compose.yaml     # Docker compose for Allure and Selenium grid
    ├── Dockerfile              # DevOps config files
    ├── pytest.ini              # Pytest configuration
    ├── README.md               # Project description
    └── requirements.txt        # Project related packages

Preconditions (local)
---
Make sure you have `git`, `python3` and `pip3` installed. If not, please do so by googling and following the instructions on the official resources.

Prepare local environment
---
* Clone the project to your local machine and navigate to the project directory:
```shell
git clone git@gitlab.qiwa.tech:takamol/qiwa/integration-testing/qa-automation.git
cd qa-automation
```
* Install and setup virtualenv for the project:
```shell
pip install virtualenv
virtualenv --python python3 venv
source venv/bin/activate
```
* Install all packages required for the tests run:
```shell
pip install -r requirements.txt
```
----
Same actions you can de within PyCharm IDE via UI with hints

Running tests locally
---
###Run all tests
Once the environment is ready the tests can be executed. Run the following command to do so:
```shell
pytest features/tests
```
###Run tests on specific environment
By default, tests are running on the environment: https://auth.qiwa.tech
To run tests on the another env. add the argument: `--environment_url` with your environment value.
```shell
pytest features/tests --environment_url=https://auth.qiwa.info
```
###Run tests by specific test type for specific feature 
All tests are grouped by features using tag name `@pytest.mark.user_suite`. So to run specific tests by tag name use cli argument `-m` + tag value. 

**Please note that there are api and ui tests. It's highly recommended running ONLY `ui` OR `api` tests separately. Use the example below to do so:**
```shell
# run ui tests for user
pytest features/tests -m "user_suite and ui"
# run api tests for auth
pytest features/tests -m "auth_suite and api"
```
> P.S. Available suites are listed in `pytest.ini` file in project root dir.
###Run tests with Allure reporting
To run tests with Allure reporting add the argument `--alluredir=allure-results` to the command.
```shell
pytest features/tests --alluredir=allure-results
```

View Allure report locally
---
If the tests were executed with `--alluredir` argument, allure results will be stored in the defined directory. To view allure results run the following command:
```shell
allure serve allure-results
```

Allure Docker Service setup (not locally):
---
Current version of Allure report is running as Allure server and supports multiple projects. It means that by one URL user can access to the various reports for the different types of tests.

Allure documentation:<br>
https://github.com/fescobar/allure-docker-service

Docker image with actual Allure server:<br>
`frankescobar/allure-docker-service:2.13.3`

<h3>How to send report files to the Allure server</h3>
All report files in `.xml` format (also `.png` and `.properties`) are stored in local directory `allure-results` after tests run.
Test results are sent to Allure service automatically on ci/cd side right after tests execution.

Code checker (pylint)
---
As a part of the test pipeline code verification is initialized on Merge request step.
`pylint` config file is located in the project root directory in file `.pylintrc`.

Command to run code checker:
```commandline
pylint fixtures helpers src test_data tests conftest.py
```

Discord notifications
-
### Requirements:

1. Tests are triggered by tags with following template:<br>
```pytest tests/{test_type} -m {project_name} {test_type} daily ...```<br>
    **where**:<br>
    `project_name`: um, core, up, etc...<br>
    `test_type`: ui, api<br>

2. Discord channels created with name template for each suite: `{project_name}-{test_type} 
-daily`
3. Discord channel has created Webhook. `Edit channel -> Integrations -> Webhooks -> New Webhook`
4. There are options in `TestReportManager` to control output:

```python
self.__with_stacktrace = False  # show detailed stacktrace for failed tests 
self.__failed_only = True  # show only failed tests
```

### Steps for adding
All tests should have tags: `ui, api, daily` accordingly
- Copy files to your project:
  - `/fixtures/reports.py`
  - `/helpers/discord_report.py` - update suite name according to project name
  - `/helpers/decorators.py`
- Update files:
  - `conftest.py`
    - add `fixtures.reports` to `pytest_plugins` list in `conftest.py`
    - add code line to `pytest_addhooks` inside `if '-m'`
  ```python
  os.environ["SUITE_NAME"] = "-".join(suite_name.split(" and "))
  ```
  - `gitlab-ci.yaml` - tests should start with tags in the following order: 
  ```python
    pytest tests -m "ui and daily"
    # or
    pytest tests -m "api and daily"
  ```
  - add Discord hooks to the test data file. `discord_url` can be requested in AQA lead
  ```python
    DISCORD_HOOKS = {
        "demo": {
            "{project_name}-ui-daily": {discord_url},
            "{project_name}-api-daily": {discord_url}
        }
    }
  ```