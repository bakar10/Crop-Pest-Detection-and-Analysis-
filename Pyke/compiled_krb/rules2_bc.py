# rules2_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def aphis_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.aphis_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,2,3,4,5,6):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Drosophila_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Drosophila_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,10,12,13,14,15,16,17):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Seed_weevil_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Seed_weevil_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (11,12,18,19,20,21,22,23):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Tree_borers_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Tree_borers_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,10,12,13,14,15,16,17):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Eriosoma_lanigerum_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Eriosoma_lanigerum_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (10,13,24,25,26):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Zeuzera_pyrina_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Zeuzera_pyrina_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,10,12,13,14,15,16,17):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Synanthedon_Myopaeformis_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Synanthedon_Myopaeformis_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,10,12,13,14,15,16,17):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def mites_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.mites_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,10,12,13,14,15,16,17,38):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Ladybug_larva_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Ladybug_larva_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (6,10,27,28,29,30,31):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Tow_Spotted_pider_Mite_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Tow_Spotted_pider_Mite_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (3,5,6,8,10,32,33):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Worm_rash_spider_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Worm_rash_spider_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,4,5,10,11,13,19,25,34,35,36,44):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Bark_beetles_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Bark_beetles_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,4,10,11,13,14,19,25,28,46):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Chlorophorus_Varius_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Chlorophorus_Varius_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (15,25):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Macrotoma_Palmata_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Macrotoma_Palmata_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,10,12,13,15,16,17,25,30,40,41,47):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Anarsia_Lineatella_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Anarsia_Lineatella_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (15,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Russellaspus_Pustulans_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Russellaspus_Pustulans_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (10,12,13,15,16,17,44):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Chrysomphalus_ficus_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Chrysomphalus_ficus_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,40,42,46):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Ostrinia_nubilalis_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Ostrinia_nubilalis_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,7,8,9,11):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Root_Ball_Pests_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Root_Ball_Pests_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,12,38,43,44,45,48):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Wireworms_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Wireworms_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (7,8,11,49,50,51,52,53,54,55,56,57,58,59,61):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Khapra_beetle_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Khapra_beetle_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (7,9,18,20,23,31,36,47,55,62,63,64,65,66,67,68):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def aphid_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.aphid_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (4,6,8,11,13,14,15,21,32,36,41,49,56,57,69,70,71,72,73,74,75,76,77,78,79,80):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Armyworm_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Armyworm_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,4,7,13,15,18,19,20,28,31,44,53,54,62,63,64,66,81,82,83,84,85,86,87):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Bean_fly_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Bean_fly_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (11,50,52,53,56,57,61,88):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def bean_pod_borer_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.bean_pod_borer_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (11,23,31,88):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Black_field_earwig_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Black_field_earwig_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (56,73,74,89,90,91,92):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Brown_bean_bug_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Brown_bean_bug_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (11,23,31,55,88):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Brown_shield_bug_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Brown_shield_bug_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (4,15,19,85):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Cluster_caterpillar_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Cluster_caterpillar_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (4,5,18,19,28,56,60,61,85,80):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Cutworms_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Cutworms_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,4,5,7,11,28,49,50,51,52,53,55,56):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Spotted_winged_drosophila_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Spotted_winged_drosophila_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (10,13,14,25,41,76,87,91):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Exotic_fruit_flies_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Exotic_fruit_flies_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (4,5,10,12,13,14,25,40,70,76,89,91,93):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Karnal_bunt_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Karnal_bunt_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (20,94,95):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Spongy_moths_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Spongy_moths_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (43,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Hessian_flies_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Hessian_flies_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (20,62,64):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Formosan_subterranean_termite_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Formosan_subterranean_termite_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (76,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Exotic_longhorn_beetles_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Exotic_longhorn_beetles_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (10,13,67,68):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Grape_phylloxera_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Grape_phylloxera_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (7,9,18,84):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Etiella_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Etiella_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (11,31,66,88):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Green_vegetable_bug_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Green_vegetable_bug_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (11,19,31,57,60):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Greenhouse_whitefly_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Greenhouse_whitefly_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (9,19,88):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Green_stink_bug_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Green_stink_bug_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (11,19,31,57):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Helicoverpa_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Helicoverpa_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (11,19,31,57,58,66,96,97):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Leaf_beetles_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Leaf_beetles_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (9,11,19,31,60,66,84):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Cotton_leafhopper_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Cotton_leafhopper_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (19,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Vegetable_leafhopper_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Vegetable_leafhopper_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (19,66,97):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Lucerne_leafhopper_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Lucerne_leafhopper_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (31,55,66):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Spotted_leafhopper_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Spotted_leafhopper_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (11,31,97):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Maize_leafhopper_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Maize_leafhopper_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (9,11,60):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Brown_leafhopper_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Brown_leafhopper_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (4,11,19,31,66,96):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Loopers_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Loopers_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (11,19,23,31,57,99):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Lucerne_crownborer_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Lucerne_crownborer_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (31,97):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Mealybug_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Mealybug_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (11,19,57,66,98):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Mirids_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Mirids_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (11,19,31,57,66,82,97,106):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Podsucking_bugs_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Podsucking_bugs_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (9,20,57,58,88,104):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Scarabs_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Scarabs_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (57,60,66,103):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Sorghum_midge_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Sorghum_midge_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (9,105):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Silverleaf_whitefly_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Silverleaf_whitefly_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (19,31,66,102):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Symphyla_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Symphyla_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (6,101):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Maize_thrips_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Maize_thrips_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (11,19,20,60):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Western_flower_thrips_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_Crops_get_Attacked', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Western_flower_thrips_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (11,19,57,58,66,100):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def insecticidal_soaps_and_oils_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.insecticidal_soaps_and_oils_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,22):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def INSECTICIDES_WITH_PYRETHRIN_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.INSECTICIDES_WITH_PYRETHRIN_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,21,23):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Azadirachtin_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Azadirachtin_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,22):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def systemic_insecticide_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.systemic_insecticide_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,22,24,16,17,18,19,20,21,37,39,52,56,58,60):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def MALATHION_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.MALATHION_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,22,15):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Insect_growth_regulators_IGRs_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Insect_growth_regulators_IGRs_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,14):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Spinosad_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Spinosad_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,13):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def chlorantraniliprole_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.chlorantraniliprole_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,12):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def pyrethroid_insecticides_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.pyrethroid_insecticides_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (3,11):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def contact_insecticides_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.contact_insecticides_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (20,10):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Methyl_bromide_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Methyl_bromide_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (21,9):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Nimbecidine_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Nimbecidine_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (23,8):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def pesticides_containing_imidacloprid_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.pesticides_containing_imidacloprid_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (24,30,41,7):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def pesticide_Virtako_40WG_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.pesticide_Virtako_40WG_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (25,6):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Eradicate_Sesbania_spp_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Eradicate_Sesbania_spp_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (25,5):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Insecticide_seed_dressings_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Insecticide_seed_dressings_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (26,4):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def insecticidal_soap_sprays_containing_fatty_acids_and_mineral_salts_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.insecticidal_soap_sprays_containing_fatty_acids_and_mineral_salts_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (27,28,40,3):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Dipel_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Dipel_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (29,43,51):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def NPV_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.NPV_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (43,57):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Pupae_bustin_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Pupae_bustin_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (29,43):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Use_Bifen_IT_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Use_Bifen_IT_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (30,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Bifen_LP_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Bifen_LP_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (30,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Cyonara_Lawn_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Cyonara_Lawn_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (30,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Garden_Insect_Control_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Garden_Insect_Control_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (30,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Quali_Pro_1_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Quali_Pro_1_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (30,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def spinosyns_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.spinosyns_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (31,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def pyrethroids1_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.pyrethroids1_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (31,42):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def carbamates_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.carbamates_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (31,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Spinosad_GF_120_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Spinosad_GF_120_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (32,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Proteus_170_O_TEQ_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Proteus_170_O_TEQ_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (32,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Propiconazole_Tilt_25_EC_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Propiconazole_Tilt_25_EC_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (33,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Insecticide_products_with_emamectin_benzoate_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Insecticide_products_with_emamectin_benzoate_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (34,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Bacillus_thuringiensis_kurtaki_Btk_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Bacillus_thuringiensis_kurtaki_Btk_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (35,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Liquid_termiticide_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Liquid_termiticide_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (36,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_chemical_control_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.no_chemical_control_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (38,59,62):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def horticultural_oils_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.horticultural_oils_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (41,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Beuvaria_bassiana_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Beuvaria_bassiana_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (41,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def organophosphates_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.organophosphates_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (42,31):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def pesticides_containing_esfenvalerate_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.pesticides_containing_esfenvalerate_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (44,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def pesticides_containing_permethrin_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.pesticides_containing_permethrin_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (44,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Asana_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Asana_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (44,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Baythroid_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Baythroid_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (44,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Brigade_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Brigade_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (44,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Karate_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Karate_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (44,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Prolex_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Prolex_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (44,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Sevin_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Sevin_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (44,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Acetamiprid_Gazelle_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Acetamiprid_Gazelle_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (45,46,47,48,49,50):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def propyzamide_herbicide_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.propyzamide_herbicide_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (52,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def carbetamide_herbicide_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.carbetamide_herbicide_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (52,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Dimethoate_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Dimethoate_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (18,53,55):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Methomyl_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Methomyl_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (53,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Buprofezin_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Buprofezin_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (53,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Bifenazate_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Bifenazate_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (54,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Deltamethrin_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Deltamethrin_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (54,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Fluvalinate_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Fluvalinate_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (54,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Organophosphate_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Organophosphate_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (58,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def Short_residual_contact_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.Short_residual_contact_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (58,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def malathion_is_theanswer(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('q', 'what_chemical_product_kill_thepest', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "rules2.malathion_is_theanswer: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (61,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('rules2')
  
  bc_rule.bc_rule('aphis_is_theanswer', This_rule_base, 'the_attacker',
                  aphis_is_theanswer, None,
                  (pattern.pattern_literal('aphis'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Drosophila_is_theanswer', This_rule_base, 'the_attacker',
                  Drosophila_is_theanswer, None,
                  (pattern.pattern_literal('Drosophila'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Seed_weevil_is_theanswer', This_rule_base, 'the_attacker',
                  Seed_weevil_is_theanswer, None,
                  (pattern.pattern_literal('Seed_weevil'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Tree_borers_is_theanswer', This_rule_base, 'the_attacker',
                  Tree_borers_is_theanswer, None,
                  (pattern.pattern_literal('Tree_borers'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Eriosoma_lanigerum_is_theanswer', This_rule_base, 'the_attacker',
                  Eriosoma_lanigerum_is_theanswer, None,
                  (pattern.pattern_literal('Eriosoma_lanigerum'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Zeuzera_pyrina_is_theanswer', This_rule_base, 'the_attacker',
                  Zeuzera_pyrina_is_theanswer, None,
                  (pattern.pattern_literal('Zeuzera_pyrina'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Synanthedon_Myopaeformis_is_theanswer', This_rule_base, 'the_attacker',
                  Synanthedon_Myopaeformis_is_theanswer, None,
                  (pattern.pattern_literal('Synanthedon_Myopaeformis'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('mites_is_theanswer', This_rule_base, 'the_attacker',
                  mites_is_theanswer, None,
                  (pattern.pattern_literal('mites'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Ladybug_larva_is_theanswer', This_rule_base, 'the_attacker',
                  Ladybug_larva_is_theanswer, None,
                  (pattern.pattern_literal('Ladybug_larva'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Tow_Spotted_pider_Mite_is_theanswer', This_rule_base, 'the_attacker',
                  Tow_Spotted_pider_Mite_is_theanswer, None,
                  (pattern.pattern_literal('Tow_Spotted_pider_Mite'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Worm_rash_spider_is_theanswer', This_rule_base, 'the_attacker',
                  Worm_rash_spider_is_theanswer, None,
                  (pattern.pattern_literal('Worm_rash_spider'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Bark_beetles_is_theanswer', This_rule_base, 'the_attacker',
                  Bark_beetles_is_theanswer, None,
                  (pattern.pattern_literal('Bark_beetles'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Chlorophorus_Varius_is_theanswer', This_rule_base, 'the_attacker',
                  Chlorophorus_Varius_is_theanswer, None,
                  (pattern.pattern_literal('Chlorophorus_Varius'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Macrotoma_Palmata_is_theanswer', This_rule_base, 'the_attacker',
                  Macrotoma_Palmata_is_theanswer, None,
                  (pattern.pattern_literal('Macrotoma_Palmata'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Anarsia_Lineatella_is_theanswer', This_rule_base, 'the_attacker',
                  Anarsia_Lineatella_is_theanswer, None,
                  (pattern.pattern_literal('Anarsia_Lineatella'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Russellaspus_Pustulans_is_theanswer', This_rule_base, 'the_attacker',
                  Russellaspus_Pustulans_is_theanswer, None,
                  (pattern.pattern_literal('Russellaspus_Pustulans'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Chrysomphalus_ficus_is_theanswer', This_rule_base, 'the_attacker',
                  Chrysomphalus_ficus_is_theanswer, None,
                  (pattern.pattern_literal('Chrysomphalus_ficus'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Ostrinia_nubilalis_is_theanswer', This_rule_base, 'the_attacker',
                  Ostrinia_nubilalis_is_theanswer, None,
                  (pattern.pattern_literal('Ostrinia_nubilalis'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Root_Ball_Pests_is_theanswer', This_rule_base, 'the_attacker',
                  Root_Ball_Pests_is_theanswer, None,
                  (pattern.pattern_literal('Root_Ball_Pests'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Wireworms_is_theanswer', This_rule_base, 'the_attacker',
                  Wireworms_is_theanswer, None,
                  (pattern.pattern_literal('Wireworms'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Khapra_beetle_is_theanswer', This_rule_base, 'the_attacker',
                  Khapra_beetle_is_theanswer, None,
                  (pattern.pattern_literal('Khapra_beetle'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('aphid_is_theanswer', This_rule_base, 'the_attacker',
                  aphid_is_theanswer, None,
                  (pattern.pattern_literal('aphid'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Armyworm_is_theanswer', This_rule_base, 'the_attacker',
                  Armyworm_is_theanswer, None,
                  (pattern.pattern_literal('Armyworm'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Bean_fly_is_theanswer', This_rule_base, 'the_attacker',
                  Bean_fly_is_theanswer, None,
                  (pattern.pattern_literal('Bean_fly'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('bean_pod_borer_is_theanswer', This_rule_base, 'the_attacker',
                  bean_pod_borer_is_theanswer, None,
                  (pattern.pattern_literal('bean_pod_borer'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Black_field_earwig_is_theanswer', This_rule_base, 'the_attacker',
                  Black_field_earwig_is_theanswer, None,
                  (pattern.pattern_literal('Black_field_earwig'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Brown_bean_bug_is_theanswer', This_rule_base, 'the_attacker',
                  Brown_bean_bug_is_theanswer, None,
                  (pattern.pattern_literal('Brown_bean_bug'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Brown_shield_bug_is_theanswer', This_rule_base, 'the_attacker',
                  Brown_shield_bug_is_theanswer, None,
                  (pattern.pattern_literal('Brown_shield_bug'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Cluster_caterpillar_is_theanswer', This_rule_base, 'the_attacker',
                  Cluster_caterpillar_is_theanswer, None,
                  (pattern.pattern_literal('Cluster_caterpillar'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Cutworms_is_theanswer', This_rule_base, 'the_attacker',
                  Cutworms_is_theanswer, None,
                  (pattern.pattern_literal('Cutworms'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Spotted_winged_drosophila_is_theanswer', This_rule_base, 'the_attacker',
                  Spotted_winged_drosophila_is_theanswer, None,
                  (pattern.pattern_literal('Spotted_winged_drosophila'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Exotic_fruit_flies_is_theanswer', This_rule_base, 'the_attacker',
                  Exotic_fruit_flies_is_theanswer, None,
                  (pattern.pattern_literal('Exotic_fruit_flies'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Karnal_bunt_is_theanswer', This_rule_base, 'the_attacker',
                  Karnal_bunt_is_theanswer, None,
                  (pattern.pattern_literal('Karnal_bunt'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Spongy_moths_is_theanswer', This_rule_base, 'the_attacker',
                  Spongy_moths_is_theanswer, None,
                  (pattern.pattern_literal('Spongy_moths'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Hessian_flies_is_theanswer', This_rule_base, 'the_attacker',
                  Hessian_flies_is_theanswer, None,
                  (pattern.pattern_literal('Hessian_flies'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Formosan_subterranean_termite_is_theanswer', This_rule_base, 'the_attacker',
                  Formosan_subterranean_termite_is_theanswer, None,
                  (pattern.pattern_literal('Formosan_subterranean_termite'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Exotic_longhorn_beetles_is_theanswer', This_rule_base, 'the_attacker',
                  Exotic_longhorn_beetles_is_theanswer, None,
                  (pattern.pattern_literal('Exotic_longhorn_beetles'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Grape_phylloxera_is_theanswer', This_rule_base, 'the_attacker',
                  Grape_phylloxera_is_theanswer, None,
                  (pattern.pattern_literal('Grape_phylloxera'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Etiella_is_theanswer', This_rule_base, 'the_attacker',
                  Etiella_is_theanswer, None,
                  (pattern.pattern_literal('Etiella'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Green_vegetable_bug_is_theanswer', This_rule_base, 'the_attacker',
                  Green_vegetable_bug_is_theanswer, None,
                  (pattern.pattern_literal('Green_vegetable_bug'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Greenhouse_whitefly_is_theanswer', This_rule_base, 'the_attacker',
                  Greenhouse_whitefly_is_theanswer, None,
                  (pattern.pattern_literal('Greenhouse_whitefly'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Green_stink_bug_is_theanswer', This_rule_base, 'the_attacker',
                  Green_stink_bug_is_theanswer, None,
                  (pattern.pattern_literal('Green_stink_bug'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Helicoverpa_is_theanswer', This_rule_base, 'the_attacker',
                  Helicoverpa_is_theanswer, None,
                  (pattern.pattern_literal('Helicoverpa'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Leaf_beetles_is_theanswer', This_rule_base, 'the_attacker',
                  Leaf_beetles_is_theanswer, None,
                  (pattern.pattern_literal('Leaf_beetles'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Cotton_leafhopper_is_theanswer', This_rule_base, 'the_attacker',
                  Cotton_leafhopper_is_theanswer, None,
                  (pattern.pattern_literal('Cotton_leafhopper'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Vegetable_leafhopper_is_theanswer', This_rule_base, 'the_attacker',
                  Vegetable_leafhopper_is_theanswer, None,
                  (pattern.pattern_literal('Vegetable_leafhopper'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Lucerne_leafhopper_is_theanswer', This_rule_base, 'the_attacker',
                  Lucerne_leafhopper_is_theanswer, None,
                  (pattern.pattern_literal('Lucerne_leafhopper'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Spotted_leafhopper_is_theanswer', This_rule_base, 'the_attacker',
                  Spotted_leafhopper_is_theanswer, None,
                  (pattern.pattern_literal('Spotted_leafhopper'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Maize_leafhopper_is_theanswer', This_rule_base, 'the_attacker',
                  Maize_leafhopper_is_theanswer, None,
                  (pattern.pattern_literal('Maize_leafhopper'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Brown_leafhopper_is_theanswer', This_rule_base, 'the_attacker',
                  Brown_leafhopper_is_theanswer, None,
                  (pattern.pattern_literal('Brown_leafhopper'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Loopers_is_theanswer', This_rule_base, 'the_attacker',
                  Loopers_is_theanswer, None,
                  (pattern.pattern_literal('Loopers'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Lucerne_crownborer_is_theanswer', This_rule_base, 'the_attacker',
                  Lucerne_crownborer_is_theanswer, None,
                  (pattern.pattern_literal('Lucerne_crownborer'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Mealybug_is_theanswer', This_rule_base, 'the_attacker',
                  Mealybug_is_theanswer, None,
                  (pattern.pattern_literal('Mealybug'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Mirids_is_theanswer', This_rule_base, 'the_attacker',
                  Mirids_is_theanswer, None,
                  (pattern.pattern_literal('Mirids'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Podsucking_bugs_is_theanswer', This_rule_base, 'the_attacker',
                  Podsucking_bugs_is_theanswer, None,
                  (pattern.pattern_literal('Podsucking_bugs'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Scarabs_is_theanswer', This_rule_base, 'the_attacker',
                  Scarabs_is_theanswer, None,
                  (pattern.pattern_literal('Scarabs'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Sorghum_midge_is_theanswer', This_rule_base, 'the_attacker',
                  Sorghum_midge_is_theanswer, None,
                  (pattern.pattern_literal('Sorghum_midge'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Silverleaf_whitefly_is_theanswer', This_rule_base, 'the_attacker',
                  Silverleaf_whitefly_is_theanswer, None,
                  (pattern.pattern_literal('Silverleaf_whitefly'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Symphyla_is_theanswer', This_rule_base, 'the_attacker',
                  Symphyla_is_theanswer, None,
                  (pattern.pattern_literal('Symphyla'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Maize_thrips_is_theanswer', This_rule_base, 'the_attacker',
                  Maize_thrips_is_theanswer, None,
                  (pattern.pattern_literal('Maize_thrips'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Western_flower_thrips_is_theanswer', This_rule_base, 'the_attacker',
                  Western_flower_thrips_is_theanswer, None,
                  (pattern.pattern_literal('Western_flower_thrips'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('insecticidal_soaps_and_oils_is_theanswer', This_rule_base, 'the_product_is',
                  insecticidal_soaps_and_oils_is_theanswer, None,
                  (pattern.pattern_literal('insecticidal_soaps_and_oils'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('INSECTICIDES_WITH_PYRETHRIN_is_theanswer', This_rule_base, 'the_product_is',
                  INSECTICIDES_WITH_PYRETHRIN_is_theanswer, None,
                  (pattern.pattern_literal('INSECTICIDES_WITH_PYRETHRIN'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Azadirachtin_is_theanswer', This_rule_base, 'the_product_is',
                  Azadirachtin_is_theanswer, None,
                  (pattern.pattern_literal('Azadirachtin'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('systemic_insecticide_is_theanswer', This_rule_base, 'the_product_is',
                  systemic_insecticide_is_theanswer, None,
                  (pattern.pattern_literal('systemic_insecticide'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('MALATHION_is_theanswer', This_rule_base, 'the_product_is',
                  MALATHION_is_theanswer, None,
                  (pattern.pattern_literal('MALATHION'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Insect_growth_regulators_IGRs_is_theanswer', This_rule_base, 'the_product_is',
                  Insect_growth_regulators_IGRs_is_theanswer, None,
                  (pattern.pattern_literal('Insect_growth_regulators_IGRs'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Spinosad_is_theanswer', This_rule_base, 'the_product_is',
                  Spinosad_is_theanswer, None,
                  (pattern.pattern_literal('Spinosad'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('chlorantraniliprole_is_theanswer', This_rule_base, 'the_product_is',
                  chlorantraniliprole_is_theanswer, None,
                  (pattern.pattern_literal('chlorantraniliprole'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('pyrethroid_insecticides_is_theanswer', This_rule_base, 'the_product_is',
                  pyrethroid_insecticides_is_theanswer, None,
                  (pattern.pattern_literal('pyrethroid_insecticides'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('contact_insecticides_is_theanswer', This_rule_base, 'the_product_is',
                  contact_insecticides_is_theanswer, None,
                  (pattern.pattern_literal('contact_insecticides'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Methyl_bromide_is_theanswer', This_rule_base, 'the_product_is',
                  Methyl_bromide_is_theanswer, None,
                  (pattern.pattern_literal('Methyl_bromide'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Nimbecidine_is_theanswer', This_rule_base, 'the_product_is',
                  Nimbecidine_is_theanswer, None,
                  (pattern.pattern_literal('Nimbecidine'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('pesticides_containing_imidacloprid_is_theanswer', This_rule_base, 'the_product_is',
                  pesticides_containing_imidacloprid_is_theanswer, None,
                  (pattern.pattern_literal('pesticides_containing_imidacloprid'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('pesticide_Virtako_40WG_is_theanswer', This_rule_base, 'the_product_is',
                  pesticide_Virtako_40WG_is_theanswer, None,
                  (pattern.pattern_literal('pesticide_Virtako_40WG'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Eradicate_Sesbania_spp_is_theanswer', This_rule_base, 'the_product_is',
                  Eradicate_Sesbania_spp_is_theanswer, None,
                  (pattern.pattern_literal('Eradicate_Sesbania_spp'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Insecticide_seed_dressings_is_theanswer', This_rule_base, 'the_product_is',
                  Insecticide_seed_dressings_is_theanswer, None,
                  (pattern.pattern_literal('Insecticide_seed_dressings'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('insecticidal_soap_sprays_containing_fatty_acids_and_mineral_salts_is_theanswer', This_rule_base, 'the_product_is',
                  insecticidal_soap_sprays_containing_fatty_acids_and_mineral_salts_is_theanswer, None,
                  (pattern.pattern_literal('insecticidal_soap_sprays_containing_fatty_acids_and_mineral_salts'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Dipel_is_theanswer', This_rule_base, 'the_product_is',
                  Dipel_is_theanswer, None,
                  (pattern.pattern_literal('Dipel'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('NPV_is_theanswer', This_rule_base, 'the_product_is',
                  NPV_is_theanswer, None,
                  (pattern.pattern_literal('NPV'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Pupae_bustin_is_theanswer', This_rule_base, 'the_product_is',
                  Pupae_bustin_is_theanswer, None,
                  (pattern.pattern_literal('Pupae_bustin'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Use_Bifen_IT_is_theanswer', This_rule_base, 'the_product_is',
                  Use_Bifen_IT_is_theanswer, None,
                  (pattern.pattern_literal('Use_Bifen_IT'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Bifen_LP_is_theanswer', This_rule_base, 'the_product_is',
                  Bifen_LP_is_theanswer, None,
                  (pattern.pattern_literal('Bifen_LP'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Cyonara_Lawn_is_theanswer', This_rule_base, 'the_product_is',
                  Cyonara_Lawn_is_theanswer, None,
                  (pattern.pattern_literal('Cyonara_Lawn'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Garden_Insect_Control_is_theanswer', This_rule_base, 'the_product_is',
                  Garden_Insect_Control_is_theanswer, None,
                  (pattern.pattern_literal('Garden_Insect_Control'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Quali_Pro_1_is_theanswer', This_rule_base, 'the_product_is',
                  Quali_Pro_1_is_theanswer, None,
                  (pattern.pattern_literal('Quali_Pro_1'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('spinosyns_is_theanswer', This_rule_base, 'the_product_is',
                  spinosyns_is_theanswer, None,
                  (pattern.pattern_literal('spinosyns'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('pyrethroids1_is_theanswer', This_rule_base, 'the_product_is',
                  pyrethroids1_is_theanswer, None,
                  (pattern.pattern_literal('pyrethroids1'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('carbamates_is_theanswer', This_rule_base, 'the_product_is',
                  carbamates_is_theanswer, None,
                  (pattern.pattern_literal('carbamates'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Spinosad_GF_120_is_theanswer', This_rule_base, 'the_product_is',
                  Spinosad_GF_120_is_theanswer, None,
                  (pattern.pattern_literal('Spinosad_GF_120'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Proteus_170_O_TEQ_is_theanswer', This_rule_base, 'the_product_is',
                  Proteus_170_O_TEQ_is_theanswer, None,
                  (pattern.pattern_literal('Proteus_170_O_TEQ'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Propiconazole_Tilt_25_EC_is_theanswer', This_rule_base, 'the_product_is',
                  Propiconazole_Tilt_25_EC_is_theanswer, None,
                  (pattern.pattern_literal('Propiconazole_Tilt_25_EC'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Insecticide_products_with_emamectin_benzoate_is_theanswer', This_rule_base, 'the_product_is',
                  Insecticide_products_with_emamectin_benzoate_is_theanswer, None,
                  (pattern.pattern_literal('Insecticide_products_with_emamectin_benzoate'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Bacillus_thuringiensis_kurtaki_Btk_is_theanswer', This_rule_base, 'the_product_is',
                  Bacillus_thuringiensis_kurtaki_Btk_is_theanswer, None,
                  (pattern.pattern_literal('Bacillus_thuringiensis_kurtaki_Btk'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Liquid_termiticide_is_theanswer', This_rule_base, 'the_product_is',
                  Liquid_termiticide_is_theanswer, None,
                  (pattern.pattern_literal('Liquid_termiticide'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('no_chemical_control_is_theanswer', This_rule_base, 'the_product_is',
                  no_chemical_control_is_theanswer, None,
                  (pattern.pattern_literal('no_chemical_control'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('horticultural_oils_is_theanswer', This_rule_base, 'the_product_is',
                  horticultural_oils_is_theanswer, None,
                  (pattern.pattern_literal('horticultural_oils'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Beuvaria_bassiana_is_theanswer', This_rule_base, 'the_product_is',
                  Beuvaria_bassiana_is_theanswer, None,
                  (pattern.pattern_literal('Beuvaria_bassiana'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('organophosphates_is_theanswer', This_rule_base, 'the_product_is',
                  organophosphates_is_theanswer, None,
                  (pattern.pattern_literal('organophosphates'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('pesticides_containing_esfenvalerate_is_theanswer', This_rule_base, 'the_product_is',
                  pesticides_containing_esfenvalerate_is_theanswer, None,
                  (pattern.pattern_literal('pesticides_containing_esfenvalerate'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('pesticides_containing_permethrin_is_theanswer', This_rule_base, 'the_product_is',
                  pesticides_containing_permethrin_is_theanswer, None,
                  (pattern.pattern_literal('pesticides_containing_permethrin'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Asana_is_theanswer', This_rule_base, 'the_product_is',
                  Asana_is_theanswer, None,
                  (pattern.pattern_literal('Asana'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Baythroid_is_theanswer', This_rule_base, 'the_product_is',
                  Baythroid_is_theanswer, None,
                  (pattern.pattern_literal('Baythroid'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Brigade_is_theanswer', This_rule_base, 'the_product_is',
                  Brigade_is_theanswer, None,
                  (pattern.pattern_literal('Brigade'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Karate_is_theanswer', This_rule_base, 'the_product_is',
                  Karate_is_theanswer, None,
                  (pattern.pattern_literal('Karate'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Prolex_is_theanswer', This_rule_base, 'the_product_is',
                  Prolex_is_theanswer, None,
                  (pattern.pattern_literal('Prolex'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Sevin_is_theanswer', This_rule_base, 'the_product_is',
                  Sevin_is_theanswer, None,
                  (pattern.pattern_literal('Sevin'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Acetamiprid_Gazelle_is_theanswer', This_rule_base, 'the_product_is',
                  Acetamiprid_Gazelle_is_theanswer, None,
                  (pattern.pattern_literal('Acetamiprid_Gazelle'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('propyzamide_herbicide_is_theanswer', This_rule_base, 'the_product_is',
                  propyzamide_herbicide_is_theanswer, None,
                  (pattern.pattern_literal('insecticidal_soaps_and_oils'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('carbetamide_herbicide_is_theanswer', This_rule_base, 'the_product_is',
                  carbetamide_herbicide_is_theanswer, None,
                  (pattern.pattern_literal('carbetamide_herbicide'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Dimethoate_is_theanswer', This_rule_base, 'the_product_is',
                  Dimethoate_is_theanswer, None,
                  (pattern.pattern_literal('Dimethoate'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Methomyl_is_theanswer', This_rule_base, 'the_product_is',
                  Methomyl_is_theanswer, None,
                  (pattern.pattern_literal('Methomyl'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Buprofezin_is_theanswer', This_rule_base, 'the_product_is',
                  Buprofezin_is_theanswer, None,
                  (pattern.pattern_literal('Buprofezin'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Bifenazate_is_theanswer', This_rule_base, 'the_product_is',
                  Bifenazate_is_theanswer, None,
                  (pattern.pattern_literal('Bifenazate'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Deltamethrin_is_theanswer', This_rule_base, 'the_product_is',
                  Deltamethrin_is_theanswer, None,
                  (pattern.pattern_literal('Deltamethrin'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Fluvalinate_is_theanswer', This_rule_base, 'the_product_is',
                  Fluvalinate_is_theanswer, None,
                  (pattern.pattern_literal('Fluvalinate'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Organophosphate_is_theanswer', This_rule_base, 'the_product_is',
                  Organophosphate_is_theanswer, None,
                  (pattern.pattern_literal('Organophosphate'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('Short_residual_contact_is_theanswer', This_rule_base, 'the_product_is',
                  Short_residual_contact_is_theanswer, None,
                  (pattern.pattern_literal('Short_residual_contact'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('malathion_is_theanswer', This_rule_base, 'the_product_is',
                  malathion_is_theanswer, None,
                  (pattern.pattern_literal('malathion'),),
                  (),
                  (contexts.variable('ans'),))


Krb_filename = '..\\rules2.krb'
Krb_lineno_map = (
    ((14, 18), (2, 2)),
    ((20, 25), (4, 4)),
    ((26, 26), (5, 5)),
    ((39, 43), (7, 7)),
    ((45, 50), (9, 9)),
    ((51, 51), (10, 10)),
    ((64, 68), (12, 12)),
    ((70, 75), (14, 14)),
    ((76, 76), (15, 15)),
    ((89, 93), (17, 17)),
    ((95, 100), (19, 19)),
    ((101, 101), (20, 20)),
    ((114, 118), (22, 22)),
    ((120, 125), (24, 24)),
    ((126, 126), (25, 25)),
    ((139, 143), (28, 28)),
    ((145, 150), (30, 30)),
    ((151, 151), (31, 31)),
    ((164, 168), (33, 33)),
    ((170, 175), (35, 35)),
    ((176, 176), (36, 36)),
    ((189, 193), (38, 38)),
    ((195, 200), (40, 40)),
    ((201, 201), (41, 41)),
    ((214, 218), (43, 43)),
    ((220, 225), (45, 45)),
    ((226, 226), (46, 46)),
    ((239, 243), (48, 48)),
    ((245, 250), (50, 50)),
    ((251, 251), (51, 51)),
    ((264, 268), (53, 53)),
    ((270, 275), (55, 55)),
    ((276, 276), (56, 56)),
    ((289, 293), (58, 58)),
    ((295, 300), (60, 60)),
    ((301, 301), (61, 61)),
    ((314, 318), (63, 63)),
    ((320, 325), (65, 65)),
    ((326, 326), (66, 66)),
    ((339, 343), (68, 68)),
    ((345, 350), (70, 70)),
    ((351, 351), (71, 71)),
    ((364, 368), (73, 73)),
    ((370, 375), (75, 75)),
    ((376, 376), (76, 76)),
    ((389, 393), (78, 78)),
    ((395, 400), (80, 80)),
    ((401, 401), (81, 81)),
    ((414, 418), (83, 83)),
    ((420, 425), (85, 85)),
    ((426, 426), (86, 86)),
    ((439, 443), (88, 88)),
    ((445, 450), (90, 90)),
    ((451, 451), (91, 91)),
    ((464, 468), (93, 93)),
    ((470, 475), (95, 95)),
    ((476, 476), (96, 96)),
    ((489, 493), (98, 98)),
    ((495, 500), (100, 100)),
    ((501, 501), (101, 101)),
    ((514, 518), (103, 103)),
    ((520, 525), (105, 105)),
    ((526, 526), (106, 106)),
    ((539, 543), (108, 108)),
    ((545, 550), (110, 110)),
    ((551, 551), (111, 111)),
    ((564, 568), (113, 113)),
    ((570, 575), (115, 115)),
    ((576, 576), (116, 116)),
    ((589, 593), (118, 118)),
    ((595, 600), (120, 120)),
    ((601, 601), (121, 121)),
    ((614, 618), (123, 123)),
    ((620, 625), (125, 125)),
    ((626, 626), (126, 126)),
    ((639, 643), (128, 128)),
    ((645, 650), (130, 130)),
    ((651, 651), (131, 131)),
    ((664, 668), (133, 133)),
    ((670, 675), (135, 135)),
    ((676, 676), (136, 136)),
    ((689, 693), (138, 138)),
    ((695, 700), (140, 140)),
    ((701, 701), (141, 141)),
    ((714, 718), (143, 143)),
    ((720, 725), (145, 145)),
    ((726, 726), (146, 146)),
    ((739, 743), (148, 148)),
    ((745, 750), (150, 150)),
    ((751, 751), (151, 151)),
    ((764, 768), (153, 153)),
    ((770, 775), (155, 155)),
    ((776, 776), (156, 156)),
    ((789, 793), (158, 158)),
    ((795, 800), (160, 160)),
    ((801, 801), (161, 161)),
    ((814, 818), (163, 163)),
    ((820, 825), (165, 165)),
    ((826, 826), (166, 166)),
    ((839, 843), (168, 168)),
    ((845, 850), (170, 170)),
    ((851, 851), (171, 171)),
    ((864, 868), (173, 173)),
    ((870, 875), (175, 175)),
    ((876, 876), (176, 176)),
    ((889, 893), (178, 178)),
    ((895, 900), (180, 180)),
    ((901, 901), (181, 181)),
    ((914, 918), (183, 183)),
    ((920, 925), (185, 185)),
    ((926, 926), (186, 186)),
    ((939, 943), (188, 188)),
    ((945, 950), (190, 190)),
    ((951, 951), (191, 191)),
    ((964, 968), (193, 193)),
    ((970, 975), (195, 195)),
    ((976, 976), (196, 196)),
    ((989, 993), (198, 198)),
    ((995, 1000), (200, 200)),
    ((1001, 1001), (201, 201)),
    ((1014, 1018), (203, 203)),
    ((1020, 1025), (205, 205)),
    ((1026, 1026), (206, 206)),
    ((1039, 1043), (208, 208)),
    ((1045, 1050), (210, 210)),
    ((1051, 1051), (211, 211)),
    ((1064, 1068), (213, 213)),
    ((1070, 1075), (215, 215)),
    ((1076, 1076), (216, 216)),
    ((1089, 1093), (218, 218)),
    ((1095, 1100), (220, 220)),
    ((1101, 1101), (221, 221)),
    ((1114, 1118), (223, 223)),
    ((1120, 1125), (225, 225)),
    ((1126, 1126), (226, 226)),
    ((1139, 1143), (228, 228)),
    ((1145, 1150), (230, 230)),
    ((1151, 1151), (231, 231)),
    ((1164, 1168), (233, 233)),
    ((1170, 1175), (235, 235)),
    ((1176, 1176), (236, 236)),
    ((1189, 1193), (238, 238)),
    ((1195, 1200), (240, 240)),
    ((1201, 1201), (241, 241)),
    ((1214, 1218), (243, 243)),
    ((1220, 1225), (245, 245)),
    ((1226, 1226), (246, 246)),
    ((1239, 1243), (248, 248)),
    ((1245, 1250), (250, 250)),
    ((1251, 1251), (251, 251)),
    ((1264, 1268), (253, 253)),
    ((1270, 1275), (255, 255)),
    ((1276, 1276), (256, 256)),
    ((1289, 1293), (258, 258)),
    ((1295, 1300), (260, 260)),
    ((1301, 1301), (261, 261)),
    ((1314, 1318), (263, 263)),
    ((1320, 1325), (265, 265)),
    ((1326, 1326), (266, 266)),
    ((1339, 1343), (268, 268)),
    ((1345, 1350), (270, 270)),
    ((1351, 1351), (271, 271)),
    ((1364, 1368), (273, 273)),
    ((1370, 1375), (275, 275)),
    ((1376, 1376), (276, 276)),
    ((1389, 1393), (278, 278)),
    ((1395, 1400), (280, 280)),
    ((1401, 1401), (281, 281)),
    ((1414, 1418), (283, 283)),
    ((1420, 1425), (285, 285)),
    ((1426, 1426), (286, 286)),
    ((1439, 1443), (288, 288)),
    ((1445, 1450), (290, 290)),
    ((1451, 1451), (291, 291)),
    ((1464, 1468), (293, 293)),
    ((1470, 1475), (295, 295)),
    ((1476, 1476), (296, 296)),
    ((1489, 1493), (298, 298)),
    ((1495, 1500), (300, 300)),
    ((1501, 1501), (301, 301)),
    ((1514, 1518), (303, 303)),
    ((1520, 1525), (305, 305)),
    ((1526, 1526), (306, 306)),
    ((1539, 1543), (309, 309)),
    ((1545, 1550), (311, 311)),
    ((1551, 1551), (312, 312)),
    ((1564, 1568), (314, 314)),
    ((1570, 1575), (316, 316)),
    ((1576, 1576), (317, 317)),
    ((1589, 1593), (319, 319)),
    ((1595, 1600), (321, 321)),
    ((1601, 1601), (322, 322)),
    ((1614, 1618), (324, 324)),
    ((1620, 1625), (326, 326)),
    ((1626, 1626), (327, 327)),
    ((1639, 1643), (329, 329)),
    ((1645, 1650), (331, 331)),
    ((1651, 1651), (332, 332)),
    ((1664, 1668), (334, 334)),
    ((1670, 1675), (336, 336)),
    ((1676, 1676), (337, 337)),
    ((1689, 1693), (339, 339)),
    ((1695, 1700), (341, 341)),
    ((1701, 1701), (342, 342)),
    ((1714, 1718), (344, 344)),
    ((1720, 1725), (346, 346)),
    ((1726, 1726), (347, 347)),
    ((1739, 1743), (349, 349)),
    ((1745, 1750), (351, 351)),
    ((1751, 1751), (352, 352)),
    ((1764, 1768), (354, 354)),
    ((1770, 1775), (356, 356)),
    ((1776, 1776), (357, 357)),
    ((1789, 1793), (359, 359)),
    ((1795, 1800), (361, 361)),
    ((1801, 1801), (362, 362)),
    ((1814, 1818), (364, 364)),
    ((1820, 1825), (366, 366)),
    ((1826, 1826), (367, 367)),
    ((1839, 1843), (369, 369)),
    ((1845, 1850), (371, 371)),
    ((1851, 1851), (372, 372)),
    ((1864, 1868), (374, 374)),
    ((1870, 1875), (376, 376)),
    ((1876, 1876), (377, 377)),
    ((1889, 1893), (379, 379)),
    ((1895, 1900), (381, 381)),
    ((1901, 1901), (382, 382)),
    ((1914, 1918), (384, 384)),
    ((1920, 1925), (386, 386)),
    ((1926, 1926), (387, 387)),
    ((1939, 1943), (389, 389)),
    ((1945, 1950), (391, 391)),
    ((1951, 1951), (392, 392)),
    ((1964, 1968), (394, 394)),
    ((1970, 1975), (396, 396)),
    ((1976, 1976), (397, 397)),
    ((1989, 1993), (399, 399)),
    ((1995, 2000), (401, 401)),
    ((2001, 2001), (402, 402)),
    ((2014, 2018), (404, 404)),
    ((2020, 2025), (406, 406)),
    ((2026, 2026), (407, 407)),
    ((2039, 2043), (409, 409)),
    ((2045, 2050), (411, 411)),
    ((2051, 2051), (412, 412)),
    ((2064, 2068), (414, 414)),
    ((2070, 2075), (416, 416)),
    ((2076, 2076), (417, 417)),
    ((2089, 2093), (419, 419)),
    ((2095, 2100), (421, 421)),
    ((2101, 2101), (422, 422)),
    ((2114, 2118), (424, 424)),
    ((2120, 2125), (426, 426)),
    ((2126, 2126), (427, 427)),
    ((2139, 2143), (429, 429)),
    ((2145, 2150), (431, 431)),
    ((2151, 2151), (432, 432)),
    ((2164, 2168), (434, 434)),
    ((2170, 2175), (436, 436)),
    ((2176, 2176), (437, 437)),
    ((2189, 2193), (439, 439)),
    ((2195, 2200), (441, 441)),
    ((2201, 2201), (442, 442)),
    ((2214, 2218), (444, 444)),
    ((2220, 2225), (446, 446)),
    ((2226, 2226), (447, 447)),
    ((2239, 2243), (449, 449)),
    ((2245, 2250), (451, 451)),
    ((2251, 2251), (452, 452)),
    ((2264, 2268), (454, 454)),
    ((2270, 2275), (456, 456)),
    ((2276, 2276), (457, 457)),
    ((2289, 2293), (459, 459)),
    ((2295, 2300), (461, 461)),
    ((2301, 2301), (462, 462)),
    ((2314, 2318), (464, 464)),
    ((2320, 2325), (466, 466)),
    ((2326, 2326), (467, 467)),
    ((2339, 2343), (469, 469)),
    ((2345, 2350), (471, 471)),
    ((2351, 2351), (472, 472)),
    ((2364, 2368), (474, 474)),
    ((2370, 2375), (476, 476)),
    ((2376, 2376), (477, 477)),
    ((2389, 2393), (479, 479)),
    ((2395, 2400), (481, 481)),
    ((2401, 2401), (482, 482)),
    ((2414, 2418), (484, 484)),
    ((2420, 2425), (486, 486)),
    ((2426, 2426), (487, 487)),
    ((2439, 2443), (489, 489)),
    ((2445, 2450), (491, 491)),
    ((2451, 2451), (492, 492)),
    ((2464, 2468), (494, 494)),
    ((2470, 2475), (496, 496)),
    ((2476, 2476), (497, 497)),
    ((2489, 2493), (499, 499)),
    ((2495, 2500), (501, 501)),
    ((2501, 2501), (502, 502)),
    ((2514, 2518), (504, 504)),
    ((2520, 2525), (506, 506)),
    ((2526, 2526), (507, 507)),
    ((2539, 2543), (509, 509)),
    ((2545, 2550), (511, 511)),
    ((2551, 2551), (512, 512)),
    ((2564, 2568), (514, 514)),
    ((2570, 2575), (516, 516)),
    ((2576, 2576), (517, 517)),
    ((2589, 2593), (519, 519)),
    ((2595, 2600), (521, 521)),
    ((2601, 2601), (522, 522)),
    ((2614, 2618), (524, 524)),
    ((2620, 2625), (526, 526)),
    ((2626, 2626), (527, 527)),
    ((2639, 2643), (529, 529)),
    ((2645, 2650), (531, 531)),
    ((2651, 2651), (532, 532)),
    ((2664, 2668), (534, 534)),
    ((2670, 2675), (536, 536)),
    ((2676, 2676), (537, 537)),
    ((2689, 2693), (539, 539)),
    ((2695, 2700), (541, 541)),
    ((2701, 2701), (542, 542)),
    ((2714, 2718), (544, 544)),
    ((2720, 2725), (546, 546)),
    ((2726, 2726), (547, 547)),
    ((2739, 2743), (549, 549)),
    ((2745, 2750), (551, 551)),
    ((2751, 2751), (552, 552)),
    ((2764, 2768), (554, 554)),
    ((2770, 2775), (556, 556)),
    ((2776, 2776), (557, 557)),
    ((2789, 2793), (559, 559)),
    ((2795, 2800), (561, 561)),
    ((2801, 2801), (562, 562)),
    ((2814, 2818), (564, 564)),
    ((2820, 2825), (566, 566)),
    ((2826, 2826), (567, 567)),
    ((2839, 2843), (569, 569)),
    ((2845, 2850), (571, 571)),
    ((2851, 2851), (572, 572)),
    ((2864, 2868), (574, 574)),
    ((2870, 2875), (576, 576)),
    ((2876, 2876), (577, 577)),
    ((2889, 2893), (579, 579)),
    ((2895, 2900), (581, 581)),
    ((2901, 2901), (582, 582)),
    ((2914, 2918), (584, 584)),
    ((2920, 2925), (586, 586)),
    ((2926, 2926), (587, 587)),
    ((2939, 2943), (589, 589)),
    ((2945, 2950), (591, 591)),
    ((2951, 2951), (592, 592)),
    ((2964, 2968), (594, 594)),
    ((2970, 2975), (596, 596)),
    ((2976, 2976), (597, 597)),
)
