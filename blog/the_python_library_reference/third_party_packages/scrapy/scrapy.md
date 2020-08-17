# Architecture

<p align="center">
    <img src="../../../../img/the_python_library_reference/third_party_packages/scrapy/scrapy_architecture.png" width="100%">
</p>

# Scrapy Tutorial

```
tutorial/
    scrapy.cfg            # deploy configuration file

    tutorial/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py
```

# Spiders

Spiders are the place where you define the custom behaviour for crawling and parsing pages for a particular site (or, in some cases, a group of sites).



## Items

## Item Loaders

## Requests and Responses

## Link Extractors

# Item Pipeline

# Downloader Middleware

# Spider Middleware
