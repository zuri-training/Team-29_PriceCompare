
# Project Name
 Haggle Version 1.0 


## Table of Contents
   - About Project
   - Technologies Used
   - Environment Setup
   - Contributors
   - How To Contribute
   
## About Project
 Haggle is a price comparison web application that allows users to compare prices of products from different e-commerce merchants. Users can compare prices, make comments under products/prices, share products directly to their social media platforms and also share via emails to third parties. Also, users interested in purchasing any of the products will be redirected to the purchase page of the selected merchant via the ref link, available on the product page of every product. Haggle will be accessible to both authenticated and unauthenticated users, but with the authenticated users having full access to the platform.

One major challenge faced during the development was geting reliable merchants APIs with credible data for free.

Features we hope to implement in the nearest future are:
 - Deal of the day section
 - Top deal section
 - Wishlist
 - Blog

## Technologies Used
* __Design__<br/>
        ![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)
        
        We used figma because it makes collaboration between team members easy, as several designers can work on the same file at the same time.

* __Frontend__<br/>
      ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
      ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
      ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

      HTML 5 - The HTML was used to give structure, and to add and modify contents in the platform. It was also used to create validated forms in the platform, like the login, sign up and contact forms. 

      CSS 3 -  The CSS was used to give additional styling and layout to the web pages. We also used CSS for the styling because of its easy syntax.

      JavaScript - JavaScript was used to give functionality to the page. It was used to make the page interactive for a good user experience.


* __Backend__<br/>
        ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
        ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

        Django was used as the backend framework because it is more scalable and flexible than other web development frameworks for Python language. It allows developers to customize various aspects of web apps in accordance with the specific business requirements.

* __Database__<br/>
        ![PostgreSQL](https://img.shields.io/badge/POSTGRE-SQL-brightgreen)
        
        Postgresql was used as the database because it is better, and gives access to multiple users at the same time

* __Scraping Tool__<br/>
        ![Selenium](https://img.shields.io/badge/selenium-%23121011.svg?style=for-the-badge&logo=selenium&logoColor=white)
        
        Selenium was used for the web scraping because it is not too complicated to use, and it can be used to collect data from websites that use javascript without relying on tools to do that such as splash.


* __Project Management and Version Control__<br/>
        ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
        
        We used github because of its enhanced collaboration feature and easy file management. It makes it easier for the individual and team to use Git for version control and provide collaboration features such as task management, bug tracking and feature request for every project.



## Environment Setup

Follow these commands to run the project on your local machine :

Open your terminal

Clone the project 
```
git clone https://github.com/zuri-training/Team-29_PriceCompare.git
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



## Contributors

### Designers--------------------------Github Usernames
 - Ogechim Wodi (OG)--------------------Ogecheem
 - Ajayi Oluwaseun Irewole--------------ireSeun
 - Omojowo Busola-----------------------omojowobusola
 - Claire Gbobie------------------------Gbobieclaire
 - Priscilla Onifade--------------------PriscillaOore
 - Ernest Emediong----------------------EmediongErnest
 - Samir Areh---------------------------mistadane
 - Stephen Okesola----------------------Stefan1100
 - Roqeebah	Akesire---------------------Ro-qeebah
 - Okolo Faith--------------------------okolofaith
 - Tega Eghosa--------------------------snrchieftegz


### Developers---------------------------Github Usernames                                               
 - Amafaye Wallace (Frontend)-----------Waeyword
 - Jude Oyedele (Backend)---------------Judekennywise
 - Adelaja Oluwatobi (Backend)----------aristobells
 - Adesina	oluwatimileyin (Backend)----timmyades3
 - Isaac Olowookere (Backend)-----------Olowookereisaac
 - Richard Tamaramieye (Frontend)-------Marvingt 
 - Laurrencia O. Francis Joseph (Frontend)-----Laurrencia
 - Peace Bello (Frontend)---------------SuperPaix
 - Mas’uud Abdulkareem (Backend)--------viperrrr
 - Precious Onyishi (Backend)-----------Njidekaa
 - Etinosa	Ogbevoen (Backend)----------Jheff4
 - Rhoda Adegbola (Frontend)------------Rhododen
 - Odubo Timidi James (Frontend)--------Timidij
 - Ojewale Kehinde (Backend)------------ojewalekehinde
 - Eugene Reinhard (Frontend/Backend)---Iam-Rey
 

## To contribute:

```

- Create a Fork of this repository

- Clone the forked repository
     # git clone repo clone link

- NOTE : Don't push to the main branch

- Open your code editor

- Run your terminal

- Add Upstream
    # git remote add upstream https://github.com/zuri-training/Team-29_PriceCompare.git

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
