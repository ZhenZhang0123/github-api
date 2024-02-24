from github_api import githubApi, getRepoNameByUserId, getCommitByRepo
import pytest

def test_getRepoNameByUserId():
    userId = 'richkempinski'
    repoNames = getRepoNameByUserId(userId)
    assert repoNames == ['csp', 'hellogitworld', 'helloworld', 'Mocks', 'Project1','richkempinski.github.io','threads-of-life','try_nbdev','try_nbdev2']


def test_getCommitByRepo():
    userId = 'richkempinski'
    repoName = 'hellogitworld'
    commitCount = getCommitByRepo(userId, repoName)
    assert commitCount == 30

def test_githubApi():
    userId = 'richkempinski'
    apiInfo = githubApi(userId)
    assert apiInfo == """Repo: csp Number of commits: 2
Repo: hellogitworld Number of commits: 30
Repo: helloworld Number of commits: 6
Repo: Mocks Number of commits: 10
Repo: Project1 Number of commits: 2
Repo: richkempinski.github.io Number of commits: 9
Repo: threads-of-life Number of commits: 1
Repo: try_nbdev Number of commits: 2
Repo: try_nbdev2 Number of commits: 5"""