from github3 import GitHub
from git import Repo
import os

def clone_repositories():
	gh = GitHub()
	folderpath = "gitrepos"
	repos = gh.search_repositories("cs188 language:python")
	repo_count = 50
	for r in repos:
		if repo_count == 0: break
		repo_json = r.to_json()
		repo_path = os.path.join(folderpath, repo_json["full_name"])
		if not mkdir(repo_path): continue
		Repo.clone_from(repo_json["clone_url"], repo_path)
		repo_count-=1



def mkdir(foldername):
	if os.path.isdir(foldername):
		return False

	os.makedirs(foldername)
	return True

