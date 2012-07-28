%rebase base title=u'首页'
%from utils import wiki2html, get_month_name, get_day
%for blog in blogs:
<section class="article-list">

<div class="post_header">
    <div class="post_date">
        {{ get_day(blog['created_time']) }}<span>{{ get_month_name(blog['created_time']) }}</span>
    </div>
    <h1><a href="/post/{{blog['id']}}">{{ blog['title'] }}</a></h1>
</div>
<address class="post_infos">
<a href="#" class="label">Java</a><a class="label" href="#">Python</a><a class="label" href="#">编程</a>
</address>
{{!wiki2html(blog['content'][:100])}}
<p><a class="btn" href="/post/{{ blog['id'] }}">View details &raquo;</a></p>
</section>
%end
