%# -*- coding: utf-8 -*-
%rebase base title=u'发布新文章'
<form action="/post" method="POST">
<fieldset>
<legend>请填写文章内容</legend>
<p>标题<input type="text" name="title"/></p>
<p>内容<textarea name="content" rows=6></textarea></p>
<p><button type="submit">提交</button></p>
</fieldset>
</form>