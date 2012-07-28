%rebase base title=blog['title']
<div class="well">
    <h1>{{blog['title']}}</h1>
    
    <address class="post_infos">
                            发表于{{ blog['created_time'] }}(UTC+08)，
        &nbsp;
                            所属标签<a href="#" class="label">Java</a><a class="label" href="#">Python</a><a class="label" href="#">编程</a>
    </address>
    <hr/>
    <p>
    %from utils import wiki2html
    {{!wiki2html(blog['content'])}}
    <p>
</div>
<p>
<!--     msg: {{msg}} -->
<!--     <br/> -->
<!--     _msg: {{_('test i18n in tpl')}} -->
    <br/>
    除非注明，本站文章均为原创或编译，转载请注明： 文章来自Wenchen.me
</p>
