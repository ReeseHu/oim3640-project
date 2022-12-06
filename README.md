# Project Overview
## Team members
Sabrina Chen, Reese Hu, Hanlu Ma
## Big Idea of the Project
Our project is creating a personality test website that asks the audience to answer a series of multiple choice questions, and returns the result of the corresponding personality type, and provides the interpretations to different personality types.

The personality test is a very intriguing topic lately. It is often used in psychology to help refine diagnoses as well as in business to assess potential candidates and help build cohesive teams. In terms of  the technicality, we believe that we can integrate what we learned in class about python coding and web design into the process of creation, thus deepen out understanding of python.

## Main Features
Home Page:  The home page includes the instruction of taking the personality test and 12 multiple choice questions. Users can freely fill out their choices for every question.

Result Page: The result page will include a specific personality type based on your selections to the questions in the homepage. Also, the result page will exhibit a detailed interpretation about the personality type shown.

Error Page: The error page will appear as the users forget to answer one or more questions in the homepage. The error page also includes a hyperlink to the home page for the convenience of the test takers. Specifically, after the error page pops up, by clicking "Home Page", the website will redirect to the home page again with a series of questions.

## Library
```
from flask import Flask, render_template, request
```
## How to Run the Code
1. Open Command Prompt and type "pip install flask" if you have not installed before.
2. Access our github repository at https://github.com/ReeseHu/oim3640-project
3. Go to test.py and open it up in Visual Studio Code, then run it.
4. Open up the link (http://127.0.0.1:5000) appears in the terminal and take the test.
5. You would notice a website page like the following pops up on your computer. Follow the instruction on the website and take the personality test.


