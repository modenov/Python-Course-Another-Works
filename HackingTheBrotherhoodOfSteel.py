#  Copyright (c) Vladimir Modenov.
#  Created: 22.09.2022, 23:08
#  Project: StepikPythonProjects
#  File: HackingTheBrotherhoodOfSteel.py

# Помогите писцу Ибсену удалить все комментарии из программы.

n = input()

for _ in range(int(n[1:])):
    s = input()
    if '#' in s:
        s = s[:s.find('#')]
    print(s.rstrip())
