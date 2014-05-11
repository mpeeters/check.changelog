# encoding: utf-8
"""
check.changelog

Created by mpeeters
Licensed under the GPL license, see LICENCE.txt for more details.
"""

import re


class Commit(object):

    def __init__(self, rev, author, date, log):
        self.rev = rev
        self.author = author
        self.date = date
        self.log = log


class Changes(object):
    """Base commit parser"""
    rev = None
    author = None
    date = None
    ignored = None

    def __init__(self, logs):
        self._logs = [l for l in logs.splitlines() if l]
        self.commits = []
        for commit_lines in self.split_commits():
            self.commits.append(self.create_commit(commit_lines))

    def split_commits(self):
        commits_lines = []
        commit = None
        for line in self._logs:
            ignored = False
            if re.search(self.rev, line) is not None:
                if commit is not None:
                    commits_lines.append(commit)
                commit = []
            for ignored_regexp in self.ignored:
                if re.search(ignored_regexp, line) is not None:
                    ignored = True
                    break
            if ignored is not True:
                commit.append(line)
        return commits_lines

    def create_commit(self, lines):
        log = []
        params = {}
        for line in lines:
            is_log = True
            for key in ('rev', 'author', 'date'):
                reg_exp = getattr(self, key)
                if re.search(reg_exp, line) is not None:
                    params[key] = re.sub(reg_exp, '', line).strip()
                    is_log = False
                    continue
            if is_log is True:
                log.append(line.strip())
        return Commit(params['rev'], params['author'], params['date'], log)


class GitChanges(Changes):
    rev = '^commit'
    author = '^Author:'
    date = '^Date:'
    ignored = ('^Merge:', )
