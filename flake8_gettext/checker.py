from .version import __version__
from ast import walk, Call, Name, Attribute, Str, BinOp

try:
    from ast import JoinedStr
except ImportError:
    JoinedStr = None

GT010 = "GT010 the gettext's argument contains operators or 'format'."
GT012 = "GT012 the gettext's argument is not single string."

class GettextChecker(object):
    name = 'flake8_gettext'
    version = __version__

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        for node in walk(self.tree):
            if not isinstance(node, Call):
                continue
            if not isinstance(node.func, Name):
                continue
            if node.func.id not in ('_', 'gettext', 'ugettext', 'ngettext', 'ungettext'):
                continue
            if len(node.args) == 0:
                continue
            if type(node.args[0]) == BinOp or (isinstance(node.args[0], Call) and isinstance(node.args[0].func, Attribute) and node.args[0].func.attr == 'format'):
                yield node.lineno, node.col_offset, GT010, type(self)
            elif JoinedStr is not None and isinstance(node.args[0], JoinedStr):
                yield node.lineno, node.col_offset, GT011, type(self)
            else:
                if len(node.args) == 1 and isinstance(node.args[0], Str):
                    continue
                yield node.lineno, node.col_offset, GT012, type(self)
