%# -*- coding: utf-8 -*-
%rebase base title=blog['title']
<a href="/post">发布新文章</a>
<h1>{{blog['title']}}</h1>
{{blog['created_time']}}
<hr/>
<div style="boder:1px solid #ccc;">
{{blog['content']}}
</div>