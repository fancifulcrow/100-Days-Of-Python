import requests
from bs4 import BeautifulSoup

import json

# extract job postings information
def extractJobPostings():
    job_post_list = []

    # set the search term and location
    keywords = ["python", "web development", "engineer"]
    locations = ["Lagos", "Abuja", "Tokyo", "Toronto", "Berlin"]

    for keyword in keywords:
        for location in locations:
            # create the URL string
            url = f'https://www.linkedin.com/jobs/search?keywords={keyword}&location={location}&position=1&pageNum=2'

            # send a GET request to the URL
            response = requests.get(url=url)

            # parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            for job in soup.find_all(name='div', class_='job-search-card'):
                title = job.find(name='h3', class_='base-search-card__title').text.strip()
                company = job.find(name='h4', class_='base-search-card__subtitle').text.strip()
                location = job.find(name='span', class_='job-search-card__location').text.strip()
                url = job.find(name='a', class_='base-card__full-link').get('href').split("?")[0]

                if job not in job_post_list:
                    job_post_list.append({'title': title, 'company' : company, 'location' : location, 'url' : url})

    # return the data
    return job_post_list

with open("jobs.json", mode="w") as file:
    json.dump(obj=extractJobPostings(), fp=file)