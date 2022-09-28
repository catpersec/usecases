# usecases <!-- omit in toc -->
Simple way to keep track what I learned.

- [Markdown](#markdown)
- [Python](#python)
  - [Main table](#main-table)
  - [Other](#other)
    - [sort() vs sorted](#sort-vs-sorted)
    - [List comprehension](#list-comprehension)
- [Operating Systems](#operating-systems)
  - [Windows](#windows)
    - [Environment Variables](#environment-variables)
      - [List All Environment Variables](#list-all-environment-variables)
      - [Check A Specific Environment Variable](#check-a-specific-environment-variable)
      - [Setting Environment Variables](#setting-environment-variables)



# Markdown
+ [Markdown cheatsheet](https://www.w3schools.io/file/markdown-cheatsheet/)
C:\Git\usecases\web scraping\web_scraping_case_4.py

# Python



## Main table
| File | Tags | Note |
|---|---|---|
| [web_scraping_beautifoul_soup_case_1](https://github.com/catpersec/usecases/blob/main/web%20scraping%20-%20web%20interaction/web_scraping_beautifoul_soup_case_1.py) / [web_scraping_beautifoul_soup_case_2](https://github.com/catpersec/usecases/blob/main/web%20scraping%20-%20web%20interaction/web_scraping_beautifoul_soup_case_2.py) | web-scraping, BeautifulSoup, sorting, local-files, 100DoC-d45 | Examples show how to deal with web scraping. In this particular case I did https://news.ycombinator.com/ and [empireonline.com](https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/) scarping. Vital aspect was sorting list of dictionary objects (solution based on [programiz tutorial](https://www.programiz.com/python-programming/methods/list/sort)). At the end of the lesson 45 (100DoC) I recalled how to [append text in local files](https://codeigo.com/python/append-text-to-a-file) and how to [remove files](https://www.w3schools.com/python/python_file_remove.asp) using **os** module. |
| [web_scraping_beautifoul_soup_case_3](https://github.com/catpersec/usecases/blob/main/web%20scraping%20-%20web%20interaction/web_scraping_beautifoul_soup_case_3.py) | web-scraping, BeautifulSoup, list comprehension, 100DoC-d46 | In this particular usecase I strugggled a while with list comprehension.  |
| [web_scraping_beautifoul_soup_case_4](https://github.com/catpersec/usecases/blob/main/web%20scraping%20-%20web%20interaction/web_scraping_beautifoul_soup_case_4.py) | web-scraping, BeautifulSoup, requests module, 100DoC-d47 | Case with headers in request embedded. |
| [web_scraping_web_interaction_selenium_case_1](https://github.com/catpersec/usecases/blob/main/web%20scraping%20-%20web%20interaction/web_scraping_web_interaction_selenium_case_1.py) | web-scraping, Selenium module, web-interaction, local-files, 100DoC-d48, time  | Great usecases of Selenium (both scraping data from website and interacting with website).  |
| [decorator_function - case 1 - basic](https://github.com/catpersec/usecases/blob/main/python%20basics/decorator_function%20-%20case%201%20-%20basic.py) | decorator function, 100DoC-d54 | Case with step by step decorator function implementation. |
| [decorator_function - case 2 - flask case](https://github.com/catpersec/usecases/blob/main/python%20basics/decorator_function%20-%20case%202%20-%20flask%20case.py) | decorator function, Flask, 100DoC-d54 | Decorator function case with example of use in Flask framework. |
| [decorator_function - case 3 - time measure case](https://github.com/catpersec/usecases/blob/main/python%20basics/decorator_function%20-%20case%203%20-%20time%20measure%20case.py) | decorator function, 100DoC-d54 | Decorator function case where decorator function measures how long did it take function to run. |
| [link_title](link) | tags | note |
| [link_title](link) | tags | note |
| [link_title](link) | tags | note |
| [link_title](link) | tags | note |
| [link_title](link) | tags | note |

## Other

### sort() vs sorted
+ sort does not return the sorted list; rather, it sorts the list in place.
+ sorted does it

### List comprehension
```python
many_elements = [2,4,6]
items = [element + 2 for element in many_elements]
print(items)

RESULT > [4,6,8]
```

is the same as:

```python
many_elements = [2,4,6]
items = []
for element in many_elements:
  items.append(element+2)
print(items)

RESULT > [4,6,8]
```



# Operating Systems

## Windows

### Environment Variables

#### List All Environment Variables
+ CMD
```console
set
```
+ POWERSHELL
```powershell
Get-ChildItem Env:
```

#### Check A Specific Environment Variable
+ CMD
```console
echo %[variable_name]%
```
+ POWERSHELL
```powershell
echo $Env:[variable_name]
```

#### Setting Environment Variables
+ CMD
```console
setx [variable_name] "[variable_value]"
```
+ POWERSHELL
```powershell
$env:[variable_name] = '[variable_value]'
```