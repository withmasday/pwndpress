<h1 align="center">PwndPRESS</h1>

<p align="center">PwndPRESS Is An WordPress Theme/Plugins Exploiting Tool</p>

<div align="center">

[![All Contributors](https://img.shields.io/github/contributors/withmasday/pwndpress)](https://github.com/withmasday/pwndpress/graphs/contributors)
![GitHub last commit](https://img.shields.io/github/last-commit/withmasday/pwndpress.svg)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/withmasday/pwndpress)
[![License](https://img.shields.io/github/license/withmasday/pwndpress.svg)](LICENSE)

</div>

## Install Dependencies

**Python3**

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

**Settings Request Configuration**

| Variable | Type    | Function                                           |
| :------- | :------ | :------------------------------------------------- |
| verify   | boolean | Verify SSL on request                              |
| redirect | boolean | Allow redirect response                            |
| timeout  | int     | Request timeout                                    |
| method   | string  | Request module to use `requests` or `cloudscraper` |
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

## Exploit Reference Platform

- [ExploitDB](https://www.exploit-db.com/)
- [WPScan](https://wpscan.com/)
- [Packet Storm Security](https://packetstormsecurity.com/)
- [SploitUS](https://sploitus.com/)
- [0day.today](https://en.0day.today/webapps)

## Contributing

- Fork this repository [https://github.com/withmasday/pwndpress](https://github.com/withmasday/pwndpress)
- Create your branch `git checkout -b your-branch`
- Commit your changes `git commit -am 'Add some exploit'`
- Push to the branch `git push origin your-branch`
- Create a new Pull Request.

### Note

- You can add exploit files into the `lib` directory, place your exploits into a specific directory for example: `/lib/themes/RFU/exploitname.py`

- Don't forget add your exploit to `pwndpress.json` with format :

```json
{
  "name": "exploit name",
  "type": "theme",
  "file": "lib/themes/RFU/exploitname.py",
  "slug": "agritourismo-theme"
}
```
