test = {   'name': 'q34',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> # from numpy import std;\n>>> stdv = np.std(new_bootstrap_estimates);\n>>> 0 < stdv < 10\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> 0 < new_right_end - new_left_end < 45\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> stdv = np.std(new_bootstrap_estimates);\n>>> abs(((new_right_end - new_left_end) / stdv) - 3.9) < 0.2\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
