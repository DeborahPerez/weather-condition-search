# Weather Condition Search 

## Application Details

This is a web application that allows users to input a weather condition and have a list of cities currently experiencing that weather condition returned and displayed on the page.

1. Set up a local development environment and then deploy both a staging and a production environment on Heroku.
1. Created script to use google api in order to read a spreadsheet and capture values. (Please enable the google sheets api, download the client configuration and save the file credentials.json to your working directory).
1. Saved open weather map api token in file "openweathermap_token.py" as APPID = "your_key_goes_here"
1. Add in the back-end logic to take the submitted weather condition and then process it by using google api to extract the city data, then use geocode api to extract longitude and latitude data, and lastly use openweather api to capture temperature and wind speed data.


## Quick Start

### First Steps

```sh
$ python3-venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

##### Before running application please see application details about tokens and keys

### Run

```sh
# the app
$ python app.py
```
