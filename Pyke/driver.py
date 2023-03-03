import contextlib
import sys

from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)




def bc_test_questions():
    engine.reset()

    engine.activate('rules2')

    print("doing proof")

    try:
        with engine.prove_goal(
                'rules2.the_attacker($pest)') as x:
            for vars, plan in x:
                print("the attacker pest that harm your crops is: %s" % (vars['pest']))
                a=("the attacker pest that harm your crops is: %s" % (vars['pest']))


    except Exception:

        krb_traceback.print_exc()
        sys.exit(1)
    print("doing proof")

    try:
        with engine.prove_goal(
                'rules2.the_product_is($product)') as x:
            for vars, plan in x:
                print("the chemical product that kil this pest is: %s" % (vars['product']))
                b=("the chemical product that kil this pest is: %s" % (vars['product']))

    except Exception:

        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")
    result = [a, b]
    return result
