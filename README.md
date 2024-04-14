# How to Get Started
So I can quit forgetting and not having any consistent notes 🙄😒 Peek the demo folder to trace your steps.

## How to make Django Exist

0. I assume you have Python installed and configured. Environment variables and all that.
1. Create empty folder.
2. In the terminal at this folder's path, run `python -m venv {name-of-environment}` (can just be `.` to inherit folder's name). If you're on Mac use `python3`.
3. Run the newly generated `.\Scripts\activate` to activate the venv. Terminal should start with `({name-of-environment})`.
4. Run `pip install django` to install django in the venv.
5. Run `django-admin startproject {name-of-project}`. 
    - This is not necessarily the name of the environment or the top level folder in the first step, unless you want it to be I guess. This directory is where you would store separate project entities though, so choose wisely. I probably wouldn't fundamentally name it that way tho.
6. Change directories to the base of the newly generated `{name-of-project}`'s folder. There is a child folder of the same name and a `manage.py` in this directory.
7. To ensure that Django exists, run `python manage.py runserver`.
8. If the terminal doesn't complain and you can reach the server address, success. Si no, idk start over.

## How to add a base app with a view

1. You can run either `python manage.py startapp {name-of-app}` or `django-admin startapp {name-of-app}`. The first command seems slightly faster.
    - Similarly, the name of the app is not necessarily the same as the project, as multiple apps within the project will live here.
2. These should generate a folder of the app name, that of which contains a `migrations` folder. It should also have an `admin.py`, `apps.py`, `models.py`, `tests.py`, and `views.py` file under the app's folder.
3. It may or may not auto-list the app under `INSTALLED_APPS` in the `{name-of-project}/settings.py` file. Add it if not.

### Way 1, using HTTPResponse

4. Under the app's folder, create a `urls.py` file. Add this code block: 
```
    from django.urls import path 
    from . import views 

    urlpatterns = [ 
        path('', views.index, name='index'), 
    ] 
```
5. Under the app's folder, append this to the `views.py` file:
```
    from django.http import HttpResponse 
    def index(request): 
        return HttpResponse("This is the index view of {name-of-project}.")
```
6. Up one folder into the core project folder (sibling to your app folder), update the `urls.py` to reflect:
```
    from django.contrib import admin
    from django.urls import path, include      # add include, it is not originally here

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('{name-of-project}/', include('{name-of-app}.urls'))     # add this line.
    ]
```

### Way 2, using render and a template

4. Under the app's folder, create a `urls.py` file as: 
```
    from django.urls import path
    from . import views

    urlpatterns = [
        path('{name-of-app}', views.{name-of-app})    # be mindful of how this is declared.
    ]
```
5. Under the app's folder, create a `templates/{name-of-app}` path, then make a base HTML file within. Then append this to the app's `views.py` file:
```
    def {name-of-app}(request):
        return render(request, '{name-of-app}/{base}.html', {})
```
6. Up one folder into the core project folder (sibling to your app folder), update the `urls.py` to reflect:
```
    from django.contrib import admin
    from django.urls import path, include      # add include, it is not originally here

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('{name-of-app}.urls'))     # add this line.
    ]
```
### Ultimately

I suppose the structures of the urlpatterns between the app and project's urls.py file can be interchangeable, I'll have to look closer. But this strategy prevents dependency. Fun fact - views in the MVT model handle requests and responses.

7. On the server URL in the browser, if you append the path `/{name-of-project}` as designated in the views file, then you should see the HTTP Response or render. Great. You have a minimally functioning base page.

# Admin Stuff

Juicy! 🥤🍇

## Make an admin profile

- With the server not running, enter `python manage.py migrate`.
- Then enter `python manage.py createsuperuser`.
- Enter a new username and a password when prompted.
- Restart the server and notice the red error on init goes away. Sign in at `127.0.0.1:8000/admin` with these new credentials.

## Migrations and Models

1. When you make a new app, you can add in a model of that app in the `models.py` file, like so. 
    - Again, it doesn't necessarily have to be the name of the app, but for ease and consistency this is what I will use; I will capitalize Name-of-app to indicate that it is a class for a model.
```
    class {Name-of-app}(models.Model):
        title = models.CharField(max_length=200)
        text = models.TextField()
        created = models.DateTimeField(auto_now_add=True)
```

2. Once you have done so, you can run `python manage.py makemigrations`. A file called `0001_initial.py` will appear within that app's migrations folder. This contains info about the class you have added.

3. Running `python manage.py migrate` will add this info to the sqlite3 database.
4. Edit the new app's `admin.py` and append this block so that it will display it the admin UI.
```
    from . import models

    class {Name-of-app}Admin(admin.ModelAdmin):
        list_display = ('title',)

    admin.site.register(models.{Name-of-app}, {Name-of-app}Admin)
```
5. When you sign in to the admin interface, you will see a new section display of this model. It seems to struggle with plurals. If you populate the fields for this app model and then save, notice that the `list_display` will show the instance of the app under how you titled it. If that was not present, then it would display as `{Name-of-app}Object (n)` where n is the id index of what you added.

## Viewing in the shell

1. You can run `python manage.py shell` in a project to start a shell.
2. You can import a model with `from {name-of-app}.models import {Name-of-app}`.
3. You can make an object of a specific model using `myvar = {Name-of-app}.get(pk='n')`, and then you can access values of properties on it such as `myvar.title` and `myvar.text`.
4. You can get a QuerySet list of objects by running `{Name-of-app}.objects.all()`.
5. You can add a new instance of this model by running `myvar_2 = {Name-of-app}.objects.create(title="something", text="something also")}` where title and text are properties of that model. A different model does not inherently have these properties.
6. You can filter or exclude by using something like `{Name-of-app}.objects.filter(title__startswith="The")` or `{Name-of-app}.objects.exclude(text__icontains="something")`.
  
    

# Building Dynamic Webpages

💻🥴 Bendy!

## Dynamic Templating

1. In the new app, create a `templates/{name-of-app}` directory.
2. In this example, I will make a webpage that dynamically lists the titles of each instance of the model. I add `{name-of-app}_list.html` under this folder.
3. I append this in the app's `views.py`.
```
    from .models import {Name-of-app}

    def list(request):
        all_{name-of-app} = {Name-of-app}.objects.all()
        return render(request, '{name-of-app}/{name-of-app}_list.html', { '{name-of-app-list}': all_{name-of-app} })
```
4. I create a `urls.py` folder and append this:
```
    from . import views

    urlpatterns = [
        path('{name-of-app}', views.list)
    ]
```
5. In the project's `urls.py` file, I append this to the urlpatterns list:
```
    path('{parent-dir-name-that-i-picked-just-now}/', include('{name-of-app}.urls'))
```
6. To quickly display the dynamic listing, I add this into the new HTML file:
```
    <html>
        <h1>Notes:</h1>
        <ul>
            {% for {item} in {name-of-app-list} %}
            <li>{{ {item}.title }}</li>
            {% endfor %}
        <ul>
    </html>
```
---
### Keep in mind

- If you copied an app to another project, did you add it to the settings.py of the project folder? Did you rename the class and the name property within it under `apps.py` if it conflicts with an existing one? Did you delete any cache and init files?
