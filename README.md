# ar_git_repo
Ansible Role to manage a git repository

## Requirements
- git command line is available (>= 1.8)

## Role Variables
The following details:
- the parameters that should be passed to the role (aka vars)
- the defaults that are held
- the secrets that should generally be sourced from an ansible vault.

### Parameters:
| Variable                   | Description                                                                                                                                 | Default        |
| --------                   | -----------                                                                                                                                 | -------        |
| ar_git_repo_url            | Remote location of the git repository                                                                                                       | null (invalid) |
| ar_git_repo_ssh_key        | Base 64 encoded ssh key to use to access the git repository                                                                                 | '' (invalid)   |
| ar_git_repo_ssh_key_pass   | The passphrase for the ssh key (wip)                                                                                                        | ''             |
| ar_git_repo_commit_comment | A comment to pass though if changes are committed                                                                                           | ''             |
| ar_git_repo_version        | The version of the repository (branch, tag or commit hash note only a branch will be able to have changes committed back to the repository) | 'master'       |
| ar_git_repo_remove_list    | List of files to remove                                                                                                                     | []             |


### Defaults
| Variable                         | Description                                                                                                | Default                                                                |
| --------                         | -----------                                                                                                | -------                                                                |
| ar_git_repo_assertions           | List of assertions made before execution                                                                   | ar_git_repo_url, ar_git_repo_name and ar_git_repo_ssh_key are provided |
| ar_git_repo_gitignore_entries    | List of entries to add to .gitignore                                                                       | usual suspects                                                         |
| ar_git_repo_name                 | Name of the repository                                                                                     | Name given in ar_git_repo_url                                          |
| ar_git_repo_subdir               | A subdirectory on which to operate                                                                         | '.' (i.e. repo root directory)                                         |
| ar_git_repo_ssh_key_path         | Place in which to put the ssh key to enable access to the repo                                             | '~/.ssh/ansible-id_rsa'                                                |
| ar_git_repo_ssh_agent_socket     | Location of ssh-agent socket (wip)                                                                         | '/tmp/ssh/agent.ssh'                                                   |
| ar_git_repo_user                 | User applied to sshconfig to access upstream repo                                                          | 'git'                                                                  |
| ar_git_repo_username             | User used in setting up git global config (i.e. who will be attributed to commits)                         | 'ansible'                                                              |
| ar_git_repo_email                | Email address used in setting up git global config                                                         | 'ansible@here.com'                                                     |
| ar_git_repo_mark_change_on_clone | Define whether the git clone itself should be marked as a change                                           | false                                                                  |
| ar_git_repo_auto_cleanup         | Define whether the git repositories worked on should be removed from the filesystem at the end of the play | true                                                                   |

### Secrets
The following variables should be provided through an encrypted source:
- ar_git_repo_ssh_key
- ar_git_repo_ssh_key_pass

### External variables
The following external variables are defined for use outside of this 
role:

| Variable          | Description                                                   | Default |
| --------          | -----------                                                   | ------- |
| ar_git_repo_paths | Dictionary of git cloned directory locations keyed on git url | {}      |

## Task groups
The following is a list of task files that can be invoked separately:
- main: Invoke 'checkout'
- update: Commit and push any changes (additions or removals) based on the subdirectory provided in 'ar_git_repo_subdir'
- add: Add a specific list of files (independent of 'ar_git_repo_subdir') to upstream repo 
- remove: Remove a specific list of files (independent of 'ar_git_repo_subdir') from upstream repo
- reset: Reset the local filesystem state back to HEAD
- checkin: Commit and push the changes to upstream repository
- checkout: Clone or pull from the git repository

## Dependencies
None

## Example Playbook

```
- hosts: localhost
  tasks:
    - include_role:
        name: ar_git_repo
        tasks_from: checkout
      vars:
        ar_git_repo_url: "git@git-host:group/repo.git"
        ar_git_repo_ssh_key: 'LS0tLS1CRUdJTiBPUEVOU1NIIFBSSVZBVEUgS0VZLS0tLS0KYjNCbGJuTnphQzFyW...'
        ar_git_repo_version: "master"

    ... make changes ... 
     
    - include_role:
        name: ar_git_repo
        tasks_from: update
      vars:
        ar_git_repo_url: "git@git-host:group/repo.git"
        ar_git_repo_ssh_key: 'LS0tLS1CRUdJTiBPUEVOU1NIIFBSSVZBVEUgS0VZLS0tLS0KYjNCbGJuTnphQzFyW...'
        ar_git_repo_commit_comment: "Updates made by automation for ..."
            
```


## License

MIT / BSD

## Author Information

This role was created in 2020 by David Stewart (dstewart@redhat.com)
