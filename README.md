# Django Breeze

## Introduction

Django Breeze provides a minimal and simple starting point for building a Django application with `Inertia` and `Vite.js` with minimal or no configuration. Styled with Tailwind CSS.

Inertia helps build single-page apps, without building an API. Create modern single-page React, Vue, and Svelte apps using classic server-side routing. Works with any backend. Documentation for Inertia can be found on the [Intertia website](https://inertiajs.com/).

## Installation

Install the following python package via pip

```bash
pip install django-breeze
```

Add the following apps to your `INSTALLED_APPS` in `settings.py`

```python
INSTALLED_APPS = [
  # installed apps,
  'django_breeze',
  'django_vite',
  'inertia',
  #...............
]
```

<!-- Add the Inertia middleware to your `MIDDLEWARE` in `settings.py`

```python
MIDDLEWARE = [
  # django middleware,
  'django_breeze.middleware.InertiaMiddleware',
  # your project's middleware,
]
``` -->

## Generate Project Files

Generate your frontend project files with django-breeze

### React

```bash
django-breeze react

# or with typescript

django-breeze react --typescript
```

### Vue 3

```bash
django-breeze vue3

# or with typescript

django-breeze vue3 --typescript
```

## Install node packages

Run this command to install packages for the frontend.

```zsh
npm install

# or

yarn
```

## Start Servers

Run the following commands to start your development servers.

### Vite server

```bash
npm run dev
```

### Django server

```bash
python manage.py runserver
```

Now you're all set!

## Usage

For usage, refer to [inertia-django](https://github.com/inertiajs/inertia-django#usage) for in-depth guidlines.

## Configurations

Although, djang breeze comes with minimal or no configurations but here are some of the default settings it comes with out of the box.

### Django Settings

```python
# settings.py

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
```

Settings for [Inertia Django](https://github.com/inertiajs/inertia-django) is under `INERTIA` and [Django Vite](https://github.com/MrBin99/django-vite) is `DJANGO_VITE`. You can find more explaination of the settings on their repos

`Note:` All settings are joined with underscore to match how their developers defined them e.g inertia settings is `INERTIA_LAYOUT` and django vite is `DJANGO_VITE_DEV_MODE` which has been done automatically by django breeze so you just use the `DJANGO_BREEZE` settings format in your `settings.py` file.

## Thank you

A very big thanks to [Inertia.js Team](https://github.com/inertiajs) for [Inertia Django Adaptor](https://github.com/inertiajs/inertia-django), and [MrBin99](https://github.com/MrBin99) for [Django Vite](https://github.com/MrBin99/django-vite).

## License

Laravel Breeze is open-sourced software licensed under the [MIT license](LICENSE.md).
