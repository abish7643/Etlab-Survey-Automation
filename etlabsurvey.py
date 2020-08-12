from etlabautomation import EtlabBot

#User Credentials
username = 'username'
password = 'password'
loginlink = 'https://sctce.etlab.in/user/login'

#Survey
surveylink = 'https://sctce.etlab.in/survey/user/answer/365' 
totalSubjects = 8 #Total Number Of Subjects in Survey
answerReference = [450, 455, 460, 465, 469, 472, 476, 479, 483, 487, 491] #Required Answer To Be Filled

#Bot
SurveyBot = EtlabBot(username, password) #Create an Object & Pass Your Username and Password
SurveyBot.login(loginlink) #Pass The Login Link
SurveyBot.doTeacherEvaluationSurveys(surveylink, totalSubjects, answerReference) #Add The Survey Link & Add the Number Of Subjects to Be Filled