![django-breeze-logo](https://user-images.githubusercontent.com/60859741/233969758-939d1091-f04c-4625-8e2a-23697bca58d8.jpg)

# Django Breeze

## Introduction

Django Breeze provides a minimal and simple starting point for building a Django application with `Inertia` and `Vite.js` with minimal or no configuration. Styled with Tailwind CSS.

Inertia helps build single-page apps, without building an API. Create modern single-page React, Vue, and Svelte apps using classic server-side routing. Works with any backend. Documentation for Inertia can be found on the [Intertia website](https://inertiajs.com/).

## Setup and Installation

Before installing the packages, ensure you are in your project's virtual environment.

1. Install the django-breeze package.

```bash
pip install django-breeze
```

2. Create a new django project if you haven't created one already.

```bash
django-breeze startproject myproject
```

Add the django_breeze to your `INSTALLED_APPS` in `settings.py`

```python
INSTALLED_APPS = [
  #..............
  'django_breeze',
  #..............
]
```

### Generate Project Files

Generate your frontend project files with django-breeze, use `--typescript` option for usage with TypeScript.

React

```bash
django-breeze create-app react
```

Vue 3

```bash
django-breeze create-app vue3
```

After generating your frontend project files, you should see `src` directory with other relevant files in the root of your django project.

### Install the frontend packages

Run this command to install packages for the frontend.

```bash
npm install

# or

yarn
```

### Start the Servers

Run the following commands to start your development servers.

1. Vite server

```bash
npm run dev
```

2. Django server

```bash
python manage.py runserver
```

Now visit your django host address at e.g <http://127.0.0.1:8000/>

![django-breeze-success-setup screen](https://user-images.githubusercontent.com/60859741/233971714-3729c1d9-6f9e-4a39-ae38-4d76f14419ef.png)

Now you're all set!

## Usage

### Responses

Render Inertia responses is simple, you can either use the provided inertia render function or, for the most common use case, the inertia decorator. The render function accepts four arguments, the first is your request object. The second is the name of the component you want to render from within your pages directory (without extension). The third argument is a dict of `props` that should be provided to your components. The final argument is `template_data`, for any variables you want to provide to your template, but this is much less common.

```python
# views.py

from inertia import render
from .models import Event

def index(request):
  return render(request, 'Event/Index', props={
    'events': Event.objects.all()
  })
```

Or use the simpler decorator for the most common use cases

```python
# views.py

from inertia import inertia
from .models import Event

@inertia('Event/Index')
def index(request):
  return {
    'events': Event.objects.all(),
  }
```

For more information on the usage, refer to [inertia-django Docs.](https://github.com/inertiajs/inertia-django#usage)

## Production

In production, you must do the following:

1. In the `settings.py`

```python
DEBUG = FALSE
```

2. Run below command to build your frontend files

```bash
npm run build
# or
yarn build
```

3. Run below django command to collect static files.

```bash
python -m manage.py collectstatic
```

## Settings

Although, djang breeze comes with minimal or no configuration but here are some of the default settings it comes with out of the box.

### Django Settings

```python
# settings.py

STATIC_ROOT = "static"

 DJANGO_BREEZE = {
        "INERTIA": {
            "LAYOUT": "index.html",
            "SSR_URL": "http://localhost:13714",
            "SSR_ENABLED": False,
        },
        "DJANGO_VITE": {
            "DEV_MODE": True, # vite dev mode, default based on django DEBUG
            "SERVER_PROTOCOL": "http",
            "DEV_SERVER_HOST": "localhost",
            "DEV_SERVER_PORT": 5173,
            "WS_CLIENT_URL": "@vite/client",
            "ASSETS_PATH": "static/dist", # vite build asset path
            "STATIC_URL_PREFIX": "",
        }
 }
```

Settings for [Inertia Django](https://github.com/inertiajs/inertia-django) is under `INERTIA` and [Django Vite](https://github.com/MrBin99/django-vite) is `DJANGO_VITE`. You can find more explaination of the settings on their repos

`Note:` All settings are joined with underscore to match how their developers defined them e.g inertia settings is `INERTIA_LAYOUT` and django vite is `DJANGO_VITE_DEV_MODE` which has been done automatically by django breeze so you just use the `DJANGO_BREEZE` settings format in your `settings.py` file.

## Thank you

A very big thanks to the following people for their work done:

- [Inertia.js Team](https://github.com/inertiajs) for Inertia Django Adaptor.
- [MrBin99](https://github.com/MrBin99) for Django Vite.

## License

Django Breeze is open-sourced software licensed under the [MIT license](LICENSE.md).
