import re

def get_hostname(url):
    if url.startswith('https'):
      index=3
    elif url.startswith('git'):
      index = 1
    elif url.startswith('ssh'):
      index=4

    return re.split('[@:/]', url)[index]

def repo_dict(repo_dictionary, repourl, repopath):
    repo_dictionary[repourl] = repopath
    return repo_dictionary

class FilterModule(object):
    '''
    custom jinja2 filters for working with collections
    '''

    def filters(self):
        return {
            'get_hostname': get_hostname,
            'repo_dict': repo_dict
        }

'''
Testing
'''
import unittest


class TestSelectFromArrayOfDicts(unittest.TestCase):
    git_url = "git@git-host.domain:path/gitrepo.git"
    https_url = "https://git-host.domain/path/gitrepo.git"
    ssh_url = "ssh://git@git-host.domain/path/gitrepo.git"

    def test_get_hostname_git(self):
        self.assertEqual('git-host.domain', get_hostname(self.git_url))
        self.assertEqual('git-host.domain', get_hostname(self.https_url))
        self.assertEqual('git-host.domain', get_hostname(self.ssh_url))
