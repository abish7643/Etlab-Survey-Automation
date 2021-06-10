from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common import exceptions
import time


class EtlabBot:
    def __init__(self, username, password):
        print("-------------------------------------")
        print("------ Etlab Survey Automation ------")
        print("-------------------------------------")
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self, userLoginLink=None):

        if userLoginLink is None:
            userLoginLink = "https://sctce.etlab.in/user/login"

        bot = self.bot
        bot.get(userLoginLink)
        print("------------ Delay of 5s -----------")
        time.sleep(5)
        email = bot.find_element_by_id('LoginForm_username')
        password = bot.find_element_by_id('LoginForm_password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        print("------------ Logging In ------------")
        print("------------ Delay of 5s -----------")
        time.sleep(5)

    def doTeacherEvaluationSurveys(self, surveyToBeDone, AnswerValueHTML, delay):
        bot = self.bot
        bot.get(surveyToBeDone)

        print("------------ Delay of {}s -----------".format(delay))  # Wait Till Survey Page Loads
        time.sleep(delay)

        rows = bot.find_elements_by_id("section-form")
        totalSubjects = len(rows)
        print('------ {} Subjects To Be Done -------'.format(totalSubjects))

        totalQuestions = len(AnswerValueHTML)
        print('----- {} Questions To Be Done ------'.format(totalQuestions))

        # Iterating Through Each Subject
        subjectIterator = 0
        while subjectIterator < len(range(totalSubjects)):
            print('============= Subject {} ============'.format(subjectIterator + 1))

            # Selects The Button "Answer Questions"
            currentSubjectName = 'yt{}'.format(subjectIterator)

            # Click On Subject
            subjectTimeout = False
            try:
                currentSubjectSelector = WebDriverWait(bot, 15).until(
                    expected_conditions.presence_of_element_located((By.NAME, currentSubjectName))
                )
                currentSubjectSelector.click()
            except exceptions.TimeoutException:
                print("-------------- Timeout --------------")
                subjectTimeout = True

            if subjectTimeout:
                print("-------------- Redoing --------------")
            else:
                # wait till answer loads
                print("------------ Delay of {}s -----------".format(delay))
                time.sleep(delay)

                # Iterating Through Each Question
                questionIterator = 0
                while questionIterator < len(AnswerValueHTML):
                    print('------------ Question {} ------------'.format(questionIterator + 1))

                    # Click on Answer
                    questionTimeout = False
                    try:
                        answerSelector = WebDriverWait(bot, 15).until(
                            expected_conditions.presence_of_element_located((
                                By.XPATH, ".//input[@value='{}']".format(AnswerValueHTML[questionIterator]))
                            )
                        )
                        answerSelector.click()
                    except exceptions.TimeoutException:
                        print("-------------- Timeout --------------")
                        questionTimeout = True

                    if questionTimeout is not True:
                        questionIterator += 1
                    else:
                        print("-------------- Redoing --------------")

                print("------- Selected Req Answers -------")

                # Wait to Verify
                print("------------ Delay of {}s -----------".format(delay))
                time.sleep(delay)

                # Name Attribute Of Submit Button From HTML
                submitButtonName = 'yt0'
                submitButton = bot.find_elements_by_name(submitButtonName)
                submitButton[0].click()

                # Next Subject
                subjectIterator += 1

                print("------------ Delay of {}s -----------".format(delay))
                time.sleep(delay)

        print("------------------------------------")
        print("--------- Survey Completed ---------")
        print("------- Phew! That Was Easy! -------")
        print("------------------------------------")

    def logout(self, logoutLink=None):

        if logoutLink is None:
            logoutLink = "https://sctce.etlab.in/user/logout"

        bot = self.bot
        bot.get(logoutLink)
        print("------------ Logged Out ------------")
        bot.quit()
