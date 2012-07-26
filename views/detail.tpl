%# -*- coding: utf-8 -*-
%rebase base title=blog['title']
<a href="/post">发布新文章</a>
<h1>{{blog['title']}}</h1>
{{blog['created_time']}}
<hr/>
msg: {{msg}}
<hr/>
_msg: {{_('test i18n in tpl')}}
<hr/>
<div style="boder:1px solid #ccc;">
{{blog['content']}}
</div>