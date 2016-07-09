# coding: utf-8

# read_api = { 'json': # =>
#         'route': '/users/',
#         'views': [
#             'id': 'Int',
#             'username': 'String:164',
#         ],
# }


# create_api = {'json': # =>
# }


# update_api = {'json': # =>
# }


# delete_api = {'json': # =>
# }


user_apis = {'json': # =>
        [
            {
                'route': '/users/',
                'views': [
                    'username': 'String:164',
                    'id': 'Int',
                ],
                'paginate': True,
                'public': True,
                'mock': True,
            },
            {
                'route': '/users/<int:id>/',
                'views': [
                    'username': 'String:164',
                    'id': 'Int',
                    'intro': 'Text'
                ],
                'paginate': False,
                'public': True,
                'mock': True,
            }
        ]
}
