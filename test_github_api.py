from github_api import getRepoNameByUserId, getCommitByRepo, githubApi
import unittest
from unittest.mock import patch

class TestGitHubAPI(unittest.TestCase):
    @patch('github_api.requests.get')
    def test_getRepoNameByUserId(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = '[{"name": "csp"}, {"name": "hellogitworld"}]'
        
        userId = 'richkempinski'
        repoNames = getRepoNameByUserId(userId)
        self.assertEqual(repoNames, ['csp', 'hellogitworld'])

    @patch('github_api.requests.get')
    def test_getCommitByRepo(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = '[{"commit": {"message": "commit message"}}]'
        
        userId = 'richkempinski'
        repoName = 'repo1'
        commitCount = getCommitByRepo(userId, repoName)
        self.assertEqual(commitCount, 1)

    @patch('github_api.getRepoNameByUserId')
    @patch('github_api.getCommitByRepo')
    def test_githubApi(self, mock_getCommitByRepo, mock_getRepoNameByUserId):
        mock_getRepoNameByUserId.return_value = ['csp', 'hellogitworld']
        mock_getCommitByRepo.side_effect = [1, 3] 
        
        userId = 'richkempinski'
        apiInfo = githubApi(userId)
        expected_output = """Repo: csp Number of commits: 1\nRepo: hellogitworld Number of commits: 3"""
        self.assertEqual(apiInfo, expected_output)

if __name__ == '__main__':
    unittest.main()