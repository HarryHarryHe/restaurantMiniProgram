=====================
##启动
* export ops_config=local|production && python manage.py runserver

##flask-sqlacodegen

    ## 记得输入密码
    flask-sqlacodegen 'mysql://root:password@127.0.0.1/food_db' --outfile "common/models/model.py"  --flask
    flask-sqlacodegen 'mysql://root:password@127.0.0.1/food_db' --tables user --outfile "common/models/User.py"  --flask
    flask-sqlacodegen 'mysql://root:password@127.0.0.1/food_db' --tables app_access_log --outfile "common/models/log/AppAccessLog.py"  --flask
    flask-sqlacodegen 'mysql://root:password@127.0.0.1/food_db' --tables app_error_log --outfile "common/models/log/AppErrorLog.py"  --flask