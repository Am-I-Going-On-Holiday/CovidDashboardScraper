# Covid Dashboard Scraper

Python XPath scraper for https://coronavirus.data.gov.uk/

***

## Functions

**COVID-19 Case Data**

`getDailyCases()` - Returns positive COVID-19 cases over the last 24 hour period

`getCases7DaysIncDec()` - Returns the increase/decrease in COVID-19 cases over the last 7 days

`getCases7DaysIncDecPercentage()` - Returns the previous 7 day percentage increase/decrease in COVID-19 cases

**COVID-19 Death Data**

`getDailyDeaths()` - Returns confirmed deaths over 24 hours that were within 28 days of a positive test result

`getDeaths7DaysIncDec()` - Returns the increase/decrease in COVID-19 death over the last 7 days

`getDeaths7DaysIncDecPercentage()` - Returns the previous 7 day percentage increase/decrease in COVID-19 deaths