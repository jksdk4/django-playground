# Admin Stuff

Juicy! 🥤🍇

## Make an admin profile

- With the server not running, enter `python manage.py migrate`.
- Then enter `python manage.py createsuperuser`.
- Enter a new username and a password when prompted.
- Restart the server and notice the red error on init goes away. Sign in at `127.0.0.1:8000/admin` with these new credentials.

## Migrations and Models

1. When you make a new app, you can add in a model of that app in the `models.py` file, like so. 
    - Again, it doesn't necessarily have to be the name of the app, but it can be. Here, I'll use Name-of-model to distinguish it from the name-of-app.
```
    class {Name-of-model}(models.Model):
        title = models.CharField(max_length=200)
        text = models.TextField()
        created = models.DateTimeField(auto_now_add=True)
```

2. Once you have done so, you can run `python manage.py makemigrations`. A file called `0001_initial.py` will appear within that app's migrations folder. This contains info about the class you have added.

3. Running `python manage.py migrate` will add this info to the sqlite3 database.
4. Edit the new app's `admin.py` and append this block so that it will display it the admin UI.
```
    from . import models

    class {Name-of-model}Admin(admin.ModelAdmin):
        list_display = ('title',)

    admin.site.register(models.{Name-of-model}, {Name-of-model}Admin)
```
5. When you sign in to the admin interface, you will see a new section display of this model. It seems to struggle with plurals. If you populate the fields for this app model and then save, notice that the `list_display` will show the instance of the app under how you titled it. If that was not present, then it would display as `{Name-of-model}Object (n)` where n is the id index of what you added.

## Viewing in the shell

1. You can run `python manage.py shell` in a project to start a shell.
2. You can import a model with `from {name-of-app}.models import {Name-of-model}`.
3. You can make an object of a specific model using `myvar = {Name-of-model}.get(pk='n')`, and then you can access values of properties on it such as `myvar.title` and `myvar.text`.
4. You can get a QuerySet list of objects by running `{Name-of-model}.objects.all()`.
5. You can add a new instance of this model by running `myvar_2 = {Name-of-model}.objects.create(title="something", text="something also")}` where title and text are properties of that model. A different model does not inherently have these properties.
6. You can filter or exclude by using something like `{Name-of-model}.objects.filter(title__startswith="The")` or `{Name-of-model}.objects.exclude(text__icontains="something")`.
  
    

# Building Dynamic Webpages

💻🥴 Bendy!

## Dynamic Templating

1. In the new app, create a `templates/{name-of-app}` directory. Doesn't have to be the app name. Can be whatever makes sense. It's just for some consistency.
2. In this example, I will make a webpage that dynamically lists the titles of each instance of the model. I add `{name-of-model}_list.html` under this folder.
3. I append this in the app's `views.py`.
```
    from .models import {Name-of-model}

    def list(request):
        all_{name-of-model} = {Name-of-model}.objects.all()
        return render(request, '{name-of-app}/{name-of-model}_list.html', { '{name-of-model-list}': all_{name-of-model} })
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
        <h1>List:</h1>
        <ul>
            {% for {item} in {name-of-model-list} %}
            <li>{{ {item}.title }}</li>
            {% endfor %}
        <ul>
    </html>
```