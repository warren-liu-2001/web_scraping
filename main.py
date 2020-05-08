import bs4
import requests


class JobObject:
    # Here for future implementation and messing around

    def __init__(self, name, company, location, EZAPP, desc, days_posted):
        self.name = name
        self.company = company
        self.location = location
        self.EZAPP = EZAPP
        self.desc = desc
        self.days_posted = days_posted


def search(maximum=10):
    list_urls = []
    job_title = None
    input_correct = False

    while not input_correct:
        job_title = input("What Type of Job do you want? ")
        if input("Is {} the job you want to apply for? Enter Yes to confirm" \
                         .format(job_title)) == 'Yes':
            input_correct = True

    Location_city = input("What Is Your city? ")
    Province = input("Your Province?")

    for i in range(maximum):
        URL = "https://ca.indeed.com/jobs?q={}&l={}%2C+{}".format(job_title, Location_city, Province) + '&start=' + str(10*i)
        list_urls.append(URL)

    return list_urls

def find_job_name(list_jobs):
    names = []
    for job in list_jobs:
        if None in job:
            names.append(None)

        names.append(job.text.strip())

    return names

if __name__ == '__main__':

    URLS = search(10)

    jerbs = []

    companies = []

    location = []

    dp = []

    for url in URLS:

        page = requests.get(url)

        soup = bs4.BeautifulSoup(page.content, 'html.parser', from_encoding="utf-8")

        # print(soup)

        # Now we have the HTML. Use beautifulsoup4 to filter the website.
        results = soup.find(id='resultsCol')

        # print(results.prettify())

        comps = results.find_all('span', class_='company')
        jobs = results.find_all('h2', class_='title')
        locs = results.find_all('span', class_='location accessible-contrast-color-location')
        date_posted = results.find_all('div', class_='jobsearch-SerpJobCard-footer')

        list_names = find_job_name(jobs)
        list_comps = find_job_name(comps)
        list_locs = find_job_name(locs)
        list_dates = find_job_name(date_posted)
        # print(list_names)

        jerbs.extend(list_names)
        companies.extend(list_comps)
        location.extend(list_locs)
        dp.extend(list_dates)

    df_core = [jerbs, companies, location, dp]
    print(df_core)
