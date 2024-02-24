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
    assert apiInfo == """Repo: csp Number of commits: 2\n
    Repo: hellogitworld Number of commits: 30\n
    Repo: helloworld Number of commits: 6\n
    Repo: Mocks Number of commits: 10\n
    Repo: Project1 Number of commits: 2\n
    Repo: richkempinski.github.io Number of commits: 9\n
    Repo: threads-of-life Number of commits: 1\n
    Repo: try_nbdev Number of commits: 2\n
    Repo: try_nbdev2 Number of commits: 5"""