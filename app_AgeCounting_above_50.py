import requests

url = "https://coderbyte.com/api/challenges/json/age-counting"

data = requests.get(url).json()['data']

'''Solution 1'''
def get50plusAge():
    count = 0
    for item in data.split(','):
        ds = item.split('=')
        if ds[0].strip() == "age" and int(ds[1]) >= 50:
            count += 1

    return count

'''Solution 2'''
def get50plusAge2():
    x = lambda a: a.split('=')[0].strip()=="age" and int(a.split('=')[1])>=50
    return int(len(list(filter(x,data.split(',')))))

print(get50plusAge())
print(get50plusAge2())