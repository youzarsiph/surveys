# Users

Users is a Django app for creating, reading, updating and deleting users models.

## Get started

Install the package:

```shell
pip install django-users
```

After installation:

- In `settings.py`, add `users` app to `INSTALLED_APPS`.
- Users app can be used as a web app that uses HTML templates and/or as an API back-end:
  - If you want to use HTML templates, then include `users.urls` in your project level `urls.py`.
  - Include `users.routers` to use the API endpoints.
  - Or include the both.

## Set up the templates

Users app does not contain HTML templates to give the developer the options of customization.

To set up the templates:

- In `settings.py`, set the `DIRS` = `[BASE_DIR / 'templates']`.
- Create `templates` folder in your project folder.
- Create a folder named with the name of the app that contains `AUTH_USER_MODEL` (the default is `auth`).
- Create the templates (`user_list.html`, `user_detail.html`, `user_form.html`, `user_confirm_delete.html`)

**Note**: If you named your user model different than `User`, you may need to name your templates according to the name of the model

Example: Let's say that the name of your app is `blog` and you extended the default user model and you named the new user model `BlogUser` then the folder that you will create in the templates folder is `blog` and you will need to rename the templates, for example `user_list.html` will be `bloguser_list.html`.

I hope that you find this useful.
