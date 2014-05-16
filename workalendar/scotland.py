"""
Scotland specific module.

"""
# Since Scotland territories have a lot of different variations, it has become
# necessary to split this module and associated tests
from workalendar.core import WesternCalendar, ChristianMixin
from workalendar.core import MON


# Mixins to make it easier to put parameters
class GoodFridayMixin(object):
    include_good_friday = True


class EasterMondayMixin(object):
    include_easter_monday = True


class SpringHolidayFirstMondayAprilMixin(object):
    def get_spring_holiday(self, year):
        return (
            Scotland.get_nth_weekday_in_month(year, 4, MON),
            "Spring Holiday"
        )


class SpringHolidaySecondMondayAprilMixin(object):
    def get_spring_holiday(self, year):
        return (
            Scotland.get_nth_weekday_in_month(year, 4, MON, 2),
            "Spring Holiday"
        )


class Scotland(WesternCalendar, ChristianMixin):
    "Scotland"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 2, "New Year Holiday"),
        (12, 26, "Boxing Day"),
        (11, 30, "St Andrew's Day"),
    )

    def get_may_day(self, year):
        return (
            Scotland.get_nth_weekday_in_month(year, 5, MON),
            "May Day"
        )

    def get_spring_holiday(self, year):
        return (
            Scotland.get_last_weekday_in_month(year, 5, MON),
            "Spring Holiday"
        )

    def get_summer_holiday(self, year):
        return (
            Scotland.get_nth_weekday_in_month(year, 8, MON),
            "Summer Holiday"
        )

    # Specific holidays
    def get_winter_holiday(self, year):
        return (
            Scotland.get_nth_weekday_in_month(year, 2, MON),
            "Winter Holiday"
        )

    def get_first_monday_march(self, year):
        return (
            Scotland.get_nth_weekday_in_month(year, 3, MON),
            "First Monday in March"
        )

    def get_last_monday_march(self, year):
        return (
            Scotland.get_last_weekday_in_month(year, 3, MON),
            "Last Monday in March"
        )

    def get_variable_days(self, year):
        days = super(Scotland, self).get_variable_days(year)
        days.append(self.get_may_day(year))
        days.append(self.get_spring_holiday(year))
        days.append(self.get_summer_holiday(year))
        return days


class ScotlandInverness(SpringHolidayFirstMondayAprilMixin, Scotland):
    "Inverness (Scotland)"
    def get_variable_days(self, year):
        days = super(ScotlandInverness, self).get_variable_days(year)
        days.append(self.get_winter_holiday(year))
        days.append(self.get_first_monday_march(year))
        return days


class ScotlandLochaber(Scotland):
    "Lochaber (Scotland)"
    def get_variable_days(self, year):
        days = super(ScotlandLochaber, self).get_variable_days(year)
        days.append(self.get_last_monday_march(year))
        return days


class ScotlandAngus(SpringHolidaySecondMondayAprilMixin, Scotland):
    "Angus (Scotland)"


class ScotlandAyr(GoodFridayMixin, EasterMondayMixin, Scotland):
    "Ayr (Scotland)"


class ScotlandCarnoustie(SpringHolidayFirstMondayAprilMixin, Scotland):
    "Carnoustie (Scotland)"


class ScotlandDumfriesGalloway(GoodFridayMixin, Scotland):
    "Dumfries and Galloway (Scotland)"


class ScotlandEastDunbartonshire(GoodFridayMixin, EasterMondayMixin, Scotland):
    "East Dunbartonshire (Scotland)"


class ScotlandElgin(SpringHolidaySecondMondayAprilMixin, Scotland):
    "Elgin (Scotland)"


class ScotlandDundee(SpringHolidayFirstMondayAprilMixin, Scotland):
    "Dundee (Scotland)"


class ScotlandFife(SpringHolidayFirstMondayAprilMixin, Scotland):
    "Fife (Scotland)"


class ScotlandEdinburgh(GoodFridayMixin, EasterMondayMixin, Scotland):
    "Edinburgh (Scotland)"

    def get_spring_holiday(self, year):
        easter = self.get_easter_monday(year)
        spring_holiday = Scotland.get_nth_weekday_in_month(year, 4, MON, 3)
        if easter == spring_holiday:
            spring_holiday = Scotland.get_nth_weekday_in_month(year, 4, MON, 2)

        return (
            spring_holiday,
            "Spring Holiday"
        )


class ScotlandFalkirk(GoodFridayMixin, EasterMondayMixin, Scotland):
    "Falkirk (Scotland)"


class ScotlandGlasgow(EasterMondayMixin, Scotland):
    "Glasgow (Scotland)"


class ScotlandInverclyde(GoodFridayMixin, EasterMondayMixin, Scotland):
    "Inverclyde (Scotland)"

    def get_spring_holiday(self, year):
        return (
            Scotland.get_last_weekday_in_month(year, 4, MON),
            "Spring Holiday"
        )


class ScotlandKilmarnock(GoodFridayMixin, EasterMondayMixin, Scotland):
    "Kilmarnock (Scotland)"


class ScotlandMonifieth(SpringHolidayFirstMondayAprilMixin, Scotland):
    "Monifieth (Scotland)"


class ScotlandNorthLanarkshire(EasterMondayMixin, Scotland):
    "North Lanarkshire (Scotland)"


class ScotlandPaisley(GoodFridayMixin, EasterMondayMixin, Scotland):
    "Paisley (Scotland)"


class ScotlandPerth(SpringHolidayFirstMondayAprilMixin, Scotland):
    "Perth (Scotland)"


class ScotlandScottishBorders(SpringHolidayFirstMondayAprilMixin, Scotland):
    "Scottish Borders (Scotland)"


class ScotlandStirling(GoodFridayMixin, EasterMondayMixin, Scotland):
    "Stirling (Scotland)"


class ScotlandSouth(GoodFridayMixin, Scotland):
    "South (Scotland)"


class ScotlandSouthLanarkshire(GoodFridayMixin, EasterMondayMixin, Scotland):
    "South Lanarkshire (Scotland)"


class ScotlandWestDunbartonshire(GoodFridayMixin, EasterMondayMixin, Scotland):
    "West Dunbartonshire (Scotland)"