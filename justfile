# Run Django server
runserver:
    ./manage.py runserver

# Open a Django interactive shell.
sh:
    ./manage.py shell

# Check Django project
check:
    ./manage.py check

# Generate migrations
mmigrate app="":
    ./manage.py makemigrations {{ app }}

# Migrate models
migrate app="":
    ./manage.py migrate {{ app }}

# Open sqlite project database
db:
    sqlite3 db.sqlite3

# Show sqlite DB schema for given table
@schema table:
    sqlite3 db.sqlite3 '.schema --indent {{ table }}'