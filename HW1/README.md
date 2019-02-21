# Homework 1
**Deadline: 02/15/2018 5pm ET **

This assignment helps you review basic Python objects types: numbers, strings, lists and dictionaries and operations on these objects.

## Instructions:

* Click on the link that I shared with you on canvas. That will create a private Github repository for you. Once you have that repository, clone it to your local by using "git clone".

* Create a virtual environment by running "mkvirtualenv hmw1_env". DO NOT BUILD YOUR CODE TO YOUR SYSTEM'S PYTHON.

* Activate your new environment by running "workon hmw1_env". If you use PyCharm, you should also change the interpreter to this virtual environment.

* You are supposed to modify the file "my_answers.py" in src/mypkg. You should be able to run this file as you are editing it but tests will not be run yet.

* In order to run the tests, make sure you have pytest installed in your environment. Simply type "pip3 install pytest".

* In your terminal, cd to homework1-YourGithubID, type "pip install -e ." to build your program.

* In your terminal, cd to homework1-YourGithubID and type "pytest". It should run all the tests for this assignment and you should be able to see the output.

* Now, "git commit" ONLY YOUR my_answer.py and push it to your private Github repository. DO NOT ADD OTHER FILES generated by pycharm or your build. Travis-CI will run the tests you ran in your local in the cloud. 

* As an engineer, you are responsible for an end-to-end process of submission of your code. Failures in Travis-CI will affect your grade even if all the tests pass in your local.

* You should see a green tick in your github repository if all your tests passed. However, we will test your assignment using some extra tests hidden from you. Therefore, you should write code that passes all the tests you see but it should pass any other extra tests.

* You can run "deactivate" to deactivate the environment and delete it you just created by running "rmvirtualenv hmw1_env".