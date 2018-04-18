# Handwritten-Digit-Classifier

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://digit-identify.herokuapp.com/)
[![license](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://github.com/channelCS/digit-identify/blob/master/LICENSE) [![dep1](https://img.shields.io/badge/Tensorflow-1.3+-orange.svg)](https://www.tensorflow.org/) [![dep2](https://img.shields.io/badge/Keras-2.1+-red.svg)](https://keras.io/) [![dep3](https://img.shields.io/badge/Python-2.7+-blue.svg)](https://www.python.org/)

**Objective Goal**

Idenity Handwritten Digits with Convolutional Neural Network using Flask and deploy the app on Heroku.

## Steps to run the application

### Using GitHub
1. **Fork this repo**

    Click on the <img src = "https://github.com/akshitac8/github-buttons/blob/master/2x/github_fork.png" width=50 /> 
    button to make a copy of this repo in your own account.
2. **Clone your repo**

        git clone https://github.com/<your-name>/digit-identify.git
    
3. **Log into your Heroku account with CLI.**
4. **Push your changes in GitHub**

```
$ git add .
$ git commit -m "Add your commit name"
$ git push origin master
```
5. **Deploy it on Heroku with the steps mentioned below.**

### Using Heroku Manual Setup

1. **Setup The App**
- Create a free Heroku Account(Online)
- Python version >= 2.7 installed locally
- For Linux:
```
$ heroku login
Enter your Heroku credentials.
Email: python@example.com
Password:
```
- For Windows:
  - Download Heroku CLI
  - Once Installed use heroku command on your command shell (cmd)

2. **Prepare the app**

```
$ git clone https://github.com/heroku/python-getting-started.git
$ cd python-getting-started
```

3. **Deploy the app**

```
$ heroku create
Creating lit-bastion-5032 in organization heroku... done, stack is cedar-14
http://lit-bastion-5032.herokuapp.com/ | https://git.heroku.com/lit-bastion-5032.git
Git remote heroku added

```

```
$git push heroku master
Counting objects: 232, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (217/217), done.
Writing objects: 100% (232/232), 29.64 KiB | 0 bytes/s, done.
Total 232 (delta 118), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Python app detected
remote: -----> Installing python-3.6.0
remote: -----> Installing requirements with latest pipenv...
remote:        Installing dependencies from Pipfile.lock...
remote:      $ python manage.py collectstatic --noinput
remote:        58 static files copied to '/app/gettingstarted/staticfiles', 58 post-processed.
remote:
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote:
remote: -----> Compressing...
remote:        Done: 39.3M
remote: -----> Launching...
remote:        Released v4
remote:        http://lit-bastion-5032.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To git@heroku.com:lit-bastion-5032.git
 * [new branch]      master -> master

```

