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
| [web_scraping_beautifoul_soup_case_1](https://github.com/catpersec/usecases/blob/main/web%20scraping%20-%20web%20interaction/web_scraping_beautifoul_soup_case_1.py) / [web_scraping_beautifoul_soup_case_2](https://github.com/catpersec/usecases/blob/main/web%20scraping%20-%20web%20interaction/web_scraping_beautifoul_soup_case_2.py) | web-scraping, BeautifulSoup, sorting, local-files | Examples show how to deal with web scraping. In this particular case I did https://news.ycombinator.com/ and [empireonline.com](https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/) scarping. Vital aspect was sorting list of dictionary objects (solution based on [programiz tutorial](https://www.programiz.com/python-programming/methods/list/sort)). At the end of the lesson 45 (100DoC) I recalled how to [append text in local files](https://codeigo.com/python/append-text-to-a-file) and how to [remove files](https://www.w3schools.com/python/python_file_remove.asp) using **os** module. **(Course 100 Days of Code - Day 45)** |
| [web_scraping_beautifoul_soup_case_3](https://github.com/catpersec/usecases/blob/main/web%20scraping%20-%20web%20interaction/web_scraping_beautifoul_soup_case_3.py) | web-scraping, BeautifulSoup, list comprehension | In this particular usecase I strugggled a while with list comprehension. **(Course 100 Days of Code - Day 46)** |
| [web_scraping_beautifoul_soup_case_4](https://github.com/catpersec/usecases/blob/main/web%20scraping%20-%20web%20interaction/web_scraping_beautifoul_soup_case_4.py) | web-scraping, BeautifulSoup, requests module | Case with headers in request embedded. **(Course 100 Days of Code - Day 47)** |
| [web_scraping_web_interaction_selenium_case_1](https://github.com/catpersec/usecases/blob/main/web%20scraping%20-%20web%20interaction/web_scraping_web_interaction_selenium_case_1.py) | web-scraping, Selenium module, web-interaction, local-files, time module  | Great usecases of Selenium (both scraping data from website and interacting with website). **(Course 100 Days of Code - Day 48)** |
| [decorator_function - case 1 - basic](https://github.com/catpersec/usecases/blob/main/python%20basics/decorator_function%20-%20case%201%20-%20basic.py) | decorator function | Case with step by step decorator function implementation. **(Course 100 Days of Code - Day 54)**|
| [decorator_function - case 2 - flask case](https://github.com/catpersec/usecases/blob/main/python%20basics/decorator_function%20-%20case%202%20-%20flask%20case.py) | decorator function, Flask | Decorator function case with example of use in Flask framework. **(Course 100 Days of Code - Day 54)** |
| [decorator_function - case 3 - time measure case](https://github.com/catpersec/usecases/blob/main/python%20basics/decorator_function%20-%20case%203%20-%20time%20measure%20case.py) | decorator function | Decorator function case where decorator function measures how long did it take function to run. **(Course 100 Days of Code - Day 54)** |
| [decorator_function_advanced - case 1 - passing arguments from address bar to program](https://github.com/catpersec/usecases/blob/main/python%20basics/decorator_function_advanced%20-%20case%201%20-%20passing%20arguments%20from%20address%20bar%20to%20program.py) | advanced decorator function, Flask | Pass variable from address bar to the program. Returning passed variable as a string on the website. Turned on "Debug mode" so website server restarts with every change so client see the changes immediately |
| [decorator_function_advanced - case 2 - simple authentication example](https://github.com/catpersec/usecases/blob/main/python%20basics/decorator_function_advanced%20-%20case%202%20-%20simple%20authentication%20example.py) | advanced decorator function | Advanced Decorators with *args and **kwargs. Case with simple authentication example. |
| [decorator_function_advanced - case 3 - args and kwargs case](https://github.com/catpersec/usecases/blob/main/python%20basics/decorator_function_advanced%20-%20case%203%20-%20args%20and%20kwargs%20case.py) | advanced decorator function, *args, **kwargs, OOP, authentication | Passing function arguments to the decorator function step by step. |
| [decorator_function_advanced - case 4 - logging decorator case](https://github.com/catpersec/usecases/blob/main/python%20basics/decorator_function_advanced%20-%20case%204%20-%20logging%20decorator%20case.py) | advanced decorator function, *args, **kwargs | Passing function arguments to the decorator function example. |
<!-- | [link_title](link) | tags | note |
| [link_title](link) | tags | note |
| [link_title](link) | tags | note |
| [link_title](link) | tags | note |
| [link_title](link) | tags | note |
| [link_title](link) | tags | note | -->




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