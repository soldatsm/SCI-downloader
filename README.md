# Description

This is a script that allows you to down load articles from `sci-hub`

Currently it works only with [ChromDriver](https://chromedriver.chromium.org/) I will add other browser, at last Mozilla, in neares future

_________________________________________________________________________________

## Dependanses

* [Selenium](https://github.com/SeleniumHQ/selenium)
* [tqdm](https://github.com/tqdm/tqdm)
* `argparse`

## Manual

This script uses several flags:
* `-h` - print help massage
* `-list` - Allows to download one or many articles by writing DOIs after flag in `"10.1016/j.promfg.2019.02.324"` format without commas separation
* `-doi_file` - Allow to down load articles by using txt list of DOIs in `10.1016/j.promfg.2019.02.324` format. DOIs should be separated by lines
* `dir` - positional argumet - output derrictory for articles in `D:\article_folder\` format




