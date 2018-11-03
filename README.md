# sic
Django Static Info constructor

## Installation
1. via pip: `pip install git+https://github.com/akoikelov/sic`
or
2. download repository: https://github.com/akoikelov/sic and run script `./install.sh`

## Configuration

Add `akoikelov.sic` to INSTALLED_APPS in settings.py:
```python
INSTALLED_APPS = [
    'tastypie',
    'akoikelov.sic'
]
```

Configuration:

1. Add `url(r'^', include('akoikelov.sic.urls'))` to urls.py
```python
    urlpatterns = patterns(
        url(r'^', include('akoikelov.sic.urls')), # sic urls
        url(r'^admin/', include(admin.site.urls)),
)
```
2. Add `akoikelov.sic.context_processors.sic` to context_processors
```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')]
            ,
            'OPTIONS': {
                'context_processors': [
                    ...,
                    'akoikelov.sic.context_processors.sic' # context processor
                ]
            },
        },
]
```
3. Run `manage.py migrate` command


In template:

- Load `sic` at the top of your template
- Use `{% include_si %}` tag at the end of your template (it should be placed after jquery library script tag)
- If you don't have jquery, set `SIC_INCLUDE_JQUERY = True` in settings.py
- Every element with static content should have `sic` attribute with the key value
- Inside element just use `sic_get` template tag with a key value provided
- In order to be able to edit data, please make sure you are logged in as an administrator
- To edit an information of the element, just click on it and an modal window will be popped up

```djangotemplate
{% load "sic" %}

phone: 
<span sic="phone">
    {% sic_get 'phone' %}
</span>

<script src="jquery_link"></script>
{% include_si %}
```

There are `SIC_SAVE_BTN_LABEL`, `SIC_TEXTAREA_PLACEHOLDER` attributes which can be set in settings.py

![alt text](screencast/sic.gif)