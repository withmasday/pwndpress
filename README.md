<h1 align="center">PwndPRESS</h1>

<p align="center">PwndPRESS Is An WordPress Theme/Plugins Exploiting Tool</p>

<div align="center">

[![All Contributors](https://img.shields.io/github/contributors/withmasday/pwndpress)](https://github.com/withmasday/pwndpress/graphs/contributors)
![GitHub last commit](https://img.shields.io/github/last-commit/withmasday/pwndpress.svg)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/withmasday/pwndpress)
[![License](https://img.shields.io/github/license/withmasday/pwndpress.svg)](LICENSE)

</div>

## Install Dependencies

**python3**

- [Download Python3](https://www.python.org/downloads/) (Mac, Linux, Windows)
- Linux `sudo apt install python3 -y`
- Brew `brew install python3`

**Dependencies**

```bash
  pip install -r requirements.txt
```

- requests
- cloudscraper
- fake_useragent

## Usage/Examples

With Default Configuration

```bash
python3 pwndpress.py
```

If you want to configure the request method, configure it in `requester.json`

**Request Configuration**

| Variable | Type    | Function                                           |
| :------- | :------ | :------------------------------------------------- |
| verify   | boolean | Verify SSL on request                              |
| redirect | boolean | Allow redirect response                            |
| timeout  | int     | Request timeout                                    |
| method   | string  | Request module `requests` or `cloudscraper`        |
| agent    | string  | User Agent on request `null` or your browser agent |

```json
{
  "verify": true,
  "redirect": true,
  "timeout": 10,
  "method": "requests",
  "agent": null
}
```
