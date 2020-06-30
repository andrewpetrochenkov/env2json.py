<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/env2json.svg?maxAge=3600)](https://pypi.org/project/env2json/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/env2json.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/env2json.py/actions)

### Installation
```bash
$ [sudo] pip install env2json
```

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
    <a href="https://readme42.com/">readme42.com</a>
</p>