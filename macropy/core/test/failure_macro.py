from macropy.core.failure import MacroExpansionError
from macropy.core.macros import *

macros = Macros()

@macros.expr
def f(tree, gen_sym, **kw):
    raise Exception("i am a cow")

@macros.expr
def g(tree, gen_sym, **kw):
    assert False, "i am a cow"

@macros.block
def h(tree, gen_sym, **kw):
    raise Exception("i am a cow")

@macros.decorator
def i(tree, gen_sym, **kw):
    raise Exception("i am a cow")