# Project Readme

This project consists of a series of JavaScript scripts that perform various tasks related to file manipulation, web scraping, and API requests. The scripts adhere to specific requirements and coding standards. Below are the details and instructions for each script:

## General Requirements
- Editors: vi, vim, emacs
- Execution environment: Ubuntu 20.04 LTS using Node.js (version 14.x)
- File ending: All files should end with a new line
- Shebang: The first line of all files should be exactly `#!/usr/bin/node`
- README.md: A mandatory README file at the root of the project folder
- Code Style: Semistandard compliant with rules of Standard + semicolons on top, and using AirBnB style
- Executables: All files must be executable
- No use of `var`

## Getting Started
### Install Node 14
```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install Semistandard
```bash
$ sudo npm install semistandard --global
```

### Install Request Module
```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Scripts

### 0-readme.js
- Description: Reads and prints the content of a file in utf-8.
- Usage:
  ```bash
  $ ./0-readme.js <file_path>
  ```

### 1-writeme.js
- Description: Writes a string to a file in utf-8.
- Usage:
  ```bash
  $ ./1-writeme.js <file_path> "<string_to_write>"
  ```

### 2-statuscode.js
- Description: Displays the status code of a GET request to the provided URL using the `request` module.
- Usage:
  ```bash
  $ ./2-statuscode.js <url>
  ```

### 3-starwars_title.js
- Description: Prints the title of a Star Wars movie where the episode number matches the given integer using the Star wars API.
- Usage:
  ```bash
  $ ./3-starwars_title.js <movie_id>
  ```

### 4-starwars_count.js
- Description: Prints the number of movies where the character “Wedge Antilles” is present using the Star wars API.
- Usage:
  ```bash
  $ ./4-starwars_count.js <api_url>
  ```

### 5-request_store.js
- Description: Gets the contents of a webpage and stores it in a file using the `request` module.
- Usage:
  ```bash
  $ ./5-request_store.js <url> <file_path>
  ```

### 6-completed_tasks.js
- Description: Computes the number of tasks completed by user id using the provided API URL.
- Usage:
  ```bash
  $ ./6-completed_tasks.js <api_url>
  ```

Feel free to explore each script for more details and examples. For additional information, refer to the corresponding files in the project repository.
