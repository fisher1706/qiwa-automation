Description
---
Automated UI and API tests for Qiwa project.

High level project structure:

    .
    ├── data                    # Methods and files for generating various test data (separate for each service)
    ├── fixtures                # Fixture files related to all test types
    ├── helpers                 # Support methods to work with side libraries
    ├── src                     # Test framework source files with tests implementation
    │   ├── api                 # API tests source files
    │   ├── load                # Locust files for load testing
    │   └── ui                  # UI tests source files
    ├── tests                   # Test files stored in separate folder for each service
    │   ├── api                 # API tests
    │   └── ui                  # UI tests
    ├── utils                   # Different utils such as logger, assertions, discord manager, etc.
    ├── .env.demo               # Environment variables for run on demo env
    ├── .env.local.example      # Environment variables example for local run (replace this file with env.local)
    ├── .env.stage              # Environment variables for run on stage env
    ├── .gitignore              # List files and dirs ignored by git
    ├── .gitlab-ci.yml          # Config file for gitlab ci with pipeline for tests repository
    ├── Dockerfile              # DevOps config files
    ├── README.md               # Project description
    ├── config.py               # Key config file for the framework
    ├── conftest.py             # Pytest related fixtures
    └── pyproject.toml          # Project related dependencies

Preconditions (local)
---
Make sure you have `git`, `python3`, `pip3` and `poetry` installed. If not, please do so by following the instructions on the official resources.

Prepare local environment
---
* Clone the project to your local machine and navigate to the project directory:
```shell
git git@gitlab.qiwa.tech:takamol/qiwa/integration-testing/qiwa-automation.git
cd qiwa-automation
```
* Install and setup virtualenv for the project:
```shell
pip install virtualenv
virtualenv --python python3 venv
source venv/bin/activate
```
* Install all packages required for the tests run:
```shell
poetry install
```
----
Running tests locally
---
* Run all tests once the environment is ready the tests can be executed. Run the following command to do so:
```shell
pytest tests
```
* Run tests on specific environment

By default, tests are running on the **qiwa.tech** environment.
To run tests on the another env. create an `env.local` file and override domain variable with `qiwa.info` value.
Run `python config.py` to check the actual config values

* Run all tests for specific service 
```shell
pytest tests/ui/sso/sign_in
```

* Run tests with Allure reporting.
To run tests with Allure reporting add the argument `--alluredir=allure-results` to the command.
```shell
pytest tests/ui/sso/sign_in --alluredir=allure-results
```

View Allure report locally
---
If the tests were executed with `--alluredir` argument, allure results will be stored in the defined directory. To view allure results run the following command:
```shell
allure serve allure-results
```

Code checkers (pylint, black, isort)
---
* As a part of the test pipeline code verification is initialized on Merge request step.

Command to run pylint code checker:
```commandline
pylint data fixtures helpers src utils tests conftest.py
```

* To install Black locally execute `pip3 install black` command

Then it can be used to reformat code for the whole project or specific files:
```commandline
black conftest.py
```

* To install Isort locally execute `pip3 install isort` command

Then it can be used to sort imports alphabetically, and automatically separated into sections and by type for the whole project or specific files:
```commandline
isort .
```