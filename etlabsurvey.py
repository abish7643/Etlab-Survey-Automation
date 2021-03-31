from etlabautomation import EtlabBot

#Updated for Preliminary Survey (T8A) | May 31 2021

#User Credentials
username = 'username'
password = 'password'
loginlink = 'https://sctce.etlab.in/user/login'

#Survey
surveylink = 'https://sctce.etlab.in/survey/user/answer/499' 
totalSubjects = 8 #Total Number Of Subjects in Survey

#Required Answer To Be Filled (Get Answer Value From HTML)
answerReference = [5727, 5729, 5731, 5733, 5737, 5741, 5743, 5746, 5749] #S8
#answerReference = [450, 455, 460, 465, 469, 472, 476, 479, 483, 487, 491] #S7

#Bot
delay = 2
SurveyBot = EtlabBot(username, password) #Create an Object & Pass Your Username and Password
SurveyBot.login(loginlink) #Pass The Login Link
SurveyBot.doTeacherEvaluationSurveys(surveylink, totalSubjects, answerReference, delay) #Add The Survey Link & Add the Number Of Subjects to Be Filled
