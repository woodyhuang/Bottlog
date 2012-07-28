%rebase base title=u'发布新文章'
<form action="/post" method="POST">
    <fieldset>
        <legend>请填写文章内容</legend>
        <div class="control-group">
            <label class="control-label" for="id_title">标题</label>
            <div class="controls">
              <input type="text" class="span5" id="id_title" name="title" value="{{blog['title']}}">
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="id_content">标题</label>
            <div class="controls">
              <textarea class="span8" id="id_content" name="content" rows="15">{{blog['content']}}</textarea>
              <p class="help-block">编辑内容请用WIKI格式</p>
            </div>
        </div>
        <div class="form-actions">
            <button type="submit" class="btn btn-primary">提交</button>
            <button class="btn">取消</button>
          </div>
    </fieldset>
    <input type="hidden" name="id" value="{{blog['id']}}"/>
</form>