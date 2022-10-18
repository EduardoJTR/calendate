month_names = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
               'september', 'october', 'november', 'december']

month_len = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',
            'saturday', 'sunday']


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.__correct_format()

    def __correct_format(self):
        if len(self.day) < 2:
            self.day = '0' + self.day
        if len(self.month) < 2:
            self.month = '0' + self.month

    def date_str(self, sep=None):
        if sep is None:
            sep = '-'
        return self.day + sep + self.month + sep + self.year

    def date(self):
        return [self.day, self.month, self.year]

    def set_date(self, year=None, month=None, day=None):
        if year is not None:
            self.year = year
        if month is not None:
            self.month = month
        if day is not None:
            self.day = day
        self.__correct_format()

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def get_int_year(self):
        return int(self.year)

    def get_int_month(self):
        return int(self.month)

    def get_int_day(self):
        return int(self.day)


def is_leap(date: Date = None, direct_year=None):
    if direct_year is None:
        year = int(date.get_year())
    else:
        year = direct_year

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def is_date_valid(date: Date):
    try:
        year = int(date.get_year())
        month = int(date.get_month())
        day = int(date.get_day())
    except:
        return False

    # Local month length list, then if it is leap, february can be changed to 29 days
    local_month_len = month_len
    if is_leap(date):
        local_month_len[1] = 29

    # Check if year is bigger than 0
    if year > 0:
        # Check if month is between 1 and 12
        if 0 < month < 13:
            # Check if in current month, the maximum number of days isn't overcome
            if 0 < day <= month_len[month - 1]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


class Calendar:
    def __init__(self):
        self.ref_date_info = {'year': '2023', 'month': '01', 'day': '01', 'weekday_index': 6}

    def diff_in_years(self, first_date: Date, second_date: Date):
        difference = int(first_date.get_year()) - int(second_date.get_year())
        return abs(difference)

    # Smaller date has to be the first argument
    def diff_in_months(self, first_date: Date, second_date: Date):
        fd_month = int(first_date.get_month())
        sd_month = int(second_date.get_month())

        if first_date.get_year() == second_date.get_year():
            difference = fd_month - sd_month
        else:
            difference = abs(fd_month - 12)
            # For each complete year between both dates, there are 12 months
            diff_years = self.diff_in_years(first_date, second_date) - 1
            difference += 12 * diff_years
            difference += sd_month

        return abs(difference)

    # Pass smaller date first
    def diff_in_days(self, first_date: Date, second_date: Date):
        # Get first date information
        fd_year = int(first_date.get_year())
        fd_month = int(first_date.get_month())
        fd_day = int(first_date.get_day())

        # Get second date information
        sd_year = int(second_date.get_year())
        sd_month = int(second_date.get_month())
        sd_day = int(second_date.get_day())

        difference = 0
        local_month_len = month_len

        if is_leap(direct_year=fd_year):
            local_month_len[1] = 29

        while not (fd_day == sd_day and fd_month == sd_month and fd_year == sd_year):
            difference += 1
            fd_day += 1

            if fd_day > local_month_len[fd_month - 1]:
                fd_month += 1
                fd_day = 1
                if fd_month > 12:
                    fd_month = 1
                    fd_year += 1
                    if is_leap(direct_year=fd_year):
                        local_month_len[1] = 29
                    else:
                        local_month_len[1] = 28

        return difference

    def bigger_date(self, first_date: Date, second_date: Date):
        # Get first date information
        fd_year = int(first_date.get_year())
        fd_month = int(first_date.get_month())
        fd_day = int(first_date.get_day())

        # Get second date information
        sd_year = int(second_date.get_year())
        sd_month = int(second_date.get_month())
        sd_day = int(second_date.get_day())

        if fd_year > sd_year:
            return 0
        elif fd_year < sd_year:
            return 1
        else:
            if fd_month > sd_month:
                return 0
            elif fd_month < sd_month:
                return 1
            else:
                if fd_day > sd_day:
                    return 0
                elif fd_day < sd_day:
                    return 1
                else:
                    return None

    def get_weekday(self, date: Date):
        reference = Date(self.ref_date_info['year'], self.ref_date_info['month'], self.ref_date_info['day'])
        weekday_index = self.ref_date_info['weekday_index']

        # If reference date is smaller, the weekday shifting is positive
        if self.bigger_date(reference, date) == 1:
            difference_in_days = self.diff_in_days(reference, date)
            weekday_shift = difference_in_days % 7

            # Weekday_index gets bigger
            for _ in range(weekday_shift):
                weekday_index += 1
                if weekday_index > 6:
                    weekday_index = 0
        # If the reference is bigger, then the shifting is negative
        else:
            difference_in_days = self.diff_in_days(date, reference)
            weekday_shift = difference_in_days % 7

            # weekday_index gets smaller
            for _ in range(weekday_shift):
                weekday_index -= 1
                if weekday_index < 0:
                    weekday_index = 6

        return weekdays[weekday_index]

    def sum_days(self, date: Date, days_to_sum):
        days = date.get_int_day()
        months = date.get_int_month()
        years = date.get_int_year()

        local_month_len = month_len
        if is_leap(date):
            local_month_len[1] = 29

        while days_to_sum > 0:
            days_to_sum -= 1
            days += 1
            if days > local_month_len[months - 1]:
                months += 1
                days = 1
                if months > 12:
                    # Checks if year is leap
                    if is_leap(date):
                        local_month_len[1] = 29
                    else:
                        local_month_len[1] = 28
                    months = 1
                    years += 1
        date.set_date(str(years), str(months), str(days))
        return date

    def sum_months(self, date: Date, months_to_sum):
        months = date.get_int_month()
        years = date.get_int_year()

        while months_to_sum > 0:
            months_to_sum -= 1
            months += 1
            if months > 12:
                months = 1
                years += 1
        date.set_date(year=str(years), month=str(months))
        return date

    def sum_years(self, date: Date, years_to_sum):
        years = date.get_int_year()
        years += years_to_sum
        date.set_date(year=str(years))

    def format_date(self, date: Date, fmt: str):
        if '%wda' in fmt:
            weekday = self.get_weekday(date)
            fmt = fmt.replace('%wda', weekday[:3])
        if '%mna' in fmt:
            month_name = month_names[date.get_int_month() - 1]
            fmt = fmt.replace('%mna', month_name[:3])

        if '%wd' in fmt:
            weekday = self.get_weekday(date)
            fmt = fmt.replace('%wd', weekday)
        if '%mn' in fmt:
            month_name = month_names[date.get_int_month() - 1]
            fmt = fmt.replace('%mn', month_name)

        fmt = fmt.replace('%y', date.get_year())
        fmt = fmt.replace('%m', date.get_month())
        fmt = fmt.replace('%d', date.get_day())

        return fmt
