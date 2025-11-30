<div align=justify>

# :heavy_check_mark: SuperToDo

A ToDo web application stylized with Bootstrap and fully developed on Django.

This project was created as homework for Server-side Web Development subject of my Web Application Development formation.

## :wrench: Technologies

- `pip`
- `pip-venv`
- `Python`
- `Django`
- `HTML`
- `Bootstrap 5`

## :star: Features

1. **Add, edit and delete tasks** in a simpler way across the minimalist and clean user interface.
2. **Add deadlines** to your things to do, the application sort your list by the deadlines showing you first the nearest date.
3. **Keep it organized** navigating between the different tabs that filter your tasks in pending or completed.

## :book: What I learned

### Django basics and the Model-View-Template pattern

I learned how use Django framework to create a fully backend application using Python, also I learned how it works using his Model-View-Template pattern (similar to MVC), where the model
represents the data but the view handle the business logic and the template display the information.

### `pip` as package manager and `pip-venv` for virtual environments

I use `pip` to install the dependencies (in this case, just Django), and learned how to save that dependencies into a `requeriments.txt` that helps me to, in a future, install all packages
with just one command. Also, I use `pip-venv` to create a virtual environment, keeping isolated the packages that I used in the project.

### Basics URL handling

With the `urls.py` file, I setup different routes to execute different views, thinking on model identifiers like the `task_slug` used for create dynamic urls.

## :eyes: Demostration

<div align=center>

https://github.com/user-attachments/assets/0340f9aa-7086-4ed0-82c1-75da94dae706

</div>

## :question: How run this app?

1. Download the package or clone the repository.
2. Before use anything, execute `apt-get install python3.12 python3-pip python3-venv` into the terminal to install the neccesary packages.
3. Inside, use `python3 -m venv .venv --prompt supertodo` to create the virtual environment.
4. Use `source .venv/bin/activate` to enter into the virtual environment.
5. Execute `pip install -r requeriments.txt` to install the dependencies.
6. Now you can use `./manage.py check && ./manage.py migrate` to prepare the application.
7. If you want to access into admin dashboard later, execute `./manage.py createsuperuser` and complete the form to create your admin user.
8. then, `./manage.py runserver` to start it and access by the default url [localhost:8000](http://localhost:8000). You can enter into the admin interface with [localhost:8000/admin](http://localhost:8000/admin)
10. When you want to leave, just stop the dev server with `Ctrl+C` on terminal and writing `deactivate` to leave the virtual environment.

</div>
