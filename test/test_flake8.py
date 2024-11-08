from sys import version_info
from pytest import mark
from ast import parse
from flake8_gettext.checker import GettextChecker

def test_positive_1():
    tree = parse('''
import gettext
gettext.textdomain('myapplication')
_ = gettext.gettext
print(_('This is a translatable string %s.') % 'foo')
''')
    violations = list(GettextChecker(tree).run())
    assert len(violations) == 0

def test_positive_2():
    tree = parse('''
from gettext import textdomain, ngettext
textdomain('myapplication')
print(ngettext('This is a translatable string %s.', 'This is a translatable string %s plural.', 1) % 'foo')
''')
    violations = list(GettextChecker(tree).run())
    assert len(violations) == 0

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

@mark.skipif(version_info < (3,6), reason='fstring is not supported')
def test_formatted_string():
    tree = parse('''
import gettext
gettext.textdomain('myapplication')
_ = gettext.gettext
print(_(f'formatted string'))
''')
    violations = list(GettextChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('GT011 ')

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
    assert violations[0][2].startswith('GT012 ')

def test_direct_call_1():
    tree = parse('''
import gettext
gettext.textdomain('myapplication')
print(gettext.ngettext('This is a translatable string %s.' % 'foo'))
''')
    violations = list(GettextChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('GT010 ')

def test_direct_call_2():
    tree = parse('''
from gettext import textdomain, gettext
textdomain('myapplication')
print(gettext('This is a translatable string %s.' % 'foo'))
''')
    violations = list(GettextChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('GT010 ')

def test_emptystring():
    tree = parse('''
import gettext
gettext.textdomain('myapplication')
_ = gettext.gettext
print(_(''))
''')
    violations = list(GettextChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('GT020 ')
