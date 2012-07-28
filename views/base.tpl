%# -*- coding: utf-8 -*-
<!DOCTYPE html>
<html lang="zh">
    <head>
        <meta charset="utf-8">
        <title>{{ title or u'我的博客 ' }}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="">
        
        <link href="/static/bootstrap/bootstrap.css" rel="stylesheet">
        <style>
            body {
                padding-top: 80px;
                /* 60px to make the container go all the way to the bottom of the topbar */
                /* bootstrap-responsive.css will rewrite it to 0 */
            }
        </style>
        <link href="/static/bootstrap/bootstrap-responsive.css" rel="stylesheet">
        <link href="/static/wenchen.css" rel="stylesheet">
        
        <!--[if lt IE 9]>
          <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
        <![endif]-->
        
        <!-- Le fav and touch icons -->
        <!--
        <link rel="shortcut icon" href="assets/ico/favicon.ico">
        <link rel="apple-touch-icon-precomposed" sizes="144x144" href="assets/ico/apple-touch-icon-144-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="114x114" href="assets/ico/apple-touch-icon-114-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="72x72" href="assets/ico/apple-touch-icon-72-precomposed.png">
        <link rel="apple-touch-icon-precomposed" href="assets/ico/apple-touch-icon-57-precomposed.png">
        -->
    </head>
    <body>
        <nav class="navbar navbar-fixed-top">
          <div class="navbar-inner">
            <div class="container">
              <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </a>
              <a class="brand" href="#">Woody</a>
              <div class="nav-collapse">
                <ul class="nav">
                  <li class="active"><a href="/">主页</a></li>
                  <li><a href="/about">关于</a></li>
                </ul>
              </div><!--/.nav-collapse -->
            </div>
          </div>
        </nav>
    
        <div class="container">
            <div class="row">
                <article class="span9">
                    %include
                </article>
                <aside class="span3">
                    <a href="/post">发布新文章</a>
                </aside>
            </div>
            <hr/>
            <footer class="footer">
                &copy;2012 All Rights Opened.
            </footer>
        </div>
        <!-- Placed at the end of the document so the pages load faster -->
        <script src="/static/jquery-1.7.2.min.js"></script>
        <script src="/static/bootstrap/bootstrap.js"></script>
    </body>
</html>