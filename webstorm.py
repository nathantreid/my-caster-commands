from dragonfly import (Grammar, AppContext, MappingRule, RuleRef, RuleWrap,
                       Dictation, IntegerRef, Key, Text, Function,
                       Alternative, Choice, Literal, CompoundRule, Repetition, Compound)

from caster.lib import control
from caster.lib import settings
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge import gfilter
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R

import pystache
import _dragonfly_utils as utils
import _text_format as textFormat

from inspect           import getargspec

def formatCode():
    Key("ca-l").execute()


print("reload webstorm")
class WebStormRule(MergeRule):
    pronunciation = "web storm"

    mapping = {
        "ed dupe":                    R(Key("c-d"), rdescript="WebStorm: Duplicate"),
        "ed aut":                     R(Key("cs-enter"), rdescript="WebStorm: Auto Complete"),
        "ed form":                    R(Function(formatCode), rdescript="WebStorm: Format Code"),
        "ed par":                     R(Key("c-p"), rdescript="WebStorm: Show Parameters"),
        "ed doc":                     R(Key("c-q"), rdescript="WebStorm: Show Documentation"),
        "ed tab":                     R(Key("a-right"), rdescript="WebStorm: Next Tab"),
        "ed tack":                    R(Key("a-left"), rdescript="WebStorm: Previous Tab"),

        "ed deck":                    R(Key("c-b"), rdescript="WebStorm: Go To Declaration"),
        "ed source":                  R(Key("f4"), rdescript="WebStorm: Go To Source"),

        "ed search":                  R(Key("shift, shift"), rdescript="WebStorm: Search Everywhere"),
        "ed file":                    R(Key("cs-n"), rdescript="WebStorm: Navigate To File"),
        "ed find":                    R(Key("cs-f"), rdescript="WebStorm: Find In Path"),
        "ed line <n>":                R(Key("c-g/50") + Text("%(n)s") + Key("enter"), rdescript="WebStorm: Go To Line"),

        "ed com":                     R(Key("c-slash"), rdescript="WebStorm: Comment Line"),
        "ed block com":               R(Key("cs-slash"), rdescript="WebStorm: Comment Block"),
        "ed sell ex":                 R(Key("c-w"), rdescript="WebStorm: Expand Selection"),
        "ed sell con":                R(Key("cs-w"), rdescript="WebStorm: Shrink (Contract) Selection"),
        
        "ed tog term":                R(Key("a-f12"), rdescript="WebStorm: Toggle Terminal"),
        "ed tog proj":                R(Key("a-1"), rdescript="WebStorm: Toggle Project"),
        
        "ed debug":                   R(Key("s-f9"), rdescript="WebStorm: Debug"),
        "ed run":                     R(Key("s-f10"), rdescript="WebStorm: Run"),
        
        "ed undo":                   R(Key("c-z"), rdescript="WebStorm: Undo"),
        "ed redo":                   R(Key("cs-z"), rdescript="WebStorm: Redo"),
        
        "ed cape":                   R(Key("escape"), rdescript="WebStorm: Escape"),

        #"function <name> [par <param1>] [type <type1> []] [par <param2>] [par <param3>] [par <param4>]": R(Function(genFunction), rdescript="Javascript: Function G"),

        # "duplicate":                R(Key("c-d"), rdescript="WebStorm: Duplicate"),
        # "auto complete":            R(Key("cs-enter"), rdescript="WebStorm: Auto Complete"),
        # "format code":              R(Key("ca-l"), rdescript="WebStorm: Format Code"),
        # "show doc":                 R(Key("c-q"), rdescript="WebStorm: Show Documentation"),
        # "show param":               R(Key("c-p"), rdescript="WebStorm: Show Parameters"),
        # "Jen method":               R(Key("a-insert"), rdescript="WebStorm: Generated Method"),
        # "jump to source":           R(Key("f4"), rdescript="WebStorm: Jump To Source"),
        # "delete line":              R(Key("c-y"), rdescript="WebStorm: Delete Line"),
        # "search symbol":            R(Key("cas-n"), rdescript="WebStorm: Search Symbol"),
        # "debug":                    R(Key("s-f9"), rdescript="WebStorm: Debug"),
        # "run":                      R(Key("s-f10"), rdescript="WebStorm: Run"),
        # "next tab":                 R(Key("a-right"), rdescript="WebStorm: Next Tab"),
        # "prior tab":                R(Key("a-left"), rdescript="WebStorm: Previous Tab"),

        # "comment line":             R(Key("c-slash"), rdescript="WebStorm: Comment Line"),
        # "comment block":            R(Key("cs-slash"), rdescript="WebStorm: Uncomment Line"),
        # "select ex":                R(Key("c-w"), rdescript="WebStorm: untitled command"),
        # "select ex down":           R(Key("cs-w"), rdescript="WebStorm: entitled command"),
        # "search everywhere":        R(Key("shift, shift"), rdescript="WebStorm: Search Everywhere"),
        # "find in path":             R(Key("cs-f"), rdescript="WebStorm: Find In Path"),
        # "go to line":               R(Key("c-g"), rdescript="WebStorm: Go To Line"),

        # "toggle terminal":          R(Key("a-f12"), rdescript="WebStorm: Toggle Terminal"),
        # "toggle project":           R(Key("a-1"), rdescript="WebStorm: Toggle Project"),
        }
    extras = [
              Dictation("text"),
              IntegerRefST("n", 1, 1000),

             ]
    defaults = {"n": 1,}

