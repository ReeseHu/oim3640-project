from flask import Flask, render_template, request
from quiz import display

import sys
import os
app = Flask(__name__)

quiz_host = os.environ.get('FLASK_HOST')
quiz_port = os.environ.get('FLASK_PORT')

questions = [
        {
        "Question 1:":
        "Interacting with strangers?",
        "a.": "Wears me out",
        "b.": "Energizes me"},
        

        {
        "Question 2:":
        "With people are you usaully more?",
        "a.": "Firm than gentle",
        "b.": "Gentle than firm"}
        ,
        
        {
        "Question 3:":
        "You are more likely to enjoy?",
        "a.": "Team sports",
        "b.": "Individual sports"}
        ,

        {
        "Question 4:": 
        "Your decisions are based on?",
        "a.": "Logic & an outcome that makes sense",
        "b.": "Value & an outcome that feels right"}
        ,

        {
        "Question 5:":
        "What interests you more?",
        "a.": "What's in front of you",
        "b.": "What can be imagined"}
        ,

        {
        "Question 6:":
        "You pay particular attention to?",
        "a.": "Details, realities, past, and present",
        "b.": "Insights, patterns, and possibilities"}
        ,

        {
        "Question 7:":
        "It is worse to?",
        "a.": "Have your head in the clouds",
        "b.": "Perform the same routine every day"}
        ,


        {
        "Question 8:":
        "When considering a difficult choice involving people you are?",
        "a.": "fact based",
        "b.": "affected by the circumstances"}
        ,

        {
        "Question 9:":
        "When your cell phone rings do you?",
        "a.": "Answer it immediately",
        "b.": "Ignore it or check who is calling"}
        ,

        {
        "Question 10:":
        "You prefer you life to be?",
        "a.": "Organised and planned",
        "b.": "Flexible and Spontaneous"}
        ,
        
        {
        "Question 11:":
        "As a deadline approaches to you?",
        "a.": "Work in spurts to finish",
        "b.": "Work consistently to finish"}
        ,

        {
        "Question 12:":
        "Before the weekend you usually?",
        "a.": "Have plans made",
        "b.": "Hope to be spontaneous"
        }
]
    
    
@app.route("/quiz", methods=['POST', 'GET'])
def quiz():
    
    if request.method == 'GET':
        return render_template("homepage.html", data=questions)
    else:
        result = 0
        total = 0

    count_of_a: int = 0
    count_of_b: int = 0
    personality: str = ''
    count = 0

    for question in questions:
        answer = ''
        while not (answer == 'a' or answer == 'b'):
            count_of_a = 0
            count_of_b = 0
            try:
                answer = input(question).lower()
                if not (answer == 'a' or answer == 'b'):
                    raise ValueError("Invalid input")
            except ValueError as error:
                print(error)
        if answer == 'a':
            count_of_a = count_of_a + 1
        if answer == 'b':
            count_of_b = count_of_b + 1
        count = count + 1

        if count == 3:
            if count_of_a > count_of_b:
                personality = personality + 'E '
            else:
                personality = personality + 'I '
        else:
            if count == 6:
                if count_of_a > count_of_b:
                    personality = personality + 'S '
                else:
                    personality = personality + 'N '
            else:
                if count == 9:
                    if count_of_a > count_of_b:
                        personality = personality + 'T '
                    else:
                        personality = personality + 'F '
                else:
                    if count == 12:
                        if count_of_a > count_of_b:
                            personality = personality + 'J '
                        else:
                            personality = personality + 'P '
    return render_template('result.html')
    









