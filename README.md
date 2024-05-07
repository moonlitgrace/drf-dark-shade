# drf-dark-shade
[![Downloads](https://static.pepy.tech/badge/drf-dark-shade)](https://pepy.tech/project/drf-dark-shade) [![Pypi Badge](https://img.shields.io/pypi/v/drf-dark-shade.svg)](https://pypi.org/project/drf-dark-shade/)

Enhance your Django Rest Framework (DRF) browsing experience with the `drf-dark-shade` package. This lightweight and easy-to-use extension bring a sleek dark theme to the DRF browsable API, reducing eye strain and providing a modern, visually appealing interface for developers.

![Screenshot from 2023-11-21 12-45-09](https://github.com/tokitouq/drf-dark-shade/assets/114811070/c1f79290-f692-4eaf-bcbd-7b619bcc7962)
<p align="center">Deep Forest Theme</p>


## Installation:
1. Install `drf-dark-shade` package using **pip** or **poetry**
    ```bash
    pip install drf_dark_shade
    # or
    poetry add drf_dark_shade
    ```

2. Add `drf_dark_shade` to your `INSTALLED_APPS` in your Django project's settings.
    ```python
    INSTALLED_APPS = [
        # ...
        "rest_framework", # django-rest-framework required
        "drf_dark_shade",
    ]
    ```
3. Add `drf_dark_shade` renderer to `REST_FRAMEWORK` config
    ```python
    REST_FRAMEWORK = {
        "DEFAULT_RENDERER_CLASSES": (
            "rest_framework.renderers.JSONRenderer",
            "drf_dark_shade.renderers.DeepForestBrowsableAPIRenderer", # configure custom renderer
        ),
        # ...
    }
    ```

## Override templates
To override providing templates:
1. Configure root `templates` dir in your django app
    ```python
    TEMPLATES = [
        {
            # ...
            # configure root templates
            "DIRS": [os.path.join(BASE_DIR, "templates")],
            "APP_DIRS": True,
            # ...
        },
    ]
    ```
2. Create template to override with name of the theme you want, like:    
   `templates/drf_dark_shade/deep-forest.html`

Check `/examples/` for example configuration with setup guide.

All set! now run app and visit your API endpoint.    
Enjoy Dark 🌃    
More themes will be added later. PRs are welcome ❤️

## Contribution

Contributions are welcome!\
If you encounter issues or want to add new features, feel free to open pull requests.\
Give a ⭐️ if you find this project interesting and useful!
