from lxml import html
import requests
import datetime
import iso8601

scraperHeaders = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Refer": "https://gov.uk"
}

scraperEndpoint = requests.get('https://coronavirus.data.gov.uk/', headers=scraperHeaders)
tree = html.fromstring(scraperEndpoint.content)

def getDailyCases():
    casesDaily = tree.xpath('/html/body/div[4]/div[2]/div/main/article[1]/ul/li[2]/div[1]/ul/li[1]/div[2]/div/div/div/span[1]/text()')
    return casesDaily[0]

def getCases7DaysIncDec():
    prev7DaysCasesIncDec = tree.xpath('//*[@id="main-content"]/article[1]/ul/li[2]/div[1]/ul/li[3]/div/div/span/b/span/strong/text()')
    return prev7DaysCasesIncDec[0]

def getCases7DaysIncDecPercentage():
    prev7DaysCasesIncDecPercent = tree.xpath('/html/body/div[4]/div[2]/div/main/article[1]/ul/li[2]/div[1]/ul/li[3]/div/div/span/b/span/text()')
    return prev7DaysCasesIncDecPercent[0]

def getDailyDeaths():
    deathsDaily = tree.xpath('/html/body/div[4]/div[2]/div/main/article[1]/ul/li[3]/div[1]/ul/li[1]/div[2]/div/div/div/span[1]/text()')
    return deathsDaily[0]

def getDeaths7DaysIncDec():
    prev7DaysDeathsIncDec = tree.xpath('/html/body/div[4]/div[2]/div/main/article[1]/ul/li[3]/div[1]/ul/li[3]/div/div/span/b/span/strong/text()')
    return prev7DaysDeathsIncDec[0]

def getDeaths7DaysIncDecPercentage():
    prev7DaysDeathsIncDecPercent = tree.xpath('/html/body/div[4]/div[2]/div/main/article[1]/ul/li[3]/div[1]/ul/li[3]/div/div/span/b/span/text()')
    return prev7DaysDeathsIncDecPercent[0]

def getVaccinationsSecondDosePercentage():
    vaccinationSDPercentage = tree.xpath('/html/body/div[4]/div[2]/div/main/article[1]/ul/li[1]/figure/figcaption/ul/li[2]/div[1]/div/div/div/span/text()')
    return vaccinationSDPercentage[0]

def getDailyHospitalAdmissions():
    admissionsDaily = tree.xpath('/html/body/div[4]/div[2]/div/main/article[1]/ul/li[4]/div[1]/ul/li[1]/div[2]/div/div/div/span[1]/text()')
    return admissionsDaily[0]

def getHospitalAdmissions7DaysIncDec():
    prev7DaysAdmissionsIncDec = tree.xpath('/html/body/div[4]/div[2]/div/main/article[1]/ul/li[4]/div[1]/ul/li[3]/div/div/span/b/span/strong/text()')
    return prev7DaysAdmissionsIncDec[0]

def getHospitalAdmissions7DaysIncDecPercentage():
    prev7DaysAdmissionsIncDecPercent = tree.xpath('/html/body/div[4]/div[2]/div/main/article[1]/ul/li[4]/div[1]/ul/li[3]/div/div/span/b/span/text()')
    return prev7DaysAdmissionsIncDecPercent[0]

def getDashboardAnnouncementsBanner():
    dashboardAnnouncementIssueType = tree.xpath('/html/body/ul/li/div/strong/text()')

    # If there are no banner announcements, return none
    if not dashboardAnnouncementIssueType:
        dashboardAnnouncement = None
        return dashboardAnnouncement

    dashboardAnnouncementDate = tree.xpath('/html/body/ul/li/div/time/text()')
    dashboardAnnouncementText = tree.xpath('/html/body/ul/li/div/text()')

    # If the announcement does not relate to a data issue, return none
    if dashboardAnnouncementIssueType[0] != "data issue":
        dashboardAnnouncement = None
        return dashboardAnnouncement
    else:
        dashboardAnnouncement = "{}: {}{}".format(dashboardAnnouncementIssueType[0].capitalize(), dashboardAnnouncementDate[0], dashboardAnnouncementText[0])
        return dashboardAnnouncement

def getDashboardLastUpdate():
    dashboardLastUpdateTimeStamp = tree.xpath('//*[@id="last-update"]/time/@datetime')
    timestamp = dashboardLastUpdateTimeStamp[0]
    parsedISOTimestamp = iso8601.parse_date(timestamp)
    finalTimeStamp = datetime.datetime.strftime(parsedISOTimestamp, "%d/%m/%Y at %H:%M (GMT)")
    return finalTimeStamp

#Example
print(getDashboardLastUpdate())