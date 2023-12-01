# Project Readme: alx-higher_level_programming (0x11-python-network_1)

## Introduction

This repository contains a collection of Python scripts for various network-related tasks using the `urllib` and `requests` packages. The scripts perform actions such as fetching data from URLs, handling HTTP headers, sending POST requests, handling HTTP errors, and interacting with the GitHub API.

## Python Scripts

### 0-hbtn_status.py

This script fetches the status of [https://alx-intranet.hbtn.io/status](https://alx-intranet.hbtn.io/status) using the `urllib` package. It displays information about the response body, including its type, content, and utf-8 content.

```bash
./0-hbtn_status.py | cat -e
```

### 1-hbtn_header.py

This script takes a URL as input, sends a request to the URL using `urllib`, and displays the value of the X-Request-Id variable found in the header of the response.

```bash
./1-hbtn_header.py https://alx-intranet.hbtn.io
```

### 2-post_email.py

This script takes a URL and an email as input, sends a POST request to the URL with the email as a parameter, and displays the body of the response.

```bash
./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
```

### 3-error_code.py

This script takes a URL as input, sends a request to the URL using `urllib`, and displays the body of the response. It also handles `urllib.error.HTTPError` exceptions and prints the error code if the HTTP status code is greater than or equal to 400.

```bash
./3-error_code.py http://0.0.0.0:5000
./3-error_code.py http://0.0.0.0:5000/status_401
./3-error_code.py http://0.0.0.0:5000/doesnt_exist
./3-error_code.py http://0.0.0.0:5000/status_500
```

### 4-hbtn_status.py

This script fetches the status of [https://alx-intranet.hbtn.io/status](https://alx-intranet.hbtn.io/status) using the `requests` package. It displays information about the response body, including its type and content.

```bash
./4-hbtn_status.py | cat -e
```

### 5-hbtn_header.py

This script takes a URL as input, sends a request to the URL using `requests`, and displays the value of the X-Request-Id variable in the response header.

```bash
./5-hbtn_header.py https://alx-intranet.hbtn.io
```

### 6-post_email.py

This script takes a URL and an email as input, sends a POST request to the URL with the email as a parameter using `requests`, and displays the body of the response.

```bash
./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
```

### 7-error_code.py

This script takes a URL as input, sends a request to the URL using `requests`, and displays the body of the response. If the HTTP status code is greater than or equal to 400, it prints the error code.

```bash
./7-error_code.py http://0.0.0.0:5000
./7-error_code.py http://0.0.0.0:5000/status_401
./7-error_code.py http://0.0.0.0:5000/doesnt_exist
./7-error_code.py http://0.0.0.0:5000/status_500
```

### 8-json_api.py

This script takes a letter as input, sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter, and displays information based on the response.

```bash
./8-json_api.py a
```

### 10-my_github.py

This script takes GitHub credentials (username and personal access token) as input and uses the GitHub API to display the user's ID.

```bash
./10-my_github.py username token
```

### 100-github_commits.py

This script lists 10 commits (from most recent to oldest) of a specified repository by a given user using the GitHub API.

```bash
./100-github_commits.py repository_name owner_name
```

## Repository Information

- GitHub Repository: [alx-higher_level_programming](https://github.com/buya25/alx-higher_level_programming)
- Directory: 0x11-python-network_1
