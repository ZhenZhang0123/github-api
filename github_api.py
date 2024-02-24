import requests
import json

def githubApi(userId):
    if type(userId) != str:
        raise ValueError('Invalid input. Please enter a valid userId.')
    repoNames = getRepoNameByUserId(userId)
    results = []
    if repoNames:    
        for repoName in repoNames:
            commitCount = getCommitByRepo(userId, repoName)
            if commitCount is not None:
                results.append(f"Repo: {repoName} Number of commits: {commitCount}")
            else :
                raise ValueError('Failed to get commit data for repo: ', repoName)
        print('\n'.join(results))
        return '\n'.join(results)
    else:
        print('Failed to get repo data for user: ', userId)
     
def getRepoNameByUserId(userId):
    repoUrl = f"https://api.github.com/users/{userId}/repos"
    repoResponse = requests.get(repoUrl)
    if repoResponse.status_code == 200:
        repoInfo = json.loads(repoResponse.text)
        repoNames = [repo["name"] for repo in repoInfo]
        return repoNames  
    else:
        print('Failed to get repo data:', repoResponse.status_code)
        return None

def getCommitByRepo(userId, repoName):
    commitUrl = f"https://api.github.com/repos/{userId}/{repoName}/commits"
    commitResponse = requests.get(commitUrl)
    if commitResponse.status_code == 200:
        commitInfo = json.loads(commitResponse.text)
        return len(commitInfo)
    else:
        print('Failed to get commit data:', commitResponse.status_code)
        return None