# Django Breeze

## Introduction

<hr>

Django Breeze provides a minimal and simple starting point for building a Django application with `Inertia` and `Vite` with minimal or no configuration. Styled with Tailwind CSS.

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
```

### Vue 3

```bash
django-breeze vue3
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

## Thank you

A very big thanks to [Inertia.js Team](https://github.com/inertiajs) for [Inertia Django Adaptor](https://github.com/inertiajs/inertia-django), and [MrBin99](https://github.com/MrBin99) for [Django Vite](https://github.com/MrBin99/django-vite).

## License

Laravel Breeze is open-sourced software licensed under the [MIT license](LICENSE.md).
