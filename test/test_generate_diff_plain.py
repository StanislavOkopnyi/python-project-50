from gendiff import generate_diff
from gendiff.plain import plain


def test_gendiff_path():
    input_data1 = "test/fixtures/filepath1.json", "test/fixtures/filepath2.json"
    expected = """Property 'common.follow' was added with value: false
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

    assert generate_diff(*input_data1, plain) == expected


def test_gendiff_yaml():
    input_data1 = "test/fixtures/file1.yaml", "test/fixtures/file2.yaml"
    expected1 = """Property 'Cheesemonger' was updated. From ['Blue cheese', 'Feta'] to ['Red cheese', 'Feta']"""

    assert generate_diff(*input_data1, plain) == expected1

    input_data2 = "test/fixtures/file3.yaml", "test/fixtures/file4.yaml"
    expected2 = """Property 'development.database' was updated. From 'notmyapp_development' to 'myapp_development'"""

    assert generate_diff(*input_data2, plain) == expected2


def test_gendiff_json():
    input_data1 = "test/fixtures/file1.json", "test/fixtures/file2.json"
    expected1 = """Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true"""

    assert generate_diff(*input_data1, plain) == expected1

    input_data2 = "test/fixtures/file3.json", "test/fixtures/file4.json"
    expected2 = """Property 'color' was updated. From 'black' to 'blue'
Property 'type' was updated. From 'primary' to 'secondary'"""

    assert generate_diff(*input_data2, plain) == expected2

    input_data3 = "test/fixtures/file5.json", "test/fixtures/file6.json"
    expected = """Property 'date' was updated. From '2017-07-21T10:30:34' to '2018-07-21T10:30:34'
Property 'guid.rendered' was updated. From 'https://www.sitepoint.com/?p=157538' to 'rendered: http://www.sitepoint.com/?p=157538'
Property 'modified' was updated. From '2017-07-23T21:56:35' to '2018-07-23T21:56:35'
Property 'title.rendered' was updated. From 'Why the IoT Threatens Your WordPress Site (and How to Fix It)' to 'Why the IoT Threatens Your Tilda Site (and How to Fix It)'"""


def test_gendiff_json_empty():
    input_data1 = "test/fixtures/file3.json", "test/fixtures/file3_1.json"
    expected1 = """Property 'category' was removed
Property 'color' was removed
Property 'hex' was removed
Property 'rgba' was removed
Property 'type' was removed"""

    assert generate_diff(*input_data1, plain) == expected1

    input_data2 = "test/fixtures/file3_1.json", "test/fixtures/file3.json"
    expected2 = """Property 'category' was added with value: 'hue'
Property 'color' was added with value: 'black'
Property 'hex' was added with value: '#000'
Property 'rgba' was added with value: [255, 255, 255, 1]
Property 'type' was added with value: 'primary'"""

    assert generate_diff(*input_data2, plain) == expected2
