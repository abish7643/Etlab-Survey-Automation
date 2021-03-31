from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class EtlabBot:
    def __init__(self, username, password):
        print("-------------------------------------")
        print("------ Etlab Survey Automation ------")
        print("-------------------------------------")
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self, userLoginLink):
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

        print("------------ Delay of {}s -----------".format(delay)) #Wait Till Survey Page Loads
        time.sleep(delay)

        rows = bot.find_elements_by_id("section-form")
        totalSubjects = len(rows)
        print('----- {} Subjects To Be Done ------'.format(totalSubjects))

        totalQuestions = len(AnswerValueHTML)
        print('----- {} Questions To Be Done ------'.format(totalQuestions))

        #Iterating Through Each Subject
        for i in range(totalSubjects):
            print('------------ Subject {} ------------'.format(i+1)) #Range Means From 0 to i-1, So Making it 1 + 0
            currentSubjectorName = 'yt{}'.format(i) #Selects The Button "Answer Questions"
            currentSubjectorSelector = bot.find_element_by_name(currentSubjectorName)
            currentSubjectorSelector.click()
            print("------------ Delay of {}s -----------".format(delay)) #wait till answer loads
            time.sleep(delay)
            
            quesionNumber = 1
            #Iterating Through Each Question
            for j in AnswerValueHTML:
                print('------------ Question {} ------------'.format(quesionNumber))
                answerSelector = bot.find_element_by_xpath(".//input[@value='{}']".format(j)) #Selecting Required Answer
                answerSelector.click()
                quesionNumber += 1

            print("------- Selected Req Answers -------")
            print("------------ Delay of {}s -----------".format(delay)) #Wait to Verify
            time.sleep(delay)

            submitButtonName = 'yt0' #Name Attribute Of Submit Button From HTML
            submitButton = bot.find_elements_by_name(submitButtonName)
            submitButton[0].click()

            print("------------ Delay of {}s -----------".format(delay))
            time.sleep(delay)

        print("------------------------------------")
        print("--------- Survey Completed ---------")
        print("------- Phew! That Was Easy! -------")
        print("------------------------------------")
