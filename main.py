"""
covidDashboard.py
Script used to scrape the coronavirus.gov.uk dashboard
Uses either scraping (picking out data from inside HTML elements) or calling certain API functions
"""
from lxml import html
import requests
import datetime
import iso8601
import time

""" Headers (such as browser user agent) to make ourselves look more like a 'human' browsing the site """
scraperHeaders = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Referer": "gov.uk"
}

""" Function to initialise the scraper with the headers, which then downloads the page """
def initScraper():
    scraperEndpoint = requests.get('https://coronavirus.data.gov.uk/', headers=scraperHeaders)
    tree = html.fromstring(scraperEndpoint.content)
    return tree

""" Simple function to format numbers (1000 -> 1,000) """
def addCommas(n):
    return '{:,}'.format(n)

""" Non-scraper function: Obtain new daily cases from the JSON API """
def getDailyCases():
    casesAPIEndpoint = 'https://coronavirus.data.gov.uk/api/v1/data?filters=areaType=nation;areaName=England&structure={"date":"date","newCasesBySpecimenDate":"newCasesBySpecimenDate","cumCasesBySpecimenDate":"cumCasesBySpecimenDate"}'
    casesDaily = requests.get(casesAPIEndpoint, headers=scraperHeaders).json()['data'][0]['newCasesBySpecimenDate']
    return addCommas(casesDaily)

""" Scraper function: Get the 7 day increase/decrease in cases """
def getCases7DaysIncDec():
    prev7DaysCasesIncDec = initScraper().xpath('//*[@id="main-content"]/article[1]/ul/li[2]/div[1]/ul/li[2]/div/div/span/b/span/strong/text()')
    # Return 0 if there is no change in cases increase/decrease
    if not prev7DaysCasesIncDec:
        return 0
    return prev7DaysCasesIncDec[0]

""" Scraper function: Get the 7 day increase/decrease percentage in cases """
def getCases7DaysIncDecPercentage():
    prev7DaysCasesIncDecPercent = initScraper().xpath('/html/body/div[5]/div[2]/div/main/article[1]/ul/li[2]/div[1]/ul/li[2]/div/div/span/b/span/text()')
    # Return 0 if there is no change in cases increase/decrease percentage
    if not prev7DaysCasesIncDecPercent:
        return 0
    return prev7DaysCasesIncDecPercent[0]

""" Non-scraper function: Obtain new daily deaths from the JSON API """
def getDailyDeaths():
    deathsAPIEndpoint = 'https://coronavirus.data.gov.uk/api/v1/data?filters=areaType=nation;areaName=England&structure={%22date%22:%22date%22,%22newDeaths28DaysByDeathDate%22:%22newDeaths28DaysByDeathDate%22,%22cumDeaths28DaysByDeathDate%22:%22cumDeaths28DaysByDeathDate%22}'
    deathsDaily = requests.get(deathsAPIEndpoint, headers=scraperHeaders).json()['data'][0]['newDeaths28DaysByDeathDate']
    return addCommas(deathsDaily)

""" Scraper function: Get the 7 day increase/decrease in deaths """
def getDeaths7DaysIncDec():
    prev7DaysDeathsIncDec = initScraper().xpath('/html/body/div[5]/div[2]/div/main/article[1]/ul/li[3]/div[1]/ul/li[2]/div/div/span/b/span/strong/text()')
    # Return 0 if there is no change in deaths increase/decrease
    if not prev7DaysDeathsIncDec:
        return 0
    return prev7DaysDeathsIncDec[0]

""" Scraper function: Get the 7 day increase/decrease percentage in deaths """
def getDeaths7DaysIncDecPercentage():
    prev7DaysDeathsIncDecPercent = initScraper().xpath('/html/body/div[5]/div[2]/div/main/article[1]/ul/li[3]/div[1]/ul/li[2]/div/div/span/b/span/text()')
    # Return 0 if there is no change in deaths increase/decrease percentage
    if not prev7DaysDeathsIncDecPercent:
        return 0
    return prev7DaysDeathsIncDecPercent[0]

""" Scraper function: Get the vaccine second dose percentage """
def getVaccinationsSecondDosePercentage():
    vaccinationSDPercentage = initScraper().xpath('/html/body/div[5]/div[2]/div/main/article[1]/ul/li[1]/figure/figcaption/ul/li[2]/div[1]/div/div/div/span/text()')
    return vaccinationSDPercentage[0]

""" Scraper function: Get the vaccine booster dose percentage """
def getVaccinationsBoosterPercentage():
    vaccinationBoosterPercentage = initScraper().xpath('//*[@id="main-content"]/article[1]/ul/li[1]/figure/figcaption/ul/li[3]/div[1]/div/div/div/span/text()')
    return vaccinationBoosterPercentage[0]

""" Non-scraper function: Obtain new daily (delayed by 3-5 working days) hospital admissions from the JSON API """
def getDailyHospitalAdmissions():
    admissionsAPIEndpoint = 'https://coronavirus.data.gov.uk/api/v1/data?filters=areaType=nation;areaName=England&structure={"date":"date","newAdmissions":"newAdmissions","cumAdmissions":"cumAdmissions"}'
    admissionsDaily = requests.get(admissionsAPIEndpoint, headers=scraperHeaders).json()['data'][0]['newAdmissions']
    return addCommas(admissionsDaily)