# ---------------------------------------------------------------------------


context = AppContext(executable="WebStorm", title="WebStorm") \
          | AppContext(executable="WebStorm64", title="WebStorm")
grammar = Grammar("WebStorm", context=context)
# if settings.SETTINGS["apps"]["webstorm"]:
if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
    control.nexus().merger.add_global_rule(WebStormRule())
else:
    rule = WebStormRule(name="web storm")
    gfilter.run_on(rule)
    grammar.add_rule(rule)
    grammar.load()


# class TypeRule(Compound):
#   spec = "<type> [or]"
#   extras = [
#       Choice(
#         name = "type",
#         choices = {
#           "string": "string",
#           "number": "number",
#           "object": "object",
#           "boolean": "boolean",
#           "void": "void",
#           "null": "null",
#           "undefined": "undefined",
#           "any": "any",
#           "Date": "Date",
#         }),
#   ]
#
#
# class TypesRule(Compound):
#   spec = "<types>"
#   extras = [
#     Repetition(
#       name = "types",
#       child = TypeRule,
#       max = 8)
#   ]
#
#   def _process_recognition(self, node, extras):
#     print ("types", extras["types"])
#     types = extras["types"]
#     extras["types"] = ' | '.join(types)
#
#
# class FunctionParamRule(Compound):
#   spec = "par <param> [types]"
#   extras = [
#     Dictation("param"),
#     TypesRule("types"),
#
#   ]
#
#
# class WebStormFunctionRule(CompoundRule):
#     spec = "function <name> [parameters] [par <param1>] [type <type1> []] [par <param2>] [par <param3>] [par <param4>]",
#     extras = [
#                 Repetition(
#                     name="parameters",
#                     child=FunctionParamRule())
#                     # CompoundRule(
#                     #   spec = "par <param> [types]",
#                     #   extras = [
#                     #     Dictation("param"),
#                     #     TypesRule("types"),
#                     #   ]))
#              ]
#
#     def _process_recognition(self, node, extras):
#         params = extras["parameters"]
#         print ("extras" , extras)
#         print ("params ", params)

# class WebStormFunctionRules(CompoundRule):
#     spec = "function <name> [parameters]",
#     extras = [
#                 Repetition(
#                     name="parameters",
#                     child=FunctionParamRule())
#                     # CompoundRule(
#                     #   spec = "par <param> [types]",
#                     #   extras = [
#                     #     Dictation("param"),
#                     #     TypesRule("types"),
#                     #   ]))
#              ]
#
#     def _process_recognition(self, node, extras):
#         params = extras["parameters"]
#         print ("extras" , extras)
#         print ("params ", params)


