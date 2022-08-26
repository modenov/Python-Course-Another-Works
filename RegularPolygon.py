"""
Правильный многоугольник — выпуклый многоугольник, у которого равны все стороны
и все углы между смежными сторонами. Площадь правильного многоугольника с длиной стороны a
и количеством сторон n.
"""

#  Copyright (c) Vladimir Modenov.
#  Created: 13.08.2022, 22:09
#  Project: StepikPythonProjects
#  File: RegularPolygon.py

import math

n = int(input())
a = float(input())

S = (n * a**2) / (4 * math.tan(math.pi / n))

print(S)
