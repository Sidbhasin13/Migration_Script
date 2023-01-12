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
# github_token_migration = 'Bearer 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'

# ArgParser Section
# parser = argparse.ArgumentParser()
# parser.add_argument("--user", "-u1", help="User Name")
# parser.add_argument("--password", "-p1", help="Password")
# parser.add_argument("--Github_Repo_Name", "-gb", help="Github Repository Name")
# parser.add_argument("--Gitlab_Project_Id", "-gl", help="Gitlab Project ID")
# args = parser.parse_args()


# if args.user:
#     gitlab_user_name = args.user
# if args.password:
#     gitlab_user_pass = args.password
# if args.Github_Repo_Name:
#     github_repo_name = args.Github_Repo_Name
# if args.Gitlab_Project_Id:
#     gl_project_id = args.Gitlab_Project_Id



gitlab_user_name = "Sidbhasin13"
print("***** Arg User *****", gitlab_user_name)

gitlab_user_pass = "Sidbhasinnewdelhi@0786"
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
#     headers = {'Authorization': 'Bearer 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', 'Cookie': '_octo=GH1.1.784827204.1673029009; logged_in=no'}
    while True:
#         params = {"page": page, "per_page": 10, headers = {'Authorization': 'Bearer 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'}}
#         print("----- Params -----", params)
        url = 'https://api.github.com/users/Sidbhasin13/repos'
        print("---- URL ----", url)
        res = requests.request("GET", url, auth=HTTPBasicAuth('Sidbhasin13', '@$ID&bHA786'), verify=False)
        print("+++++ Response +++++", res)
        repos += res.json()
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