# def genFunction(name, param1=None, param2=None, param3=None):
#     parameters = ', '.join(map(lambda val: val.format(), filter(None, [param1, param2, param3])))
#     print("par ", parameters)
#     template = 'function {{name}}({{parameters}}) {' # no ending bracket necessary, WebStorm automatically adds it
#     Text(pystache.render(template, {'name': name, 'parameters': parameters})).execute()
#     Key('enter').execute()
#     formatCode()

def writeFunction(name):
    template = 'function {name}() {{' # no ending bracket necessary, WebStorm automatically adds it
    Text(template.format(name=name)).execute()
    Key('enter').execute()
    formatCode()
    Key('a-up,end,left:3').execute()

def writeParam(name):
    Text('{name},'.format(name=name)).execute()
    formatCode()

def deleteBlock():
    Key('c-minus,c-y').execute()

def findText(text):
    Key('c-f/25').execute()
    Text(text).execute()

formatted_dictation = utils.create_rule(
    "FormatRule",
    {
        "camel <dictation>": Function(textFormat.format_camel),
    },
    {"dictation": Dictation()}
)

dictation_rule = utils.create_rule(
    "DictationRule",
    {
        "<text>": Text("%(text)s"),
    },
    {
        "text": Dictation()
    }
)
dictation_element = RuleWrap(None, Alternative([
    RuleRef(rule=dictation_rule),
]))


class FuncChoice(Alternative):

    def __init__(self, name, choices, extras=None, default=None):

        # Argument type checking.
        assert isinstance(name, basestring) or name is None
        assert isinstance(choices, dict)
        for k, v in choices.iteritems():
            assert isinstance(k, basestring)

        # Construct children from the given choice keys and values.
        self._choices = choices
        self._extras = extras
        children = []
        for k, v in choices.iteritems():
            if callable(v):
                child = Compound(spec=k, value_func=v, extras=extras)
            else:
                child = Compound(spec=k, value=v, extras=extras)
            children.append(child)

        # Initialize super class.
        Alternative.__init__(self, children=children,
                                       name=name, default=default)


def echo(node, extras):
    print("-------------- node ----------------")
    print(node)
    print("-------------- extras ----------------")
    print(extras)
    print(extras['name'].format())
    return 'echo!!' + unicode(extras['name'])


def FuncWrap(node, extras):
    return echo(extras.name)


def echo2(name):
    return '{name}'.format(name=name)


def FuncWrap1(node, extras):
    return echo2(**extras)


def F(func):
    (args, varargs, varkw, defaults) = getargspec(func)
    if varkw:
        _filter_keywords = False
    else:
        _filter_keywords = True
    _valid_keywords = set(args)

    def wrapFunc(node, extras):
        if _filter_keywords:
            invalid_keywords = set(extras.keys()) - _valid_keywords
            for key in invalid_keywords:
                del extras[key]
        return func(**extras)
    return wrapFunc


def FA(func):
    def wrapFunc(node, extras):
        return func(*extras)
    return wrapFunc


class WebStormFunctionRules(MergeRule):
    pronunciation = "web storm custom"

    mapping = {
        "function [<name>]": R(Function(writeFunction), rdescript="WebStorm: Generate Function"),
        "par <name>": R(Function(writeParam), rdescript="WebStorm: Write Function Param"),
        "delete block": R(Function(deleteBlock), rdescript="WebStorm: Delete Block"),
        "go to params": R(Function(findText, text="params")),
        "go to function params": R(Function(findText, text = "params")),
        "go to arrow params": R(Function(findText, text = "params")),
    }
    extras = [
        FuncChoice(name="name", choices={
            "<name>": Text("%(name)s"),
            "cat <dictation>": F(textFormat.format_camel),
            "dog <name>": echo,
            "mouse <name>": FuncWrap1,
            "bird <name>": F(echo2),
            "test": "yo",
        }, extras=[
           Dictation("name"),
           Dictation("dictation"),
        ]),
    ]
    defaults = {"n": 1, }


# navigate to function parameters from inside function:
# alt + up
# end
# left (3)



grammar = Grammar("WebStorm Function", context=context)
rule = WebStormFunctionRules(name="web storm function")
gfilter.run_on(rule)
grammar.add_rule(rule)
grammar.load()
