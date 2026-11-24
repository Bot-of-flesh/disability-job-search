def matches_location(job_location, desired_location):
    if job_location == desired_location:
        return True
    else:
        return False
ifmatch = matches_location("東京都", "東京都")
print(ifmatch)
print(matches_location("大阪府", "東京都"))
print(matches_location("東京都新宿区", "東京都"))
