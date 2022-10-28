from .version import __version__
from ast import walk, Call, Name, Attribute, Str, BinOp

try:
    from ast import JoinedStr
except ImportError:
    JoinedStr = None

GT010 = "GT010 the gettext's argument contains operators or 'format'."
GT011 = "GT011 the gettext's argument is a fstring."
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
            if isinstance(node.func, Name) and node.func.id in ('_', 'gettext', 'ugettext', 'ngettext', 'ungettext'):
                pass
            elif isinstance(node.func, Attribute) and isinstance(node.func.value, Name) and node.func.value.id == 'gettext' and node.func.attr in ('_', 'gettext', 'ugettext', 'ngettext', 'ungettext'):
                pass
            else:
                continue
            if len(node.args) == 0:
                continue
            if type(node.args[0]) == BinOp or (isinstance(node.args[0], Call) and isinstance(node.args[0].func, Attribute) and node.args[0].func.attr == 'format'):
                yield node.lineno, node.col_offset, GT010, type(self)
            elif JoinedStr is not None and isinstance(node.args[0], JoinedStr):  # Py3
                yield node.lineno, node.col_offset, GT011, type(self)
            else:
                if len(node.args) == 1 and isinstance(node.args[0], Str):
                    continue
                yield node.lineno, node.col_offset, GT012, type(self)
