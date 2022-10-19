# Calendate

Calendate is a simple python package to work with calendars and dates.

## How to use Calendate

Calendate work with two different classes, `Date` and `Calendar`.
The `Calendar` class will use `Date` objects to work with.

This is how to create a `Date` and a `Calendar` object
```python
from calendate import *

my_date = Date('2022', '10', '07')
my_calendar = Calendar()

```
You can change the `my_date` object using the method `set_date()` and passing the new year, month, and day
values.
To check if the `my_date` object is a valid date use the `is_date_valid()` function, it will return True
if the date is valid, and False if it isn't
```python
my_date = Date('2022', '10', '07')
my_calendar = Calendar()

print(is_date_valid(my_date))
```
You can check if the year of the `my_date` object is a leap year using the `is_leap()` function, return
True if is leap, and False if it isn't
```python
my_date = Date('2022', '10', '07')
my_calendar = Calendar()

print(is_leap(my_date))
```

## Using the Calendar object
List of methods from the `Calendar` object
- `diff_in_years`
- `diff_in_months`
- `diff_in_days`
- `bigger_date`
- `get_weekday`
- `sum_days`
- `sum_months`
- `sum_years`
- `format_date`

### diff_in_years
The `diff_in_years` method will take two dates as arguments, and will return the difference in years of the given dates.

### diff_in_months
The `diff_in_months` method will take two dates as arguments, and will return the difference in months of the given dates.

### diff_in_days
The `diff_in_days` method will take two dates as arguments, and will return the difference in days of the given dates.

### bigger_date
The `bigger_date` method will take two dates as arguments, and will return `0` if the first date is bigger, or `1` if the second date is bigger, or `None` if the dates are equal

### get_weekday
The `get_weekday` method will take one date as argument, and will return the name of the day from the given date

### sum_days
The `sum_days` method will take one date and one integer value as arguments, it will add the integer value as days to the date object, and will return a date object

### sum_months
The `sum_months` method will take one date and one integer value as arguments, it will add the integer value as months to the date object, and will return a date object

### sum_years
The `sum_years` method will take one date and one integer value as arguments, it will add the integer value as years to the date object, and will return a date object

### format_date
The `format_date` method will take one date and one string value as arguments, it will return a string with the formated date.
The string that you pass will have to contain some keywords to identify where you want to place the year, month or day.
Example:
```python
my_date = Date('2022', '10', '07')
my_calendar = Calendar()

print(my_calendar(my_date, '%wd, %mn %d, %y'))
```
This will print `friday, october 07, 2022`
You can acctually type anything in the string
```python
print(my_calendar(my_date, 'banana %wd, %mn %d, %y'))
```
This will print `banana friday, october 07, 2022`

Keywords you can use:
- `%y` (year)
- `%m` (month)
- `%d` (day)
- `%wd` (weekday)
- `%mn` (month name)
- `%wda` (weekday abbreviated)
- `%mna` (month name abbreviated)

# Installation
To install the calendate package, use
```
pip install calendate
```
