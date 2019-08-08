# TwitterQuery ~ [![Python3-shield]](https://www.python.org/) [![version-shield]]() [![license-shield]]() [![flask-require-shield]]() 
 Query Twitter Api (Frontend/Backend)

### Local Machine Testing
#### Create ./boot_server.bat
``` bash
set FLASK_CONFIG=development
set SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
set TWITTER_CONSUMER_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
set TWITTER_CONSUMER_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
set TWITTER_ACCESS_TOKEN_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
set TWITTER_ACCESS_TOKEN_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
python manage.py runserver
pause
```

# Api Mappings

### GET /api/tweet/search
#### Example: Search – GET http://localhost:5000/api/tweet/search?q=Dev%20World&count=25
``` json
{
  "data": {
    "search_metadata": {
      "completed_in": 0.025, 
      "count": 1, 
      "max_id": 1150481719922851840, 
      "max_id_str": "1150481719922851840", 
      "next_results": "?max_id=1150481719922851839&q=Dev%20World&count=1&include_entities=1&result_type=recent", 
      "query": "Dev+World", 
      "refresh_url": "?since_id=1150481719922851840&q=Dev%20World&result_type=recent&include_entities=1", 
      "since_id": 0, 
      "since_id_str": "0"
    }, 
    "statuses": [....]
    "wordfrequency": {
      "1975": 1, 
      "1979": 1, 
      "1983": 1, 
      "Allan": 1, 
      "Border": 1, 
      "Captains": 1, 
      "Clive": 1, 
      "Cups": 1, 
      "Kapil": 1, 
      "Lloyd": 1, 
      "SeerviBharath": 1, 
      "World": 1
    }
  }, 
  "message": "ok", 
  "status": "ok"
}
```

#### Screenshots

<img width="640 " height="360"
    src="https://raw.githubusercontent.com/InSertCod3/TwitterQuery/master/screenshots/2.PNG">
  
# Example Google Cloud (APPENGINE) Deployment

#### Example: Yaml configuration
#### 1. --> Create: ./app.yaml
#### 2. --> Configure: Apply Contents below (Fill in the "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" with there respective values)
``` yaml
runtime: python
env: flex
entrypoint: gunicorn -b :$PORT manage:app

env_variables:
  FLASK_CONFIG: production
  SECRET_KEY: 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
  TWITTER_CONSUMER_KEY: 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'
  TWITTER_CONSUMER_SECRET: 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'
  TWITTER_ACCESS_TOKEN_KEY: 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
  TWITTER_ACCESS_TOKEN_SECRET: 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'

runtime_config:
  python_version: 3

# This sample incurs costs to run on the App Engine flexible environment. 
# The settings below are to reduce costs during testing and are not appropriate
# for production use. For more information, see:
# https://cloud.google.com/appengine/docs/flexible/python/configuring-your-app-with-app-yaml
manual_scaling:
  instances: 1
resources:
  cpu: 1
  memory_gb: 0.5
  disk_size_gb: 10
```
#### 3. --> Deploy: Run the App on Google Cloud App Engine
```bash
>>> gcloud app deploy
```

# Example Google Cloud (Cloud Run) Deployment
#### 1. Create ./Dockerfile
```DockerFile
# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.7

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

# Install production dependencies.
RUN pip install Flask gunicorn Flask requests fire python-twitter better_profanity

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 2 manage:app
```

#### 2. Configure & Deploy 
```bash
foo@bar:~$ gcloud config get-value project
{PROJECT_ID}
foo@bar:~$ gcloud builds submit --tag gcr.io/{PROJECT_ID}/twitterquery
............................
.....Build Container........
............................
foo@bar:~$ gcloud beta run deploy --image gcr.io/unique-aloe-217423/twitterquery --platform managed --update-env-vars 
              TWITTER_CONSUMER_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX,TWITTER_CONSUMER_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX,
              TWITTER_ACCESS_TOKEN_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX,TWITTER_ACCESS_TOKEN_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Service name (twitterquery):  twitterquery
Allow unauthenticated invocations to [twitterquery] (y/N)?  y
Deploying container..........
Service [twitterquery] revision [twitterquery-00001] has been deployed and is serving traffic at https://twitterquery.XXXXXXX..........
foo@bar:~$
```
## 3. Useful Conmands
#### Avoid unnecessary memory allocation
```bash
foo@bar:~$ gcloud beta run services update [SERVICE_NAME] --memory 128
```
#### Change Envoriment Variables
```bash
foo@bar:~$ gcloud beta run services update [SERVICE_NAME] --update-env-vars KEY1=VALUE1,KEY2=VALUE2
```

[version-shield]: https://img.shields.io/badge/version---dev-yellowgreen.svg "dev"
[Python3-shield]: https://img.shields.io/badge/Python3%2B-3.6-blue.svg "Python3+"
[license-shield]: https://img.shields.io/badge/license-Apache%202.0-lightgrey.svg "License"
[flask-require-shield]: https://img.shields.io/badge/requires-Flask%201.0%2B-yellow.svg "Flask"
