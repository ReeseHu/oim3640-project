from flask import Flask, render_template, request
from helper import run, descrip


app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def display():
    if request.method=='POST':
        result_list=[]
        i=1
        for i in range(1,13):
            result_list.append(request.form.get(f'{i}'))
            personality = run(result_list).strip()
            answer=descrip(personality)
            i+=1
        return render_template('result.html',type=answer,personality_answer=personality)

    return render_template('homepage.html')


if __name__ == '__main__':
    app.run(debug=True)