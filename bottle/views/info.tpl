<html>
    <head>
        <title>会员中心</title>
    <head>
    <body>
       <p><h2>会员信息</h2></p>
       如果tname后端有返回值，就显示出来</br>
       %if tname:
          姓名：{{tname}}</br>
       %end
       <p></p>

       也可以使用if else语句</br>
       %if tnum:
            tnum:{{tnum}}</br>
       %else:
            tnum没有定义</br>
       %end
       <p></p>

       也可以使用if xx == 'yy'语句</br>
       %if tage == '30':
            哈哈，你老了！</br>
       %else:
            你年轻吗？</br>
       %end

            <p>如果tnum没有定义，那就使用默认值666：{{get('tnum','666')}}</p>
            <p>QQ：{{get('tqq','111111')}}</p>
            <p>Email: {{get('temail','111@163.com')}}</p>

            所有的书名用for循环遍历：</br>
            %for col in tbook:
            {{col}}</br>
            %end

    </body>
</html>