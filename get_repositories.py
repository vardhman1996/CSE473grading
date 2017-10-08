from github3 import GitHub
from git import Repo
import os
import os.path
import glob
import shutil

def copy_files_for_mos(file_paths):
    mos_github_folder = "mos_github_folder"
    mkdir(mos_github_folder)
    for file_path in file_paths:
        github_user = file_path.split("/")[2]
        folder_path = os.path.join(mos_github_folder, "{0}_{1}".format(github_user, "github"))
        mkdir(folder_path)
        shutil.copy2(file_path, folder_path)
    return None


def find_files(folderpath, file_name):
    file_paths = []
    for dirpath, dirnames, filenames in os.walk(folderpath):
        for filename in [f for f in filenames if f.endswith(file_name)]:
            file_paths.append(os.path.join(dirpath, filename))
    return file_paths

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
    return None

def mkdir(foldername):
    if os.path.isdir(foldername):
        return False

    os.makedirs(foldername)
    return True

file_paths = find_files("./gitrepos", "search.py")
copy_files_for_mos(file_paths)