# Etlab-Survey-Automation
Logins to Etlab &amp; automates the required survey. 
Made Using Selenium &amp; Python3

### Requirements

* [Selenium](https://pypi.org/project/selenium/) (`pip3 install selenium`)
* [Geckodriver](https://github.com/mozilla/geckodriver/releases) & Mozilla Firefox

### Geckdriver Installation (Linux)

* Download the latest release of geckdriver for linux and extract the file.
`tar -xvf geckodriver-v0.29.0-linux64.tar.gz` (Replace the filename with your downloaded one.)

* Make the extracted binary executable.
`chmod +x geckodriver`

* Move the file /usr/local/bin/ directory.
`sudo mv geckodriver /usr/local/bin/`
 

### Run The Program By,

`python3 etlabsurvey.py`

> Note: Replace username, password, surveylink, answerReference in etlabsurvey.py file depending upon your requirement.
