# Covid Dashboard Scraper

Python XPath scraper for https://coronavirus.data.gov.uk/ - Functions in this script are used in the application backend

Contact: p2533140@my365.dmu.ac.uk // dom@dominic.sk

***

## Functions

**COVID-19 Case Data**

`getDailyCases()` - Returns positive COVID-19 cases over the last 24 hour period

`getCases7DaysIncDec()` - Returns the increase/decrease in COVID-19 cases over the last 7 days

`getCases7DaysIncDecPercentage()` - Returns the previous 7 days percentage increase/decrease in COVID-19 cases

**COVID-19 Death Data**

`getDailyDeaths()` - Returns confirmed deaths over 24 hours that were within 28 days of a positive test result

`getDeaths7DaysIncDec()` - Returns the increase/decrease in COVID-19 death over the last 7 days

`getDeaths7DaysIncDecPercentage()` - Returns the previous 7 days percentage increase/decrease in COVID-19 deaths

**Vaccination Data**

`getVaccinationsSecondDosePercentage()` - Returns the percentage total of the UK population (persons aged 12+) that has received a second dose/completed 1 full course of vaccination (i.e. J&J)

**Hospital Admissions Data**

`getDailyHospitalAdmissions()` - Returns the number of hospital admissions related to COVID-19 over the last 24 hour period

`getHospitalAdmissions7DaysIncDec()` - Returns the increase/decrease in COVID-19 related hospital admissions over the last 7 days

`getHospitalAdmissions7DaysIncDecPercentage()` - Returns the increase/decrease in COVID-19 related hospital admissions over the last 7 days as a percentage

**Dashboard Misc.**

`getDashboardAnnouncementsBanner()` - Returns the announcements banner text (if there are any announcements such as delays to data etc.)

`getDashboardLastUpdate()` - Returns the timestamp of the last update to the dashboard (coverted from an ISO8601 format->DD/MM/YYYY HH:MM)