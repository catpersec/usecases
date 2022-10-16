Simple way to keep track what I learned.

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
- [Powershell](#powershell)
  - [Basics](#basics)
  - [Assing, Compare Operators](#assing-compare-operators)
  - [Formatting output (Format-Table, Format-List, -AutoSize)](#formatting-output-format-table-format-list--autosize)
  - [Regular expressions (regex)](#regular-expressions-regex)
  - [Flow Control (if, for, foreach, while, switch)](#flow-control-if-for-foreach-while-switch)
  - [Variables](#variables)
  - [Functions (functions definition)](#functions-functions-definition)
  - [Modules (powershell modules)](#modules-powershell-modules)
    - [Working with modules](#working-with-modules)
    - [Module managment](#module-managment)
  - [Filesystem (working with local files)](#filesystem-working-with-local-files)
  - [Hashtables (Powershell Dictionary)](#hashtables-powershell-dictionary)
  - [Windows Management Instrumentation (WMI) (Windows only)](#windows-management-instrumentation-wmi-windows-only)
  - [Asynchronous Event Registration](#asynchronous-event-registration)
    - [Register for filesystem events](#register-for-filesystem-events)
  - [Perform a task on a timer (ie. every 5000 milliseconds)](#perform-a-task-on-a-timer-ie-every-5000-milliseconds)
  - [PowerShell Drives (PSDrives)](#powershell-drives-psdrives)
  - [Data Management (sort-object, where-object, group-object)](#data-management-sort-object-where-object-group-object)
- [Markdown](#markdown)

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
| [my sum function](link) | *args, for loop | Simple usecase of for loop and *args  |


<!-- | [link_title](link) | tags | note |
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

# Powershell
ALL CREDITS TO: [[https://gist.github.com/pcgeek86]]
## Basics
```powershell
Get-Command                                               # Retrieves a list of all the commands available to PowerShell
                                                          # (native binaries in $env:PATH + cmdlets / functions from PowerShell modules)
Get-Command -Module Microsoft*                            # Retrieves a list of all the PowerShell commands exported from modules named Microsoft*
Get-Command -Name *item                                   # Retrieves a list of all commands (native binaries + PowerShell commands) ending in "item"

Get-Help                                                  # Get all help topics
Get-Help -Name about_Variables                            # Get help for a specific about_* topic (aka. man page)
Get-Help -Name Get-Command                                # Get help for a specific PowerShell function
Get-Help -Name Get-Command -Parameter Module              # Get help for a specific parameter on a specific command
```
## Assing, Compare Operators
```powershell
$a = 2                                                    # Basic variable assignment operator
$a += 1                                                   # Incremental assignment operator
$a -= 1                                                   # Decrement assignment operator

$a -eq 0                                                  # Equality comparison operator
$a -ne 5                                                  # Not-equal comparison operator
$a -gt 2                                                  # Greater than comparison operator
$a -lt 3                                                  # Less than comparison operator

$FirstName = 'Trevor'
$FirstName -like 'T*'                                     # Perform string comparison using the -like operator, which supports the wildcard (*) character. Returns $true

$BaconIsYummy = $true
$FoodToEat = $BaconIsYummy ? 'bacon' : 'beets'            # Sets the $FoodToEat variable to 'bacon' using the ternary operator
```

## Formatting output (Format-Table, Format-List, -AutoSize)
```powershell


```

## Regular expressions (regex)
```powershell
'Trevor' -match '^T\w*'                                   # Perform a regular expression match against a string value. # Returns $true and populates $matches variable
$matches[0]                                               # Returns 'Trevor', based on the above match

@('Trevor', 'Billy', 'Bobby') -match '^B'                 # Perform a regular expression match against an array of string values. Returns Billy, Bobby

$regex = [regex]'(\w{3,8})'
$regex.Matches('Trevor Bobby Dillon Joe Jacob').Value     # Find multiple matches against a singleton string value.
```
## Flow Control (if, for, foreach, while, switch)
```powershell
if (1 -eq 1) { }                                          # Do something if 1 is equal to 1

do { 'hi' } while ($false)                                # Loop while a condition is true (always executes at least once)

while ($false) { 'hi' }                                   # While loops are not guaranteed to run at least once
while ($true) { }                                         # Do something indefinitely
while ($true) { if (1 -eq 1) { break } }                  # Break out of an infinite while loop conditionally

for ($i = 0; $i -le 10; $i++) { Write-Host $i }           # Iterate using a for..loop
foreach ($item in (Get-Process)) { }                      # Iterate over items in an array

switch ('test') { 'test' { 'matched'; break } }           # Use the switch statement to perform actions based on conditions. Returns string 'matched'
switch -regex (@('Trevor', 'Daniel', 'Bobby')) {          # Use the switch statement with regular expressions to match inputs
  'o' { $PSItem; break }                                  # NOTE: $PSItem or $_ refers to the "current" item being matched in the array
}
switch -regex (@('Trevor', 'Daniel', 'Bobby')) {          # Switch statement omitting the break statement. Inputs can be matched multiple times, in this scenario.
  'e' { $PSItem }
  'r' { $PSItem }
}
```

## Variables
```powershell
$a = 0                                                    # Initialize a variable
[int] $a = 'Trevor'                                       # Initialize a variable, with the specified type (throws an exception)
[string] $a = 'Trevor'                                    # Initialize a variable, with the specified type (doesn't throw an exception)

Get-Command -Name *varia*                                 # Get a list of commands related to variable management

Get-Variable                                              # Get an array of objects, representing the variables in the current and parent scopes 
Get-Variable | ? { $PSItem.Options -contains 'constant' } # Get variables with the "Constant" option set
Get-Variable | ? { $PSItem.Options -contains 'readonly' } # Get variables with the "ReadOnly" option set

New-Variable -Name FirstName -Value Trevor
New-Variable FirstName -Value Trevor -Option Constant     # Create a constant variable, that can only be removed by restarting PowerShell
New-Variable FirstName -Value Trevor -Option ReadOnly     # Create a variable that can only be removed by specifying the -Force parameter on Remove-Variable

Remove-Variable -Name firstname                           # Remove a variable, with the specified name
Remove-Variable -Name firstname -Force                    # Remove a variable, with the specified name, that has the "ReadOnly" option set
```

## Functions (functions definition)
```powershell
function add ($a, $b) { $a + $b }                         # A basic PowerShell function

function Do-Something {                                   # A PowerShell Advanced Function, with all three blocks declared: BEGIN, PROCESS, END
  [CmdletBinding]()]
  param ()
  begin { }
  process { }
  end { }
}
```

## Modules (powershell modules)
### Working with modules
```powershell
Get-Command -Name *module* -Module mic*core                 # Which commands can I use to work with modules?

Get-Module -ListAvailable                                   # Show me all of the modules installed on my system (controlled by $env:PSModulePath)
Get-Module                                                  # Show me all of the modules imported into the current session

$PSModuleAutoLoadingPreference = 0                          # Disable auto-loading of installed PowerShell modules, when a command is invoked

Import-Module -Name NameIT                                  # Explicitly import a module, from the specified filesystem path or name (must be present in $env:PSModulePath)
Remove-Module -Name NameIT                                  # Remove a module from the scope of the current PowerShell session

New-ModuleManifest                                          # Helper function to create a new module manifest. You can create it by hand instead.

New-Module -Name trevor -ScriptBlock {                      # Create an in-memory PowerShell module (advanced users)
  function Add($a,$b) { $a + $b } }

New-Module -Name trevor -ScriptBlock {                      # Create an in-memory PowerShell module, and make it visible to Get-Module (advanced users)
  function Add($a,$b) { $a + $b } } | Import-Module
```

### Module managment
```powershell
Get-Command -Module PowerShellGet                           # Explore commands to manage PowerShell modules

Find-Module -Tag cloud                                      # Find modules in the PowerShell Gallery with a "cloud" tag
Find-Module -Name ps*                                       # Find modules in the PowerShell Gallery whose name starts with "PS"

Install-Module -Name NameIT -Scope CurrentUser -Force       # Install a module to your personal directory (non-admin)
Install-Module -Name NameIT -Force                          # Install a module to your personal directory (admin / root)
Install-Module -Name NameIT -RequiredVersion 1.9.0          # Install a specific version of a module

Uninstall-Module -Name NameIT                               # Uninstall module called "NameIT", only if it was installed via Install-Module

Register-PSRepository -Name <repo> -SourceLocation <uri>    # Configure a private PowerShell module registry
Unregister-PSRepository -Name <repo>                        # Deregister a PowerShell Repository
```

## Filesystem (working with local files)
```powershell
New-Item -Path c:\test -ItemType Directory                  # Create a directory
mkdir c:\test2                                              # Create a directory (short-hand)

New-Item -Path c:\test\myrecipes.txt                        # Create an empty file
Set-Content -Path c:\test.txt -Value ''                     # Create an empty file
[System.IO.File]::WriteAllText('testing.txt', '')           # Create an empty file using .NET Base Class Library

Remove-Item -Path testing.txt                               # Delete a file
[System.IO.File]::Delete('testing.txt')                     # Delete a file using .NET Base Class Library
```

## Hashtables (Powershell Dictionary)
```powershell
$Person = @{
  FirstName = 'Trevor'
  LastName = 'Sullivan'
  Likes = @(
    'Bacon',
    'Beer',
    'Software'
  )
}                                                           # Create a PowerShell HashTable

$Person.FirstName                                           # Retrieve an item from a HashTable
$Person.Likes[-1]                                           # Returns the last item in the "Likes" array, in the $Person HashTable (software)
$Person.Age = 50                                            # Add a new property to a HashTable
```

## Windows Management Instrumentation (WMI) (Windows only)
```powershell
Get-CimInstance -ClassName Win32_BIOS                       # Retrieve BIOS information
Get-CimInstance -ClassName Win32_DiskDrive                  # Retrieve information about locally connected physical disk devices
Get-CimInstance -ClassName Win32_PhysicalMemory             # Retrieve information about install physical memory (RAM)
Get-CimInstance -ClassName Win32_NetworkAdapter             # Retrieve information about installed network adapters (physical + virtual)
Get-CimInstance -ClassName Win32_VideoController            # Retrieve information about installed graphics / video card (GPU)

Get-CimClass -Namespace root\cimv2                          # Explore the various WMI classes available in the root\cimv2 namespace
Get-CimInstance -Namespace root -ClassName __NAMESPACE      # Explore the child WMI namespaces underneath the root\cimv2 namespace
```

## Asynchronous Event Registration
### Register for filesystem events
```powershell
$Watcher = [System.IO.FileSystemWatcher]::new('c:\tmp')
Register-ObjectEvent -InputObject $Watcher -EventName Created -Action {
  Write-Host -Object 'New file created!!!'
}        
```
## Perform a task on a timer (ie. every 5000 milliseconds)
```powershell
$Timer = [System.Timers.Timer]::new(5000)
Register-ObjectEvent -InputObject $Timer -EventName Elapsed -Action {
  Write-Host -ForegroundColor Blue -Object 'Timer elapsed! Doing some work.'
}
$Timer.Start()
```

## PowerShell Drives (PSDrives)
```powershell
Get-PSDrive                                                 # List all the PSDrives on the system
New-PSDrive -Name videos -PSProvider Filesystem -Root x:\data\content\videos  # Create a new PSDrive that points to a filesystem location
New-PSDrive -Name h -PSProvider FileSystem -Root '\\storage\h$\data' -Persist # Create a persistent mount on a drive letter, visible in Windows Explorer
Set-Location -Path videos:                                  # Switch into PSDrive context
Remove-PSDrive -Name xyz                                    # Delete a PSDrive
```

## Data Management (sort-object, where-object, group-object)
```powershell
Get-Process | Group-Object -Property Name                   # Group objects by property name
Get-Process | Sort-Object -Property Id                      # Sort objects by a given property name
Get-Process | Where-Object -FilterScript { $PSItem.Name -match '^c' } # Filter objects based on a property matching a value
gps | where Name -match '^c'                                # Abbreviated form of the previous statement
```

# Markdown
+ [Markdown cheatsheet](https://www.w3schools.io/file/markdown-cheatsheet/)
C:\Git\usecases\web scraping\web_scraping_case_4.py
