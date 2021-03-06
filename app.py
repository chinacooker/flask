from flask import Flask,redirect,url_for,request,render_template,make_response,escape,session

# Flask Request对象
# Form - 它是一个字典对象，包含表单参数及其值的键和值对。
# args - 解析查询字符串的内容，它是问号（？）之后的URL的一部分。
# Cookies  - 保存Cookie名称和值的字典对象。
# files - 与上传文件有关的数据。
# method - 当前请求方法
app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/user/<name>')   #动态路由
def hello_name(name):
    if name=='admin':
        return redirect(url_for('hello_admin'))  #会重定向到hello_admin对应的route，返回也是对应route的返回
    else:
        return ('Hello guest %s'%(name))
@app.route('/Admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/helloint/<int:x>')   #动态路由,限制int
def hello_int(x):
    return ('Hello %s'%(x))


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        user=request.form.get('nm')                  #当前目录下login_html提交表单实现该功能
                                                #post用request.form.get

        return redirect(url_for('success',name=user))
    else:
        user=request.args.get('nm')
        return redirect(url_for('success',name=user))

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route("/tm/<user>")
def tm(user):
    return render_template("tm.html",name=user)    #从templates里面找html文件；传参

@app.route('/sc/',methods=["get"])
def sc():
    score=request.args['score']                 #get用request.args
    return render_template('sc.html', marks = int(score))

@app.route('/result/',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form   #可以直接当字典来操作
        return render_template("result.html", result=result)
    else:
        dict = {'phy': 50, 'che': 60, 'maths': 70}
        return render_template('result.html', result=dict)

@app.route('/setcookie',methods=['POST','GET'])
def setcookie():
    if request.method=='POST':
        user =request.form.get('nm')
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)

        return resp
    else:
        return 'Hello get'
@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return ('welcome userID: %s '%name)





@app.route('/new')
def indexnew():
    if 'username' in session:
        username = session.get('username')
        return render_template("loged.html",name=username)
    else:
        return render_template('notloged.html')
@app.route('/loginnew',methods=['POST','GET'])
def loginnew():
    if request.method=='POST':
        session['username'] = request.form.get('username')
        username = session.get('username')
        return render_template("loged.html",name=username)
    else:
        return render_template("loginnew.html")
@app.route('/logoutnew')
def logoutnew():
    session.pop('username',None)
    return redirect(url_for('indexnew'))


if __name__ == '__main__':
    app.debug = True
    app.secret_key = '123456'

    app.add_url_rule('/x',view_func=hello_world)


    app.run()