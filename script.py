#!/usr/bin/env python
import os
import re
import subprocess
import requests
import json
import urllib3
import sys
import argparse
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Github Token
github_token_migration = os.getenv('Bearer '+ 'GitHub')

# ArgParser Section
parser = argparse.add_argument("--user", "-u1", help="User Name")
parser = argparse.add_argument("--password", "-p1", help="Password")
parser = argparse.add_argument("--Github_Repo_Name", "gb", help="Github Repository Name")
parser = argparse.add_argument("--Gitlab_Project_Id", "gl", help="Gitlab Project ID")

args = parser.parse_args()
if (args.user):
    gitlab_user_name = args.user
if (args.password):
    gitlab_user_pass = args.password
if (args.Github_Repo_Name):
    github_repo_name = args.Github_Repo_Name
if (args.Gitlab_Project_Id):
    gl_project_id = args.Gitlab_Project_Id
    
# Collecting Username and Password Variables
gitlab_username = gitlab_user_name
gitlab_password = gitlab_user_pass
github_reponame = github_repo_name
gitlab_projectid = gl_project_id

gitlab = requests.session()
gitlab.auth = (gitlab_username, gitlab_password)

gitlabUrl = 'https://gitlab.com/'

print('***** Gitlab Url is *****', gitlabUrl)

repoDirectory = os.environ['WORKSPACE']

print('***** ????? *****', repoDirectory)

print('**** github token is *****', github_token_migration)

def list_repos():
    repos = []
    page = 1
    while True:
        params = {"page": page, "per_page": 10, "bearer_token": github_token_migration}
        url = os.path.join('https://api.github.com/users/Sidbhasin13/repos')
        res = requests.get('url', parms=params, verify=False)
        groups += res.json
        if "x-total-pages" in res.headers:
            if page >= int(res.headers["x-total-pages"]):
                break
            page +=1
        else:
            break
    return repos
    
repository = repos

print("**** Repos ****", repository)

