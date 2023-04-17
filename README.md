# DJANGO BREEZE

## Introduction

<hr>

Django Breeze provides a minimal and simple starting point for building a Django application with `Vite` and . Styled with Tailwind, Breeze publishes authentication controllers and views to your application that can be easily customized based on your own application's needs.

Django Breeze is powered by Vite and Tailwind.

## Installation

Install the following python package via pip

```bash
pip install django-breeze
```

Add the django_breeze app to your `INSTALLED_APPS` in `settings.py`

```python
INSTALLED_APPS = [
  # installed apps,
  'django_breeze',
  #........
]
```

Add the Inertia middleware to your `MIDDLEWARE` in `settings.py`

```python
MIDDLEWARE = [
  # django middleware,
  'django_breeze.middleware.InertiaMiddleware',
  # your project's middleware,
]
```

## Generate Project Files

### React

```bash
python3 -m django_breeze react
```

### Vue 3

```bash
python3 -m django_breeze vue
```

## Install node packages

To install node packages for the frontend

```zsh
npm install
```

### OR use yarn

```bash
yarn
```

## Start Servers

Run the following to start your development servers

```bash
python manage.py runserver
```

```bash
npm run dev
```

Now you're all set!

## Official Inertia Documentation

Documentation for Inertia can be found on the [Intertia website](https://inertiajs.com/).

## License

Laravel Breeze is open-sourced software licensed under the [MIT license](LICENSE.md).
