from ast import parse
from flake8_gettext.checker import GettextChecker

def test_binop():
    tree = parse('''
import gettext
gettext.textdomain('myapplication')
_ = gettext.gettext
print(_('This is a translatable string %s.' % 'foo'))
''')
    violations = list(GettextChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('GT010 ')

def test_variable():
    tree = parse('''
import gettext
gettext.textdomain('myapplication')
_ = gettext.gettext
x = 'This is a translatable string.'
print(_(x))
''')
    violations = list(GettextChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('GT011 ')

