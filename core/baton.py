BATON = {
    'SITE_HEADER': 'Guru Mantra',
    'SITE_TITLE': 'Guru Mantra',
    'INDEX_TITLE': 'Guru Mantra',
    'SUPPORT_HREF': '   ',
    'POWERED_BY': 'Guru Mantra',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'CHANGELIST_FILTERS_IN_MODAL': True,
    'CHANGELIST_FILTERS_ALWAYS_OPEN': True,
    'CHANGELIST_FILTERS_FORM': True,
    'MENU_ALWAYS_COLLAPSED': False,
    'MENU_TITLE': 'Menu',
    'GRAVATAR_DEFAULT_IMG': 'retro',
    'MENU': (
        {'type': 'title', 'label': 'main', 'apps': ('auth',)},
        {
            'type': 'app',
            'name': 'auth',
            'label': 'Authentication',
            'icon': 'fa fa-lock',
            'models': (
                {
                    'name': 'user',
                    'label': 'Users'
                },
                {
                    'name': 'group',
                    'label': 'Groups'
                }
            )
        },

        {'type': 'title', 'label': 'content', 'apps': ('katha', 'mantra', 'poojabidhi', 'chadparba')},

        {
            'type': 'app',
            'name': 'katha',
            'label': 'Katha',
            'icon': 'fa fa-book',
            'models': (
                {
                    'name': 'katha',
                    'label': 'Katha'
                },
            )
        },
        {
            'type': 'app',
            'name': 'mantra',
            'label': 'Mantra',
            'icon': 'fa  fa-connectdevelop',
            'models': (
                {
                    'name': 'mantra',
                    'label': 'Mantra'
                },

                {
                    'name': 'category',
                    'label': 'Category'
                }
            )
        },
        {
            'type': 'app',
            'name': 'poojabidhi',
            'label': 'Pooja Bidhi',
            'icon': 'fa fa-envelope',
            'models': (
                {
                    'name': 'poojabidhi',
                    'label': 'Pooja Bidhi'
                },
            )
        },
        {
            'type': 'app',
            'name': 'chadparba',
            'label': 'Chad Parba',
            'icon': 'fa fa-book',
            'models': (
                {
                    'name': 'chadparba',
                    'label': 'Chad Parba'
                },
            )
        },
    )
}
