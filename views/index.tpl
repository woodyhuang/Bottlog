%rebase base title=u'首页'
<div>
    <h1>欢迎访问我的博客</h1>
    <a href="/post">发布新文章</a>
</div>
<ul style="border: 1px solid #ccc;">
    %for blog in blogs:
    <li>
	标题:<a href="/post/{{blog['id']}}">{{blog['title']}}</a><br/>
	创建时间:{{blog['created_time']}} <br/>
	摘要: {{blog['content'][:50]}} ...
    </li>
    %end
</ul>