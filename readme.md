# pirate
a mvc restful api framework

### ⏬  Install
still in development, you can install from source

    $ git clone https://github.com/neo1218/pirate && cd pirate
    $ virtualenv pirate-ship && source pirate-ship/bin/activate
    $ pip install --editable .

[packages]: <br>
❌src.cli; ❌src.jsonify; ❌src.orm; ✅src.pirate; ✅src.route

### 📝  Document
#### wiki
+ [pirate-wiki](https://github.com/neo1218/pirate/wiki)

### 💻  Features
#### (M)orm
+ **sql**: [pirate-orm](https://github.com/neo1218/pirate/tree/master/src/orm)
+ **nosql**: [mongokit](https://github.com/namlook/mongokit)

#### (V)route
+ [pirate-route](https://github.com/neo1218/pirate/tree/master/src/route) <br/>
pirate的路由系统主要处理这些事情: 请求匹配、响应处理,
pirate的请求处理在wsgi内部创建greenlet local object:
```_request_ctx_hub``` 进行协程调度切换, 即```CoroutineLocal```模型.
相比于传统的```ThreadLocal```, 协程更加的轻量, 支持的并发连接数更高. <br/>
**pirate的route系统和flask的route系统对比** <br/>
为了尽可能保证测试的一致性, 我使用单文件的flask框架[flask.py](https://github.com/neo1218/pirate/blob/master/examples/compares/compare_with_flask/flask.py),
并且将内置```run_simple```服务器替换为```gevent WSGIServer```,
并打上monkey_patch. <br/>
+ [测试源码](https://github.com/neo1218/pirate/tree/master/examples/compares/compare_with_flask)
+ [测试结果] ![result](http://7xj431.com1.z0.glb.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202016-07-06%20%E4%B8%8A%E5%8D%8812.45.30.png)
#### (V)jsonify
+ [marshmallow](https://github.com/marshmallow-code/marshmallow)

#### (C)cli
+ [pirate-cli](https://github.com/neo1218/pirate/tree/master/src/cli)

### 📄  License
[MIT], check [License file] for more detail
