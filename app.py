from flask import Flask,redirect,url_for,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return ('Hello World')

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
        # user=request.form('nm')
        user=request.form.get('nm')                  #当前目录下login_html提交表单实现该功能

        return redirect(url_for('success',name=user))
    else:
        user=request.args.get('nm')
        return redirect(url_for('success',name=user))

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name



if __name__ == '__main__':
    app.debug = True
    app.add_url_rule('/x',view_func=hello_world)


    app.run()