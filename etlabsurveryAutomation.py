from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class EtlabSurveyBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self, userLoginLink):
        bot = self.bot
        bot.get(userLoginLink)
        print("-------- Delay of 5s --------")
        time.sleep(3)
        email = bot.find_element_by_id('LoginForm_username')
        password = bot.find_element_by_id('LoginForm_password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        print("-------- Logging In --------")
        print("-------- Delay of 5s --------")
        time.sleep(5)

    def doTeacherEvaluationSurveys(self, surveyToBeDone, totalNumber):
        bot = self.bot
        bot.get(surveyToBeDone)
        AnswerValueHTML = [450, 455, 460, 465, 469, 472, 476, 479, 483, 487, 491]
        totalQuestions = len(AnswerValueHTML)
        print('--- {} Questions To Be Done ---'.format(totalQuestions))
        for i in range(totalNumber):
            print('-------- Subject {} --------'.format(i+1)) #Range Means From 0 to i-1, So Making it 1 + 0
            currentSubjectorName = 'yt{}'.format(i) #Selects The Button "Answer Questions"
            currentSubjectorSelector = bot.find_element_by_name(currentSubjectorName)
            currentSubjectorSelector.click();
            print("-------- Delay of 5s --------") #wait till answer loads
            time.sleep(5)
            
            quesionNumber = 0;
            for j in AnswerValueHTML:
                print('------- Question {} -------'.format(quesionNumber))
                answerSelector = bot.find_element_by_xpath(".//input[@value='{}']".format(j)) #Selecting Required Answer
                answerSelector.click();
                quesionNumber += 1

            print("---- Selected Req Answers ----")
            print("-------- Delay of 5s --------") #Wait to Verify
            time.sleep(5)

            submitButton = bot.find_elements_by_name(currentSubjectorName)
            print(submitButton) #Getting A List
            submitButton[0].click() #Since a List, Picking it's First Position

            print("-------- Delay of 5s --------")
            time.sleep(5)

        print("--- Phew! That Was Easy! ---")


print("------ Etlab Survey Automation ------")
botObject = EtlabSurveyBot('Username', 'Password') #Create an Object & Pass Your Username and Password
botObject.login('https://sctce.etlab.in/user/login') #Pass The Login Link
botObject.doTeacherEvaluationSurveys('https://sctce.etlab.in/survey/user/answer/365', 8) #Add The Survey Link & Add the Number Of Subjects to Be Filled