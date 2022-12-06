from flask import Flask, render_template, request
from helper import run, descrip


app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def display():
    if request.method=='POST':
        result_list=[]
        i=1
        for i in range(1,13): # iterate from question 1 - 12 (all the questions) in the personality test
            result_list.append(request.form.get(f'{i}')) # request the answer the user selects for every question and append it to the result_list we created before.
        if None not in result_list: # if the user fills out every choice in the test, the website will return the result page with the personality trait and the corrresponding interpretation.
            personality = run(result_list).strip()
            answer=descrip(personality)
            return render_template('result.html',type=answer,personality_answer=personality)
        else: # if the user misses one or more question(s) in the test, the website will return to the error page with a hyperlink for the user's convenience to return to the original test page.
            return render_template('error.html')

    return render_template('homepage.html')


if __name__ == '__main__':
    app.run(debug=True)