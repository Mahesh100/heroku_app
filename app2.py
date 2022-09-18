from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/',methods=['POST', 'GET'])
def home():
    return render_template('1main.html')
    return render_template('1main.js')
    return render_template('1main.css')

@app.route('/category',methods=['POST', 'GET'])
def category():
    return render_template('2category.html')
    return render_template('style2.css')
    return render_template('script2.js')    
    
if __name__ == '__main__':
    #app.debug = True
    #app.run()
    app.run(debug=True)