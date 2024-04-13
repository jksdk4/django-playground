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

## Keep in mind

- If you copied an app to another project, did you add it to the settings.py of the project folder? Did you rename the class and the name property within it under `apps.py` if it conflicts with an existing one? Did you delete any cache and init files?
