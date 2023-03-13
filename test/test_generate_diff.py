import pytest
from gendiff import generate_diff


def test_gendiff1():
    input_data1 = "test/fixtures/file1.json", "test/fixtures/file2.json"
    expected1 = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff(*input_data1) == expected1
    input_data2 = "test/fixtures/file3.json", "test/fixtures/file4.json"
    expected2 = """{
    category: hue
  - color: black
  + color: blue
    hex: #000
    rgba: [255, 255, 255, 1]
  - type: primary
  + type: secondary
}"""
    assert generate_diff(*input_data2) == expected2
    input_data3 = "test/fixtures/file5.json", "test/fixtures/file6.json"
    expected3 = """{
      - date: 2017-07-21T10:30:34
      + date: 2018-07-21T10:30:34
        date_gmt: 2017-07-21T17:30:34
      - guid: {"rendered": "https://www.sitepoint.com/?p=157538"}
      + guid: {"rendered": "http://www.sitepoint.com/?p=157538"}
        id: 157538
        link: https://www.sitepoint.com/why-the-iot-threatens-your-wordpress-site-and-how-to-fix-it/
      - modified: 2017-07-23T21:56:35
      + modified: 2018-07-23T21:56:35
        modified_gmt: 2017-07-24T04:56:35
        slug: why-the-iot-threatens-your-wordpress-site-and-how-to-fix-it
        status: publish
      - title: {"rendered": "Why the IoT Threatens Your WordPress Site (and How to Fix It)"}
      + title: {"rendered": "Why the IoT Threatens Your Tilda Site (and How to Fix It)"}
        type: post
    }"""


def test_gendiff2():
    input_data1 = "some_file.json", "test/fixtures/file2.json"
    input_data2 = "test/fixtures/file2.json", "some_file.json"
    expected = "Can't find some_file.json"
    assert generate_diff(*input_data1) == expected
    assert generate_diff(*input_data2) == expected
