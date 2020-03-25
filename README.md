# MindK Python TA starter Kit

Description
=============
Test Automation Framework using selenium and Python with the below features:

* Framework is based on page object model.
* Faker and factory to generate test data.
* Reporting using Allure report.


Install dependencies
=====================
* Install the depended packages in ``requirements.txt`` using ``pip3 install -r requirements.txt``

Run Automated Tests
=====================

To run selected test without Allure report you need to set pytest as default test runner in Pycharm first
```
$ pytest ./path-to-test
```
After that you just need to choose one of the tests from "tests" directory and click "Run test" green arrow. There are 2 versions of test in each test file. In general test cases you can easily modify test inputs. Data-driven tests base on xlsx files from [utils](utils) directory. 

Generate Test Report
=====================

To generate all tests report using Allure you need to run tests by command first:
```
$ pytest ./path-to-test --alluredir=<reports directory path>
```
After that you need to use command (`allure cli` should be installed):
```
$ allure serve <reports directory path>
```


How to install virtualenv:
=====================

You can install requirements and execute tests not globally on your system, but using python virtual environment

#### Install **pip** first

    sudo apt-get install python3-pip

#### Then install **virtualenv** using pip3

    sudo pip3 install virtualenv 

#### Now create a virtual environment 

    virtualenv venv 

>you can use any name insted of **venv**

#### You can also use a Python interpreter of your choice

    virtualenv -p /usr/bin/python2.7 venv
  
#### Active your virtual environment:    
    
    source venv/bin/activate
    
#### Using fish shell:    
    
    source venv/bin/activate.fish

#### To deactivate:

    deactivate

#### Create virtualenv using Python3
    virtualenv -p python3 myenv

#### Instead of using virtualenv you can use this command in Python3
    python3 -m venv myenv