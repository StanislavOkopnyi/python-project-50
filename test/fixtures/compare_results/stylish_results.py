file1_file2_json = \
    """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

file3_file4_json = \
    """{
    category: hue
  - color: black
  + color: blue
    hex: #000
    rgba: [255, 255, 255, 1]
  - type: primary
  + type: secondary
}"""

file5_file6_json = \
    """{
  - date: 2017-07-21T10:30:34
  + date: 2018-07-21T10:30:34
    date_gmt: 2017-07-21T17:30:34
    guid: {
      - rendered: https://www.sitepoint.com/?p=157538
      + rendered: http://www.sitepoint.com/?p=157538
    }
    id: 157538
    link: https://www.sitepoint.com/why-the-iot-threatens-your-wordpress-site-and-how-to-fix-it/
  - modified: 2017-07-23T21:56:35
  + modified: 2018-07-23T21:56:35
    modified_gmt: 2017-07-24T04:56:35
    slug: why-the-iot-threatens-your-wordpress-site-and-how-to-fix-it
    status: publish
    title: {
      - rendered: Why the IoT Threatens Your WordPress Site (and How to Fix It)
      + rendered: Why the IoT Threatens Your Tilda Site (and How to Fix It)
    }
    type: post
}"""

file1_file2_yaml = \
    """{
    Bakery: [Sourdough loaf, Bagels]
  - Cheesemonger: [Blue cheese, Feta]
  + Cheesemonger: [Red cheese, Feta]
}"""

file3_file4_yaml = \
    """{
    defaults: {
        adapter: postgres
        host: localhost
    }
    development: {
        adapter: postgres
      - database: notmyapp_development
      + database: myapp_development
        host: localhost
    }
    test: {
        adapter: postgres
        database: myapp_test
        host: localhost
    }
}"""

file3_file3_1_json = \
    """{
  - category: hue
  - color: black
  - hex: #000
  - rgba: [255, 255, 255, 1]
  - type: primary
}"""

file3_1_file3_json = \
    """{
  + category: hue
  + color: black
  + hex: #000
  + rgba: [255, 255, 255, 1]
  + type: primary
}"""

filepath1_filepath2_json = \
    """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: \n              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""

filepath1_filepath2_yaml = \
    """{
    employees: {
        martin: {
          - job: Developer
          + job: Data scientist
            name: Martin D'vloper
          - skills: [python, perl, pascal]
          + skills: [python, go, pascal]
        }
        tabitha: {
            job: Developer
            name: Tabitha Bitumen
          - skills: [lisp, fortran, erlang]
          + skills: [lisp, cobol, erlang]
        }
    }
}"""
