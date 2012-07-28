%rebase base title=u'首页'
%for blog in blogs:
<section class="article-list">

<div class="post_header">
    <div class="post_date">
        26<span>OCT</span>
    </div>
    <h1><a href="/post/{{blog['id']}}">{{ blog['title'] }}</a></h1>
</div>
<address class="post_infos">
%#{{ blog['created_time'] }}
<a href="#" class="label">Java</a><a class="label" href="#">Python</a><a class="label" href="#">编程</a>
</address>
<p>{{ blog['content'][:100] }}...</p>
<p><a class="btn" href="/post/{{ blog['id'] }}">View details &raquo;</a></p>
</section>
%end
