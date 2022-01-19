import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

food_quality = ctrl.Antecedent(np.arange(0, 11, 1), 'food_quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')

tip = ctrl.Consequent(np.arange(0, 21, 1), 'tip')

print(tip.universe)
