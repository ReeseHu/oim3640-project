from flask import Flask, render_template, request
from quiz2 import run


app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def mbta_station():
    if request.method=='POST':
        while True:
                result_list=[]
                for i in range(0,13):
                    result_list.append(request.form['question'+[i]])
                    answer=run(result_list)
                return render_template('result.html',type=answer)
            # except IndexError:
            # # if the input is wrong or not in the database
            #     return render_template('error.html')

    return render_template('homepage.html')




if __name__ == '__main__':
    app.run(debug=True)