""" Scraper function: Get the 7 day increase/decrease in hospital admissions """
def getHospitalAdmissions7DaysIncDec():
    prev7DaysAdmissionsIncDec = initScraper().xpath('/html/body/div[5]/div[2]/div/main/article[1]/ul/li[4]/div[1]/ul/li[2]/div/div/span/b/span/strong/text()')
    # Return 0 if there is no change in admissions increase/decrease
    if not prev7DaysAdmissionsIncDec:
        return 0
    return prev7DaysAdmissionsIncDec[0]

""" Scraper function: Get the 7 day increase/decrease percentage in hospital admissions """
def getHospitalAdmissions7DaysIncDecPercentage():
    prev7DaysAdmissionsIncDecPercent = initScraper().xpath('/html/body/div[5]/div[2]/div/main/article[1]/ul/li[4]/div[1]/ul/li[2]/div/div/span/b/span/text()')
    # Return 0 if there is no change in admissions increase/decrease percentage
    if not prev7DaysAdmissionsIncDecPercent:
        return 0
    return prev7DaysAdmissionsIncDecPercent[0]

""" Non-scraper function (not used in applicaton): Obtain occupied mechanical ventilator beds from the JSON API """
def getDailyHopsitalOccupiedMVBeds():
    occupiedMVBedsAPIEndpoint = 'https://coronavirus.data.gov.uk/api/v1/data?filters=areaType=overview&structure={%22date%22:%22date%22,%22areaName%22:%22areaName%22,%22covidOccupiedMVBeds%22:%22covidOccupiedMVBeds%22}'
    occupiedMVBedsDaily = requests.get(occupiedMVBedsAPIEndpoint, headers=scraperHeaders).json()['data'][0]['covidOccupiedMVBeds']
    return addCommas(occupiedMVBedsDaily)

""" Scraper function: If there is a data issue (dashboard announcement), get the announcement information """
def getDashboardAnnouncementsBanner():
    dashboardAnnouncementIssueType = initScraper().xpath('/html/body/ul/li/div/strong/text()')

    # If there are no banner announcements, return none
    if not dashboardAnnouncementIssueType:
        dashboardAnnouncement = None
        return dashboardAnnouncement

    dashboardAnnouncementDate = initScraper().xpath('/html/body/ul/li/div/time/text()')
    dashboardAnnouncementText = initScraper().xpath('/html/body/ul/li/div/text()')

    # If the announcement does not relate to a data issue, return none
    if dashboardAnnouncementIssueType[0] != "data issue":
        dashboardAnnouncement = None
        return dashboardAnnouncement
    else:
        dashboardAnnouncement = f"{dashboardAnnouncementIssueType[0].capitalize()}: {dashboardAnnouncementDate[0]}{dashboardAnnouncementText[0]}"
        return dashboardAnnouncement

""" Function to convert the timestamp from ISO8601 (i.e. 2022-05-19T22:56:36Z -> 19/05/2022 22:56:36 -> 19/05/2022 at 22:56 (GMT) ) """
def getDashboardLastUpdate():

    """ Check if BST (British Summer Time / +01:00) is in effect """
    def checkBST():
        return bool(time.localtime().tm_isdst)

    dashboardLastUpdateTimeStamp = initScraper().xpath('//*[@id="last-update"]/time/@datetime')
    timestamp = dashboardLastUpdateTimeStamp[0]
    parsedISOTimestamp = iso8601.parse_date(timestamp)

    """ (Summer time conversion) If it is currently the summer, add an extra hour to the time """
    if checkBST() is True:
        parsedISOTimestamp = parsedISOTimestamp + datetime.timedelta(hours=1)
        return parsedISOTimestamp.strftime("%d/%m/%Y at %H:%M (GMT)")

    return parsedISOTimestamp.strftime("%d/%m/%Y at %H:%M (GMT)")


""" Uncomment lines below and test it out - as of August 2022, data is now reported once a week """

#print(f"Daily cases: {getDailyCases()} - ±{getCases7DaysIncDec()} cases {getCases7DaysIncDecPercentage()} from previous 7 days")
#print(f"Daily deaths: {getDailyDeaths()} - ±{getDeaths7DaysIncDec()} deaths {getDeaths7DaysIncDecPercentage()} from previous 7 days")
#print(f"Daily hospital admissions: {getDailyHospitalAdmissions()} - ±{getHospitalAdmissions7DaysIncDec()} admissions {getHospitalAdmissions7DaysIncDecPercentage()} from previous 7 days")
#print(f"Daily hospital occupied MV beds: {getDailyHopsitalOccupiedMVBeds()}")
#print(f"Vaccinations: {getVaccinationsSecondDosePercentage()} second dose, {getVaccinationsBoosterPercentage()} third dose/booster")
#print(f"Last updated: {getDashboardLastUpdate()} - Source: https://coronavirus.data.gov.uk/")
#print(f"Dashboard Banner Announcement (if any): {getDashboardAnnouncementsBanner()}")
#print(f"{getDashboardLastUpdate()}")