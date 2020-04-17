# Data Engineering Assesement

Retrieve data from drug database api: https://drugtargetcommons.fimm.fi/api/data/bioactivity

Data to retrieve:

* compounds
* publications (pubmed_id)
* publication authors (authors)
* targets
* genes

## Data Description and Assumptions 

The below assumptions have been made regarding the data.

1. The data to retrieve overall describes a bioactivity
2. A bioactivity except the above data points can also be uniquely identified from the data provider based on the resource url each one provides. We can get get that from the last path param of: 
```javascript
{
    "resource_uri": "/api/data/bioactivity/6715077/",
}
```
In this example the native id is 6715077

3. A compound consist of its name, concnentration value and concentration value unit. Fields in response:
```javascript
{
    "compound_concentration_value": null,
    "compound_concentration_value_unit": null,
    "compound_name": null,
}
```
4. Publications are described from pubmed_id which it is assumed that is unique.
5. Author is only described by his/her name. We assume that this name is unique -in this context- and each author may have participated in several publications.
6. Targets are described from organism and pref_name. Fields in response:
```javascript
{
    "target_organism": null,
    "target_pref_name": null,
}
```
7. A gene is described by its name. Field in response:
```javascript
{
    "gene_name": null,
}
```


## Database Schema

From a data exploration (on sample data) that took place before the implementaton seems that there are a lot of null values for the mentioned fields. Those are handled as default values in the database (ids are set to -1 and rest of fields as 'N/A'). This happens in order to maintain the relational integrity for bioactivity table.

Escept the previously mentioned fields all the tables are also storing the creation date and the update date (This can be optimized although since it seems that is only needed for bioactivity table).

Database schema can be found below:

![database schema](https://user-images.githubusercontent.com/25746825/79562783-3cc16f80-80b4-11ea-84cf-14ebed2a384c.png "Database Schema")

### Notes:
* Bioactivity is the table that holds the foreign keys of the rest of the tables and the native id as described above.
* A many to many relationship exists between authors and publications

## Project Structure and Short Description

```bash
├── app.py
├── db
│   ├── database.py
│   └── __init__.py
├── logger
│   ├── __init__.py
│   └── log_conf.py
├── .env
├── models
│   ├── Author.py
│   ├── BaseModel.py
│   ├── Bioactivity.py
│   ├── Compound.py
│   ├── Gene.py
│   ├── __init__.py
│   ├── PublicationAuthor.py
│   ├── Publication.py
│   └── Target.py
├── Pipfile
├── Pipfile.lock
├── Readme.md
├── requirements.txt
├── service
│   ├── database_service.py
│   ├── data_service.py
│   ├── fetch_service.py
│   └── __init__.py
└── settings.py
```

* app.py: Entry point of the application. It just calls the needed methods to run the app from their respective services.
* db: Module where we create the database connection and the session to interact with it. 
* logger: Module to overwrite the default logger configuration. Also defines the log file name (File will be generated as soon as the application starts with a date suffix). 
* .env: File to hold environmental variables (More on this below)
* models: Modules that holds all the models that we are using to interact with the database. All the models inherits some basic functionalit from the BaseModel.py which inherits the Base model of SQLAlchemy
* Pipfile & Pipfile.lock: Pipenv files
* requirements.txt: Dependecies and versions that this application is using
* service: Module that holds the logic of the application
    * database service: Initialize the database and inserts default values
    * data service: Prepares and stores the data
    * fetch_service: Retrieves the data from api and initialize the data storage
* settings.py: Module to consume .env file or to add other constants of the application

## Using the application

In order to use application create a new directory in your machine and clone the repo.

```
cd to/your/project/path
git clone https://github.com/karolosk/iai_data_engineering_assessment.git
cd iai_data_engineering_assesement
```

Optionally you can create a virual environment for the application.
Assuming that you want to use pipenv for this:
```
pip install pipenv
```

Then in order to install the dependencies run:
```
pipenv install -r requirements.txt
```

Note: You can enter the virtual environment in your current working directory with 
```
pipenv shell
``` 

In the case you do not want to use a virual environment skip the above virtual environment steps and just run 
```
pip install -r requirements.txt
```

## .env File

The application is using environmental variables to run properly. Those variables are stored in the .env file. 

The contents of the file are:
```
ENV=dev
DRUGTARGETCOMMONS_BASE_URL=https://drugtargetcommons.fimm.fi
DRUGTARGETCOMMONS_API_ENDPOINT=/api/data/bioactivity/?format=json
DRUGTARGETCOMMONS_API_LIMIT=&limit=20
LOG_LEVEL=DEBUG
DATABASE_URI=postgres://db_user:db_password@db_host:db_port/db_name
```
* ENV = Desctibes the development environemt. If it is set to dev -as it is in the moment- it will eneable the echo of all sql queries/commands that are executed to the console. 

* DRUGTARGETCOMMONS_BASE_URL = Base url of the data provider 

* DRUGTARGETCOMMONS_API_ENDPOINT = API endpoint of the data provider, used to initially the retrieval of the data

* DRUGTARGETCOMMONS_API_LIMIT = Limit parameter of the API. If you want to increase/decrease the batch size change this vale

* LOG_LEVEL= Describes from which logging level the logs will appear in the console or written in the log file 

* DATABASE_URI = Database uri which will be used for the application. **(You need to change this)**
    * Assuming you have Postgres already installed change the values with your own (e.g Assuming you have a default Postgres installation, with user admin and password admin, and you have created a database called iai_assesement for the application then this should be set as: postgres://admin:admin@localhost:5432/iai_assesement)
        

As soon as you are ready with your environment (installed dependencies, .env file) simply run in your project directory:

```
python app.py
```
This will start the process and it will run untill it consume the whole API.
