from etlabautomation import EtlabBot

#Updated for Preliminary Survey (T7A) | September 5 2020

#User Credentials
username = 'username'
password = 'password'
loginlink = 'https://sctce.etlab.in/user/login'

#Survey
surveylink = 'https://sctce.etlab.in/survey/user/answer/394' 
totalSubjects = 12 #Total Number Of Subjects in Survey
answerReference = [5727, 5729, 5731, 5733, 5737, 5741, 5743, 5746, 5749] #Required Answer To Be Filled (Get Answer Value From HTML)

#Bot
delay = 2
SurveyBot = EtlabBot(username, password) #Create an Object & Pass Your Username and Password
SurveyBot.login(loginlink) #Pass The Login Link
SurveyBot.doTeacherEvaluationSurveys(surveylink, totalSubjects, answerReference, delay) #Add The Survey Link & Add the Number Of Subjects to Be Filled