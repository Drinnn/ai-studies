import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

food_quality = ctrl.Antecedent(np.arange(0, 11, 1), 'food_quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')

tip = ctrl.Consequent(np.arange(0, 21, 1), 'tip')

food_quality.automf(number=3, names=['bad', 'good', 'tasty'])
service.automf(number=3, names=['bad', 'acceptable', 'great'])

tip['low'] = fuzz.sigmf(tip.universe, 5, -1)
tip['medium'] = fuzz.gaussmf(tip.universe, 10, 3)
tip['high'] = fuzz.pimf(tip.universe, 10, 20, 20, 21)

rule_1 = ctrl.Rule(food_quality['bad'] | service['bad'], tip['low'])
rule_2 = ctrl.Rule(service['acceptable'], tip['medium'])
rule_3 = ctrl.Rule(service['great'] | food_quality['tasty'], tip['high'])

control_system = ctrl.ControlSystem([rule_1, rule_2, rule_3])
system = ctrl.ControlSystemSimulation(control_system)

tip.view()

plt.show()
