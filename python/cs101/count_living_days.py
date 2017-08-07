# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    if year1 < year2:
        while year1 < year2:
            if year2 % 4 != 0:
                days = days
            else:
                if year2 % 100 != 0 and month2 >= 2:
                    days = days + 1
                else:
                    if year2 % 400 != 0:
                        days = days
                    else:
                        if month2 >= 2:
                            days = days + 1
                        else:
                            days = days
                        
            if year1 % 4 != 0:
                days = days + 365
            else:
                if year1 % 100 != 0:
                    days = days + 366
                else:
                    if year1 % 400 != 0:
                        days = days + 365
                    else:
                        days = days + 366
            year1 = year1 + 1
        days = days
        return month_compare(month1,day1,month2,day2,days)
    if year1 == year2:
        days = days
        return month_compare(month1,day1,month2,day2,days)
        
def month_compare(month1,day1,month2,day2,days):
    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    cha = month2 - month1
    if cha > 1:
        month_day = 0
        real_month = month1 - 1
        while cha > 1:
            month_day = month_day + daysOfMonths[month1]
            cha = cha - 1
            month1 = month1 + 1
        if day1 == day2:
            days = days + 1
        day1 = daysOfMonths[real_month] - day1
        days = days + day1 + month_day + day2
        return days
    if cha == 1:
        day1 = daysOfMonths[month1 - 1] - day1
        days = days + day1 + day2
        return days
    if cha == 0:
        days = days + day2 - day1
        return days
    if cha < 0:
        month_day = 0
        while cha < 0:
            month_day = month_day + daysOfMonths[month1 - 2]
            cha = cha + 1
        day2 = daysOfMonths[month2 - 1] - day2
        days = days - day1 - month_day - day2
        return days        

        
        
        


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
