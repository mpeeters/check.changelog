# encoding: utf-8
"""
check.changelog

Created by mpeeters
Licensed under the GPL license, see LICENCE.txt for more details.
"""

from check.changelog.changes import GitChanges
from check.changelog.changelog import Changelogs
from zest.releaser import choose
from zest.releaser import utils


def main():
    vcs = choose.version_control()
    changelogs = Changelogs(vcs)
    last_tag = utils.get_last_tag(vcs)
    git_command = vcs.cmd_log_since_tag(last_tag)
    changes = GitChanges(utils.system(git_command))
    print 'There are {0} commit(s) for {1} line(s) in changelog'.format(
        len(changes.commits),
        len(changelogs.last_version.logs),
    )
