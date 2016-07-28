# slack-news-stream
Post news from reddit programming channel to slack

### Usage
Rename the env.py.example to env.py and set your slack webhook url as the value of url key.
Add the crawler and news_poster.py file to cronjob
e.g:
*/5 * * * * cd /path/to/project/ && scrapy crawl reddit
*/5 * * * * cd /path/to/project/ && python news_poster.py
n.b: must have python & scrapy installed on your machine
n.b: you may also need to add scrapy to the path if scrapy command not found
