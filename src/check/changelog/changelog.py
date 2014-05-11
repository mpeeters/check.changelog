# encoding: utf-8
"""
check.changelog

Created by mpeeters
Licensed under the GPL license, see LICENCE.txt for more details.
"""

from datetime import datetime
from distutils.version import StrictVersion
from docutils import io
from docutils import readers
from docutils.frontend import OptionParser


class Changelogs(object):

    def __init__(self, vcs):
        self.vcs = vcs
        self._read_changelog()
        self.versions = [VersionChangelog(v) for v in self.root.children[1:]]

    def _read_changelog(self):
        source = io.FileInput(source_path=self.vcs.history_file())
        reader_class = readers.get_reader_class('standalone')
        rst_reader = reader_class(None, 'restructuredtext')
        settings = OptionParser(components=(rst_reader.parser, )).parse_args()
        self.document = rst_reader.read(source, rst_reader.parser, settings)

    @property
    def root(self):
        if self.is_version(self.document.children[0]) is True:
            return self.document
        return self.document.children[0]

    def is_version(self, node):
        try:
            StrictVersion(node.children[0].rawsource.split()[0])
            return True
        except ValueError:
            return False

    @property
    def last_version(self):
        return self.versions[0]


class VersionChangelog(object):

    def __init__(self, node):
        self.node = node

    @property
    def title_node(self):
        return self.node.children[0]

    @property
    def version(self):
        return self.title_node.rawsource.split()[0]

    @property
    def date(self):
        date = self.title_node.rawsource.split()[1][1:-1]
        if date == u'unreleased':
            return
        return datetime.strptime(date, '%Y-%m-%d')

    @property
    def logs_nodes(self):
        return self.node.children[1].children

    @property
    def logs(self):
        return [l.rawsource for l in self.logs_nodes]
