from lxml import html
import requests
import datetime
import iso8601

def initScraper():
    scraperHeaders = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Referer": "gov.uk"
    }
    scraperEndpoint = requests.get('https://coronavirus.data.gov.uk/', headers=scraperHeaders)
    tree = html.fromstring(scraperEndpoint.content)
    return tree


def addCommas(n):
    return '{:,}'.format(n)

def getDailyCases():
    casesAPIEndpoint = 'https://coronavirus.data.gov.uk/api/v1/data?filters=areaType=overview&structure=%7B%22date%22:%22date%22,%22areaName%22:%22areaName%22,%22newCasesByPublishDate%22:%22newCasesByPublishDate%22,%22cumCasesByPublishDate%22:%22cumCasesByPublishDate%22%7D'
    # From the JSON data, get the latest 'newAdmissions' value (nested dictionary)
    casesDaily = requests.get(casesAPIEndpoint).json()['data'][0]['newCasesByPublishDate']
    return addCommas(casesDaily)

def getCases7DaysIncDec():
    prev7DaysCasesIncDec = initScraper().xpath('//*[@id="main-content"]/article[1]/ul/li[2]/div[1]/ul/li[2]/div/div/span/b/span/strong/text()')
    # Return 0 if there is no change in cases increase/decrease
    if not prev7DaysCasesIncDec:
        return 0
    return prev7DaysCasesIncDec[0]

def getCases7DaysIncDecPercentage():
    prev7DaysCasesIncDecPercent = initScraper().xpath('/html/body/div[4]/div[2]/div/main/article[1]/ul/li[2]/div[1]/ul/li[2]/div/div/span/b/span/text()')
    # Return 0 if there is no change in cases increase/decrease percentage
    if not prev7DaysCasesIncDecPercent:
        return 0
    return prev7DaysCasesIncDecPercent[0]

def getDailyDeaths():
    deathsAPIEndpoint = 'https://coronavirus.data.gov.uk/api/v1/data?filters=areaType=overview&structure=%7B%22date%22:%22date%22,%22areaName%22:%22areaName%22,%22newDeaths28DaysByDeathDate%22:%22newDeaths28DaysByDeathDate%22,%22cumDeaths28DaysByDeathDate%22:%22cumDeaths28DaysByDeathDate%22%7D'
    # From the JSON data, get the latest 'newAdmissions' value (nested dictionary)
    deathsDaily = requests.get(deathsAPIEndpoint).json()['data'][0]['newDeaths28DaysByDeathDate']
    return addCommas(deathsDaily)

def getDeaths7DaysIncDec():
    prev7DaysDeathsIncDec = initScraper().xpath('/html/body/div[4]/div[2]/div/main/article[1]/ul/li[3]/div[1]/ul/li[2]/div/div/span/b/span/strong/text()')
    # Return 0 if there is no change in deaths increase/decrease
    if not prev7DaysDeathsIncDec:
        return 0
    return prev7DaysDeathsIncDec[0]

def getDeaths7DaysIncDecPercentage():
    prev7DaysDeathsIncDecPercent = initScraper().xpath('/html/body/div[4]/div[2]/div/main/article[1]/ul/li[3]/div[1]/ul/li[2]/div/div/span/b/span/text()')
    # Return 0 if there is no change in deaths increase/decrease percentage
    if not prev7DaysDeathsIncDecPercent:
        return 0
    return prev7DaysDeathsIncDecPercent[0]

def getVaccinationsSecondDosePercentage():
    vaccinationSDPercentage = initScraper().xpath('/html/body/div[4]/div[2]/div/main/article[1]/ul/li[1]/figure/figcaption/ul/li[2]/div[1]/div/div/div/span/text()')
    return vaccinationSDPercentage[0]

def getVaccinationsBoosterPercentage():
    vaccinationBoosterPercentage = initScraper().xpath('//*[@id="main-content"]/article[1]/ul/li[1]/figure/figcaption/ul/li[3]/div[1]/div/div/div/span/text()')
    return vaccinationBoosterPercentage[0]

def getDailyHospitalAdmissions():
    admissionsAPIEndpoint = 'https://coronavirus.data.gov.uk/api/v1/data?filters=areaType=overview&structure=%7B%22date%22:%22date%22,%22areaName%22:%22areaName%22,%22newAdmissions%22:%22newAdmissions%22,%22cumAdmissions%22:%22cumAdmissions%22%7D'
    #From the JSON data, get the latest 'newAdmissions' value (nested dictionary)
    admissionsDaily = requests.get(admissionsAPIEndpoint).json()['data'][0]['newAdmissions']
    return addCommas(admissionsDaily)

def getHospitalAdmissions7DaysIncDec():
    prev7DaysAdmissionsIncDec = initScraper().xpath('/html/body/div[4]/div[2]/div/main/article[1]/ul/li[4]/div[1]/ul/li[2]/div/div/span/b/span/strong/text()')
    # Return 0 if there is no change in admissions increase/decrease
    if not prev7DaysAdmissionsIncDec:
        return 0
    return prev7DaysAdmissionsIncDec[0]

def getHospitalAdmissions7DaysIncDecPercentage():
    #prev7DaysAdmissionsIncDecPercent = initScraper().xpath('/html/body/div[4]/div[2]/div/main/article[1]/ul/li[4]/div[1]/ul/li[3]/div/div/span/b/span/text()')
    prev7DaysAdmissionsIncDecPercent = initScraper().xpath('/html/body/div[4]/div[2]/div/main/article[1]/ul/li[4]/div[1]/ul/li[2]/div/div/span/b/span/text()')
    # Return 0 if there is no change in admissions increase/decrease percentage
    if not prev7DaysAdmissionsIncDecPercent:
        return 0
    return prev7DaysAdmissionsIncDecPercent[0]

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
        dashboardAnnouncement = "{}: {}{}".format(dashboardAnnouncementIssueType[0].capitalize(), dashboardAnnouncementDate[0], dashboardAnnouncementText[0])
        return dashboardAnnouncement

def getDashboardLastUpdate():
    dashboardLastUpdateTimeStamp = initScraper().xpath('//*[@id="last-update"]/time/@datetime')
    timestamp = dashboardLastUpdateTimeStamp[0]
    parsedISOTimestamp = iso8601.parse_date(timestamp)
    finalTimeStamp = datetime.datetime.strftime(parsedISOTimestamp, "%d/%m/%Y at %H:%M (GMT)")
    return finalTimeStamp

#print(f"Daily cases: {getDailyCases()} - ±{getCases7DaysIncDec()} cases {getCases7DaysIncDecPercentage()} from previous 7 days")
#print(f"Daily deaths: {getDailyDeaths()} - ±{getDeaths7DaysIncDec()} deaths {getDeaths7DaysIncDecPercentage()} from previous 7 days")
#print(f"Daily hospital admissions: {getDailyHospitalAdmissions()} - ±{getHospitalAdmissions7DaysIncDec()} admissions {getHospitalAdmissions7DaysIncDecPercentage()} from previous 7 days")
#print(f"Vaccinations: {getVaccinationsSecondDosePercentage()} second dose, {getVaccinationsBoosterPercentage()} third dose/booster")
#print(f"Last updated: {getDashboardLastUpdate()} - Source: https://coronavirus.data.gov.uk/")
#print(getDashboardAnnouncementsBanner())