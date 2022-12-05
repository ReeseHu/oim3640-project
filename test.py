from flask import Flask, render_template, request
from quiz2 import run


app = Flask(__name__)

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

@app.route('/', methods=['POST','GET'])
def mbta_station():
    if request.method=='GET':
        return render_template('homepage.html')
    else:
        result_list=[]
        for question in questions:
            result_list.append(request.form[question.get])
            answer=run(result_list)
        return render_template('result.html',type=answer)
        # except IndexError:
        # # if the input is wrong or not in the database
        #     return render_template('error.html')

    return render_template('homepage.html')




if __name__ == '__main__':
    app.run(debug=True)

