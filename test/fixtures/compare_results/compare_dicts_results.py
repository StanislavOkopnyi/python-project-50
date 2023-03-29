test_compare_dicts1 = \
    [{'name': 'foo', 'last': '"bar"', 'now': '"bar"', 'type': 'item'},
     {'name': 'joo',
      'value': [
          {'name': 'noo',
           'last': '"mar"',
           'now': '"mar"',
           'type': 'item'},
          {'name': 'qoo',
           'last': '"__empty_value__"',
           'now': '"xar"',
           'type': 'item'},
          {'name': 'zoo',
           'last': '"xar"',
           'now': '"__empty_value__"',
           'type': 'item'}],
      'type': 'common_dict'},
     {'name': 'loo',
      'last': '"__empty_value__"',
      'now': [{'name': 'moo', 'last': '"dar"', 'now': '"dar"', 'type': 'item'}],
      'type': 'item'},
     {'name': 'roo', 'last': '"aar"', 'now': '"__empty_value__"', 'type': 'item'}]

test_make_common_dict1 = \
    {'name': 'foo',
     'value': [{'name': 'w', 'last': '"z"', 'now': '"w"', 'type': 'item'},
               {'name': 'x', 'last': '"y"', 'now': '"y"', 'type': 'item'}],
     'type': 'common_dict'}
