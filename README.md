<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/env2json.svg?longCache=True)](https://pypi.org/project/env2json/)
[![](https://img.shields.io/pypi/v/env2json.svg?maxAge=3600)](https://pypi.org/project/env2json/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/env2json.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/env2json.py/)

#### Installation
```bash
$ [sudo] pip install env2json
```

#### Executable modules
usage|`__doc__`
-|-
`python -m env2json path` |print `.env` as json

#### Examples
`.env.dev`
```bash
DB_NAME=name
DB_USER=username
DB_HOST=127.0.0.1
DB_PORT=5432
```

```bash
$ python -m env2json .env.dev > .env.dev.json
```

`.env.dev.json`
```json
{
  "DB_HOST": "127.0.0.1",
  "DB_NAME": "name",
  "DB_PORT": "5432",
  "DB_USER": "username"
}
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>