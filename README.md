# RESTFUL-Resume

This is a rest application of resume. End users can access my resume in a restful manner. Various section of my resume like education, experience, project can be accessed through this api.

### Deployement
This restful api is deployed on heroku and the data base used is mongodb. DataBase is deployed on mLab's MongoDB hosting platform.

### Sections of resume

1. Contact Information
2. Education
3. Experience
4. Skills
5. Projects
6. Links

### Endpoint access

1. https://prabhath-resume.herokuapp.com/ or https://prabhath-resume.herokuapp.com/resume
2. https://prabhath-resume.herokuapp.com/education or [Education](https://prabhath-resume.herokuapp.com/education)

### Parmas in https://prabhath-resume.herokuapp.com/{param}

1. education
2. contact
3. skills
4. projects
5. experience
6. links

#### Response for https://prabhath-resume.herokuapp.com/
```json
{
  "Resume": [
    {
      "Contact Information": {
        "Gmail": "prabhathkiran20@gmail.com",
        "Hotmail": "prabhath6@hotmail.com",
        "LinkedIn": "Prabhath Kiran",
        "name": "Prabhath Kiran Atmakuri"
      },
      "Education": {
        "Bachelors": {
          "GPA": "3.6/4",
          "Graduated": "April, 2014",
          "Stream": "Electronic and communications",
          "University": "KLUniversity"
        },
        "Masters": {
          "GPA": "3.46/4",
          "Graduated": "March, 2016",
          "Stream": "Computer Science",
          "University": "Santa Clara University"
        }
      },
      "Experience": {
        "Company": "Ecofactor",
        "Duration": "July 2015 - September 2015",
        "Location": "RedWood City, CA",
        "Title": "Software Intern",
        "worked-on": [
          "Enabling continuous Integration tests in development process using Jenkins and Maven.",
          "Built coverage reports using Cobertura and Jacoco plugins.",
          "Worked on RESTful api using python micro-service framework(Bottle).",
          "Adding instrumentation to monitor production code using New Relic.",
          "Writing automation scripts to fill the missing data in MySQL Database.",
          "Worked in a test driven development, familiar with UnitTests, Integration, Mocking data, TestNg.",
          "Familiar with git work flow, all the code was managed on git.",
          "Participated as a team member in Agile Process, such a pointing stories, transactional stories to in progress and ready QA, obtaining code reviews."
        ]
      },
      "Links": {
        "Github": "https://github.com/prabhath6",
        "LinkedIn": "https://www.linkedin.com/pub/prabhath-kiran/56/56a/505"
      },
      "Projects": {
        "Category prediction Using Naive Bayes on Hadoop": "The goal of this project is build a prediction system that takes in title of a particular reddit post and predict to which category it belongs. The main algorithm employed in project is Naive Bayes. This projects mainly focuses on modeling huge data set (60gb) on hadoop.",
        "Occupancy Determination": "The main goal of this project is to show evidence that power consumption of electrical devices in a residential setting can be used to determine presence of residents in their house. This is achieved by using Random Forests from sklearn library in python.",
        "Online Dairy Using Django": "Built an online dairy using Django framework. The main features of this application are registration, email conformation, password change, create an entry, change an entry. The backend data base used for this project is mysql.",
        "Reliable data Transfer over an Unreliable Channel with Bit Errors": "Designed a stop and wait protocol using C language, to transmit data over an unreliable channel by calculating checksum to detect bit errors in the data and re-transmit the data with out errors.",
        "Spatial Database implementation using java": "Designed a front end user interface using java and backend database using oracle. The main implementation of the project is to build queries based on the selection of check boxes and radio buttons from the gui that is build using java and these queries are sent to database using jdbc and data is returned and plotted on the gui.",
        "System Metrics RESTful Api": "Designed and built a RESTful api inorder to access system metrics like CPU Usage, CPU Times, Disk usage, Network Usage and Memory Usage of the given system. Python's flask micro-framework and psutil are used to build the rest api.",
        "Web Server HTTP 1.0 using Java": "Built a HTTP 1.0 web server using Java. Web Server handles multiple clients using multi-threaded approach. The clients send their request to the web server using browser and the server process the request and renders particular web page to client. The web supports basic http status like 200, 400, 404 and 403."
      },
      "Skills": {
        "Cloud Applications": "Heroku",
        "Editors": [
          "Vim",
          "Emacs",
          "Sublime",
          "Eclipse",
          "Pycharm",
          "IntelliJ IDEA"
        ],
        "Languages": [
          "Python",
          "Java",
          "sql",
          "Bash"
        ],
        "ORM Technologies": [
          "Hibernate",
          "SQLAlchemy",
          "MongoAlchemy"
        ],
        "Operating Systems": [
          "OSX",
          "LINUX",
          "Windows"
        ],
        "SQL": [
          "Mysql",
          "Postgres",
          "Oracle11g"
        ],
        "Version Control": "Git",
        "Web Development": [
          "HTML",
          "CSS",
          "JavaScript",
          "Flask",
          "Django(basic knowledge)"
        ]
      }
    }
  ]
}
```

##### Response for endpoint https://prabhath-resume.herokuapp.com/resume/contact

```json
{
  "contact_info": [
    {
      "contact_info": {
        "Gmail": "prabhathkiran20@gmail.com",
        "Hotmail": "prabhath6@hotmail.com",
        "LinkedIn": "Prabhath Kiran",
        "name": "Prabhath Kiran Atmakuri"
      }
    }
  ]
}
```

![REST API](http://2y5mo62gdufr3ganc332cx3n.wpengine.netdna-cdn.com/wp-content/uploads/REST-API-Logo.png "REST API")
