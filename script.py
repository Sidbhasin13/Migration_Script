#!/usr/bin/env python
import os
import re
import subprocess
import requests
import json
import urllib3
import sys
import argparse
from requests.auth import HTTPBasicAuth
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


gitlab_user_name = "Sidbhasin13"
print("***** Arg User *****", gitlab_user_name)

gitlab_user_pass = "gitlab_password"
print("***** Arg Password *****", gitlab_user_pass)

github_repo_name = "Migration_Script"
print("***** Arg GitHub Password *****", github_repo_name)

gl_project_id = "42235831"
print("***** Arg Gitlab Project ID *****", gl_project_id)

print("***** Gitlab Data *****", gitlab_user_name, gitlab_user_pass, github_repo_name, gl_project_id )

# Collecting Username and Password Variables
gitlab_username = gitlab_user_name
gitlab_password = gitlab_user_pass
github_reponame = github_repo_name
gitlab_projectid = gl_project_id

gitlab = requests.Session()
gitlab.auth = (gitlab_username, gitlab_password)

print("____ Gitlab Auth ____", gitlab.auth)

gitlabUrl = 'https://gitlab.com/'

print('***** Gitlab Url is *****', gitlabUrl)

repoDirectory = os.environ['WORKSPACE']

print('***** ????? *****', repoDirectory)

# print('**** github token is *****', github_token_migration)

def list_repos():
    repos = []
    page = 1
#     headers = {'Authorization': 'Bearer Token', 'Cookie': '_octo=GH1.1.784827204.1673029009; logged_in=no'}
    while True:
#         params = {"page": page, "per_page": 10, headers = {'Authorization': 'Bearer Token'}}
#         print("----- Params -----", params)
        url = 'https://api.github.com/users/Sidbhasin13/repos'
        print("---- URL ----", url)
        res = requests.request("GET", url, auth=HTTPBasicAuth('Sidbhasin13', 'Password'), verify=False)
        print("+++++ Response +++++", res)
#         repos += res.json()
        repos.extend(i['full_name'] for i in res.json())
        print(*repos, sep = "\n")
        if "x-total-pages" in res.headers:
            if page >= int(res.headers["x-total-pages"]):
                break
            page +=1
        else:
            break
    return repos
    
repository = list_repos()

print("**** Repos ****", repository)

