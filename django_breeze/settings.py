from django.conf import settings as django_settings
from inertia.settings import settings as inertia_settings
from pathlib import Path
import inertia


def initialize() -> None:
    """Initialize all neccessary django, inertia and django-vite settings"""
    BASE_DIR = getattr(django_settings, "BASE_DIR")

    MIDDLEWARES = [
        "inertia.middleware.InertiaMiddleware",
        # "django-breeze.django_breeze.middleware.inertia_share",
    ]

    # Django Breeze Default Settings
    DJANGO_BREEZE: dict = {
        "TEMPLATE_DIR_PATH": Path(BASE_DIR) / "src/",  # path to frontend files
        "INERTIA": {
            "LAYOUT": "index.html",
            "SSR_URL": inertia_settings.INERTIA_SSR_URL,
            "SSR_ENABLED": inertia_settings.INERTIA_SSR_ENABLED,
            "JSON_ENCODER": inertia_settings.INERTIA_JSON_ENCODER,
        },
        "DJANGO_VITE": {
            "DEV_MODE": getattr(django_settings, "DEBUG", True),
            "SERVER_PROTOCOL": "http",
            "DEV_SERVER_HOST": "localhost",
            "DEV_SERVER_PORT": 5173,
            "WS_CLIENT_URL": "@vite/client",
            "ASSETS_PATH": Path(getattr(django_settings, "STATIC_PATH", "static"))
            / "dist",
            "STATIC_URL_PREFIX": "",
            "LEGACY_POLYFILLS_MOTIF": "legacy-polyfills",
        },
        "STATIC_ROOT": "static",
        "CSRF_HEADER_NAME": "HTTP_X_XSRF_TOKEN",
        "CSRF_COOKIE_NAME": "XSRF-TOKEN",
    }

    # Get user defined django breeze settings
    user_settings = getattr(django_settings, "DJANGO_BREEZE", {})

    def merge_dicts(*dicts):
        """
        Recursively merges dictionaries.
        """
        result = {}
        for d in dicts:
            for k, v in d.items():
                if isinstance(v, dict):
                    result[k] = merge_dicts(result.get(k, {}), v)
                else:
                    result[k] = v
        return result

    # Merge DJANGO_BREEZE and user-defined settings
    merged_settings = merge_dicts(DJANGO_BREEZE, user_settings)

    def key_exist(key) -> bool:
        return (
            hasattr(django_settings, key) and getattr(django_settings, key) is not None
        )

    settings = {}

    for key, value in merged_settings.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                sub_key = f"{key}_{sub_key}"
                if not key_exist(sub_key):
                    settings[sub_key] = sub_value
        else:
            if not key_exist(key):
                settings[key] = value

    for key, value in settings.items():
        setattr(django_settings, key, value)

    TEMPLATE_DIR = Path(getattr(django_settings, "TEMPLATE_DIR_PATH"))

    django_settings.TEMPLATES[0]["DIRS"].extend(
        [TEMPLATE_DIR, Path(inertia.__file__).resolve().parent / "templates/"]
    )

    django_settings.STATICFILES_DIRS.extend(
        [
            django_settings.DJANGO_VITE_ASSETS_PATH,
            TEMPLATE_DIR / "assets",
            TEMPLATE_DIR / "public",
        ]
    )
    for middleware in MIDDLEWARES:
        django_settings.MIDDLEWARE.append(middleware)
