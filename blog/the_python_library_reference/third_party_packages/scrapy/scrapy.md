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

- `class scrapy.spiders.Spider`

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

- `class scrapy.spiders.CrawlSpider`

    1. `rules` -> `Rule`
        - `class scrapy.spiders.Rule`
            1. `link_extractor`
            2. `callback`
            3. `cb_kwargs`
            4. `follow`
            5. `process_links`
            6. `process_request`
            7. `errback`
    2. `parse_start_url(response, **kwargs)`

- `class scrapy.spiders.XMLFeedSpider`

- `class scrapy.spiders.CSVFeedSpider`

- `class scrapy.spiders.SitemapSpider`

## Items

- Item Types

    1. dictionaries -> `dict`
    2. Item objects -> `class scrapy.item.Item([arg])`, `class scrapy.item.Field([arg])`
    3. dataclass objects -> `dataclass`
    4. attrs objects -> `attr.s`

- Supporting All Item Types

    In code that receives an item, such as methods of item pipelines or spider middlewares, it is a good practice to use the `ItemAdapter` class and the `is_item()` function to write code that works for any supported item type.

## Item Loaders

> Collected data is internally stored as lists, allowing to add several values to the same field.

- `class scrapy.loader.ItemLoader`

    1. `item` -> `Item`
    2. `context`
    3. `default_item_class`
    4. `default_input_processor`
    5. `default_output_processor`
    6. `default_selector_class`
    7. `selector`
    8. `add_css(field_name, css, *processors, **kw)`
    9. `add_value(field_name, value, *processors, **kw)`
    10. `add_xpath(field_name, xpath, *processors, **kw)`
    11. `load_item()`
    12. `nested_css(css, **context)`
    13. `nested_xpath(xpath, **context)`

## Requests and Responses

## Link Extractors

# Item Pipeline

# Downloader Middleware

# Spider Middleware
