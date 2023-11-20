# `drf-dark-shade`
Enhance your Django Rest Framework (DRF) browsing experience with the `drf-dark-shade` package. This lightweight and easy-to-use extension bring a sleek dark theme to the DRF browsable API, reducing eye strain and providing a modern, visually appealing interface for developers.

`Deep Forest Theme:`
![Screenshot from 2023-11-20 22-24-45](https://github.com/tokitouq/drf-dark-shade/assets/114811070/e9a865e2-c581-455a-bba3-694432567910)

## Installation:
1. Install `drf-dark-shade` package using **pip** or **poetry**
```bash
pip install drf_dark_shade
```

2. Add `drf_dark_shade` to your `INSTALLED_APPS` in your Django project's settings.
```bash
INSTALLED_APPS = [
    # other packages
    'rest_framework', # drf required
    'drf_dark_shade',
]
```
3. Add `drf_dark_shade` renderer to `REST_FRAMEWORK` config
```bash
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'drf_dark_shade.renderers.DeepForestBrowsableAPIRenderer', # deep forest theme
    )
}
```
All set! now run app and visit your API endpoint.\
Enjoy Dark 🌃

## Contribution

Contributions are welcome!\
If you encounter issues or want to add new features, feel free to open pull requests.\
Give a ⭐️ if you find this project interesting and useful!
