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

- `classscrapy.spiders.Spider`

    1. `name`
    2. `allowed_domains` -> `OffsiteMiddleware`
    3. `start_urls`
    4. `custom_settings`
    5. `crawler` -> `from_crawler()`
    6. `settings`
    7. `logger`
    8. `from_crawler(crawler, *args, **kwargs)`
    9. `start_requests()`
    10. `parse(response)`
    11. `log(message[, level, component])`
    12. `closed(reason)`

- Spider arguments -> `-a`

- `classscrapy.spiders.CrawlSpider`

    1. `rules` -> `Rule`
        - `classscrapy.spiders.Rule`
            1. `link_extractor`
    2. `parse_start_url(response, **kwargs)`

## Items

## Item Loaders

## Requests and Responses

## Link Extractors

# Item Pipeline

# Downloader Middleware

# Spider Middleware
