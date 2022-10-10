# Calendate

Calendate is a simple python package to work with calendars and dates.

## How to use Calendate

Calendate work with two different classes, `Date` and `Calendar`.
The `Calendar` class will use `Date` objects to work with.

This is how to create a `Date` and a `Calendar` object
```python
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
