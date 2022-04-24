from curses import baudrate
import imp
import re


import requests
import json


base_url = 'https://jp-mah.herokuapp.com/api'
# base_url = 'http://127.0.0.1:8000/api'
auth_header = {
    'Authorization': f"Bearer {requests.post(base_url + '/token/', data={'username': 'mah', 'password': '1234'}).json()['access']}"}

with open('/home/mah/projects/programming/automation/others/problems.json', 'r') as f:
    problems = json.load(f)
    print(problems[0].keys())

res = requests.get(f'{base_url}/problems/?limit=10000',
                   headers=auth_header).json()['results']
print(len(res))
absent_problems = [x for x in problems if x['name'].strip()
                   not in [y['name'].strip() for y in res]]
for problem in absent_problems:
    problem['question_html'] = problem['questionHtml']
    problem['solution_html'] = problem['solutionHtml']
    problem['companies'] = problem['tags']
    problem['difficulty'] = problem['difficulty'].lower()
    # find floating part of a string
    problem['acceptance'] = float(re.findall(r'\d+\.\d+', problem['acceptance'])[0])
    problem.pop('questionHtml')
    problem.pop('solutionHtml')
    problem.pop('tags')
    res = requests.post(f'{base_url}/problems/', headers=auth_header, data=problem)
    print(res.status_code)
