# GAE RESTful API 

A simple RESTful API built on top of Google App Engine

## Disclaimer

This app is intended for educational purposes only, and should NOT be used on production. 

To create a RESTful API for production purposes, you should use the [Endpoints API](https://cloud.google.com/appengine/docs/python/endpoints/create_api).

## Installation

##### To set up the app locally:

* Install the Google [App Engine Python SDK](https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python)
* Run `git clone git@github.com:bengrunfeld/gae-restful-api.git && cd gae-restful-api`
* Edit `app.yaml` and change the value for `application` from `gae-restful-api` to any name of your choice. You'll need it later
* You can now test your app. Run the development server with `dev_appserver.py .`, then test the app using [Postman](http://www.getpostman.com/). You should be able to test a route at [http://target-domain/todos/api/v0.1.0/](http://target-domain/todos/api/v0.1.0/)

##### To set up an appspot for the app:

* Navigate to [https://console.developers.google.com/project](https://console.developers.google.com/project)
* Click `Create Project`
* You can use whatever name you want for `PROJECT NAME`, but for `PROJECT ID`, you need to use the same value you set above for `application` in `app.yaml`.
* `cd` into your application directory and run `appcfg.py update .`. You will need to enter your email and password.
* You can now view the application at `[your-project-id].appspot.com`, although to receive anything besides a **404 error**, you'll need to use a URI like [http://[your-project-id].appspot.com/todos/api/v0.1.0/](http://[your-project-id].appspot.com/todos/api/v0.1.0/)

## Usage

I suggest using [Postman](http://www.getpostman.com/) to send HTTP requests.

##### Create

Send a HTTP POST request to [http://target-domain/todos/api/v0.1.0/](http://target-domain/todos/api/v0.1.0/) with form data of `Key: title, Value: [title of todo]`

##### Read all 

Send a HTTP GET request to [http://target-domain/todos/api/v0.1.0/](http://target-domain/todos/api/v0.1.0/) 

##### Read one

Send a HTTP GET request to [http://target-domain/todos/api/v0.1.0/ndb-key-id](http://target-domain/todos/api/v0.1.0/ndb-key-id) 

##### Update

Send a HTTP PUT request to [http://target-domain/todos/api/v0.1.0/ndb-key-id](http://target-domain/todos/api/v0.1.0/ndb-key-id) with form data of `Key: title, Value: [new title of todo]`

##### Delete 

Send a HTTP DELETE request to [http://target-domain/todos/api/v0.1.0/ndb-key-id](http://target-domain/todos/api/v0.1.0/ndb-key-id) with **NO** form data 
