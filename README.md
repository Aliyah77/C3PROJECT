# Email Header Analyzer

**Author:** Aliyah Ibrahim  
**Version:** 2025-June-29  
**Bootcamp:** Cyber Security Bootcamp – CCUBED

---

## 🧠 Project Overview

The Email Header Analyzer is a Python-based CLI tool that analyzes raw email headers to determine the credibility of an email using three authentication mechanisms:

- **SPF** (Sender Policy Framework)
- **DKIM** (DomainKeys Identified Mail)
- **DMARC** (Domain-based Message Authentication, Reporting & Conformance)

This tool can help detect spoofing and phishing attempts by verifying these components and generating a credibility score.

---

## ✨ Features

- ✅ Supports input via text file or pasted header  
- ✅ Extracts SPF, DKIM, and DMARC results  
- ✅ Color-coded console output using `colorama`  
- ✅ Calculates credibility score (out of 100)  
- ✅ Supports multiple headers in a single session  
- ✅ Saves results in a timestamped `.txt` report file

---

## ⚙️ Prerequisites

- Python 3.8+
- `colorama` library

### 📦 Installation

1. Clone or download the repository  
2. Install the required package:

```bash
pip install -r requirements.txt

```
or manually install by:
```bash
pip install colorama
```
## How To Use
Run the program using:
```bash
python email_header_analyzer.py
```
Then follow the on-screen prompts:

1. Select the Analyze Header(s) option by entering in 1.
![Input1](Images/Input1.jpeg)
2. Select whether to paste the email header or read it from a file.
![Input2](Images/Input2.jpeg)
3. If reading from a file, provide the filename (with or without path).
![Input3](Images/Input3.jpeg)
4. If you have multiple headers, separate them using the keyword #NEXT#.
    Email header 1 info---
    #NEXT#
    Email header 2 info---
### Sample Input File

#NEXT#

email header 2 info...
### Sample OutPut
![sample_output](Images/sample_output.jpeg)
## Licence
MIT License

Copyright (c) [2025] [Aliyah Ibrahim Oyinkansola]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



## Author
**Aliyah Ibrahim O.**
Computer Science Enthusiast & Mechanical Engineering Student

