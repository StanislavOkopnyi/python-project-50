filepath1_filepath2_json = \
    """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""

file1_file2_yaml = \
    """Property 'Cheesemonger' was updated. From ['Blue cheese', 'Feta'] to ['Red cheese', 'Feta']"""

file3_file4_yaml = \
    """Property 'development.database' was updated. From 'notmyapp_development' to 'myapp_development'"""

file1_file2_json = \
    """Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true"""

file3_file4_json = \
    """Property 'color' was updated. From 'black' to 'blue'
Property 'type' was updated. From 'primary' to 'secondary'"""

file5_file6_json = \
    """Property 'date' was updated. From '2017-07-21T10:30:34' to '2018-07-21T10:30:34'
Property 'guid.rendered' was updated. From 'https://www.sitepoint.com/?p=157538' to 'http://www.sitepoint.com/?p=157538'
Property 'modified' was updated. From '2017-07-23T21:56:35' to '2018-07-23T21:56:35'
Property 'title.rendered' was updated. From 'Why the IoT Threatens Your WordPress Site (and How to Fix It)' to 'Why the IoT Threatens Your Tilda Site (and How to Fix It)'"""

file3_file3_1_json = \
    """Property 'category' was removed
Property 'color' was removed
Property 'hex' was removed
Property 'rgba' was removed
Property 'type' was removed"""

file3_1_file3_json = \
    """Property 'category' was added with value: 'hue'
Property 'color' was added with value: 'black'
Property 'hex' was added with value: '#000'
Property 'rgba' was added with value: [255, 255, 255, 1]
Property 'type' was added with value: 'primary'"""
