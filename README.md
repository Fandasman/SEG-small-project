# Team Narwhal Small Group project

## Team members
The members of the team are:
- Ivan Arabadzhiev
- Arham Azhary
- Frantisek Hermanek
- Volodymyr Hromyk
- Bradly Zeneli
- Yuliang Zhang

## Project structure
The project is called `system`.  It consists of a single app `clubs`.


## Deployed version of the application
The deployed version of the application can be found at https://nameless-wildwood-11631.herokuapp.com/.
The admin interface can be accessed at https://nameless-wildwood-11631.herokuapp.com/admin.

## Installation instructions
To install the software and use it in your local development environment, you must first set up and activate a local development environment.  From the root of the project:

```
$ virtualenv venv
$ source venv/bin/activate
```

Install all required packages:

```
$ pip3 install -r requirements.txt
```

Migrate the database:

```
$ python3 manage.py migrate
```

Seed the development database with:

```
$ python3 manage.py seed
```

Run all tests with:
```
$ python3 manage.py test
```

*The above instructions should work in your version of the application.  If there are deviations, declare those here in bold.  Otherwise, remove this line.*

## Sources
The packages used by this application are specified in `requirements.txt`
The code used from clucker was substantially referenced in this chess hub project




*Declare are other sources here.*
