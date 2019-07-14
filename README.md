# TwitterQuery ~ [![Python3-shield]](https://www.python.org/) [![version-shield]]() [![license-shield]]() 
 Query Twitter Api (Frontend/Backend)

### Local Machine Testing
``` bash
set TWITTER_CONSUMER_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
set TWITTER_CONSUMER_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
set TWITTER_ACCESS_TOKEN_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
set TWITTER_ACCESS_TOKEN_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
python manage.py runserver
pause
```

### Api Mappings
:::/api/tweet/search?q=Dev%20World


### Example Google Cloud Deployment
``` yaml
runtime: python
env: flex
entrypoint: gunicorn -b :$PORT manage:app

env_variables:
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


[version-shield]: https://img.shields.io/badge/version---dev-yellowgreen.svg "dev"
[Python3-shield]: https://img.shields.io/badge/Python3%2B-3.6-blue.svg "Python3+"
[license-shield]: https://img.shields.io/badge/license-Apache%202.0-lightgrey.svg "License"