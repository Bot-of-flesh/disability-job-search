jobs = [
    {"company_name": "A社", "occupation": "事務", "location": "東京都"},
    {"company_name": "B社", "occupation": "事務", "location": "大阪府"},
    {"company_name": "C社", "occupation": "エンジニア","location": "東京都"},
    {"company_name": "D社", "occupation": "事務", "location": "東京都"},
]

def matches_location(job_location, desired_location):
    if job_location == desired_location:
        return True
    else:
        return False

def filter_jobs_by_location(jobs, desired_location):
    hit = []
    for job in jobs:
        if matches_location(job["location"], desired_location):
            hit.append(job)
    return hit

def filter_jobs(jobs, desired_occupation, desired_location):
    hit = []
    for job in jobs:
        if matches_location(job["location"], desired_location) and desired_occupation == job["occupation"]:
            hit.append(job)
    return hit

print(filter_jobs(jobs, "エンジニア", "東京都"))
