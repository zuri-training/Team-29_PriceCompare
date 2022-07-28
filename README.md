

# Haggle Version 1.0 

## Project Summary

## Table of Contents
   Loading

## Technologies Used
* __Design__<br/>
        ![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)

* __Frontend__<br/>
      ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
      ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
      ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

* __Backend__<br/>
        ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
        ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

* __Database__<br/>
        ![PostgreSQL](https://img.shields.io/badge/POSTGRE-SQL-brightgreen)

* __API__<br/>
        ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)

* __Project Management and Version Control__<br/>
        ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)


## To contribute:

```

- Create a Fork of this repository

- Clone the forked repository
     # git clone repo clone link

- NOTE : Don't push to the main branch

- Open your code editor

- Run your terminal

- Add Upstream
    # git remote add upstream https://github.com/zuri-training/Price-Compare-Team-29.git

- Create a branch
    # git branch branchname

- To confirm branch creation
    # git branch --v

- Switch to the branch
    # git checkout branchname

- Make your changes.

- After finishing your tasks, Stage and commit to your branch using
    # git add . to stage all changes or git add . filename.extension to stage a file.
    # git commit -m " The task you did "

- Merge the upstream changes with your current branch to prevent conflict. 
    # git pull upstream branchname

- Push to the branch you’re working on
    # git push origin branchname
    
- Come to Github and Create a new pull request. Add a description of what you have done.

- Update your local folder/branch with new changes from all collaborators. 
    # git pull upstream branchname





```
![1_YZsKvpTcsdxPM_Wk5cmqCQ](https://user-images.githubusercontent.com/68462223/181199113-5bbc9b79-41d1-44a8-975a-4ce1d5519288.png)

## Environment Setup

Follow these commands to run the project on your local machine :

Open your terminal

Clone the project 
```
git clone https://github.com/zuri-training/price_compare_team_27.git 
```

Enter the project directory 

```
cd priceCompare
```

Create a virtual env

```
python -m venv env 
```

Activate your env(for windows)

```
env\Scripts\activate.bat	 
```
(for linux or mac)

```
source env/bin/activate 
``` 

Install Project Dependencies

```
pip install -r requirements.txt
```

Make Migrations

```
python manage.py makemigrations
python manage.py migrate
```

Create Superuser

```
python manage.py createsuperuser
```

Run the server

```
python manage.py runserver
```

