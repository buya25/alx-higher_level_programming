# Project Readme: alx-higher_level_programming

## Introduction

This repository contains a collection of Bash scripts and a Python script for various network-related tasks and a Python script for finding peaks in unsorted integers.

## Bash Scripts

### 0-body_size.sh

This script takes a URL as input, sends a request to that URL using cURL, and displays the size of the response body in bytes. It must be tested using the web server running on port 5000.

```bash
./0-body_size.sh 0.0.0.0:5000
```

### 1-body.sh

This script takes a URL as input, sends a GET request to the URL using cURL, and displays the body of the response for a 200 status code only. It should be tested using the web server running on port 5000.

```bash
./1-body.sh 0.0.0.0:5000/route_1
```

### 2-delete.sh

This script sends a DELETE request to the URL passed as the first argument using cURL and displays the body of the response. It should be tested using the web server running on port 5000.

```bash
./2-delete.sh 0.0.0.0:5000/route_3
```

### 3-methods.sh

This script takes a URL as input and displays all HTTP methods the server will accept using cURL. It should be tested using the web server running on port 5000.

```bash
./3-methods.sh 0.0.0.0:5000/route_4
```

### 4-header.sh

This script takes a URL as an argument, sends a GET request to the URL using cURL with a specific header, and displays the body of the response.

```bash
./4-header.sh 0.0.0.0:5000/route_5
```

### 5-post_params.sh

This script takes a URL as input, sends a POST request to the URL using cURL with specific parameters, and displays the body of the response.

```bash
./5-post_params.sh 0.0.0.0:5000/route_6
```

## Python Script

### 6-peak.py

This Python script defines a function `find_peak` that finds a peak in a list of unsorted integers. The script includes a test script (`6-main.py`) that demonstrates the functionality of the `find_peak` function.

```python
./6-main.py
```

## Complexity

The complexity of the `find_peak` algorithm is documented in the file `6-peak.txt`.

```bash
wc -l 6-peak.txt
```

## Repository Information

- GitHub Repository: [alx-higher_level_programming](https://github.com/username/alx-higher_level_programming)
- Directory: 0x10-python-network_0
