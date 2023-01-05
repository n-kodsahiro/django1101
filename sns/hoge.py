{% extends 'sns/layout.html' %}

{% block title %}Index{% endblock %}

{% block header %}
<script>
function sendGroupForm(page) {
    document.group_form.action += page;
    document.group_form.submit();
}
</script>
<h1 class="display-4 text-primary">SNS</h1>
<p>※グループのチェックをONにしてupdateすると、
そのグループに登録されている利用者のメッセージだけが表示されます。</p>
{% if messages %}
<ul class="messages">
    {% for message in messages %}
    <li{% if message.tags %} 
        class="{{ message.tags }}"
        {% endif %}>{{ message }}</li>
    {% endfor %}
</ul>
{% endif %}
{% endblock %}

{% block content %}
<hr>
<div>
    <form action="{% url 'index' %}" method="post" name="group_form">
        {% csrf_token %}
        {{check_form}}
        <div>
            <button class="btn btn-primary">update</button>
        </div>
    </form>
</div>
<table class="table mt-3">
    <tr><th>Messages</th></tr>
{% for item in contents %}
    <tr><td>
    <p class="my-0">
        {% if item.group.title == 'public' %}
        <span class="bg-info text-light px-1">Public</span>
        {% endif %}
        {{item.content}}</p>
    <p class=""> ({{item.pub_date}})</p>
    {% if item.share_id > 0 %}
    <ul><li class="text-black-50">"{{item.get_share}}"</li></ul>
    {% endif %}
    <span class="float-left text-info">
        share={{item.share_count}} good={{item.good_count}}
    </span>
    <span class="float-right">
        "{{item.owner}}"(<a href="{% url 'add' %}?name={{item.owner}}">
            add friend</a>)
        <a href="{% url 'share' item.id %}">
            <button class="py-0">share</button></a>
        <a href="{% url 'good' item.id %}">
            <button class="py-0">good!</button></a>
    </span>
</td></tr>
{% endfor %}
</table>

<ul class="pagination justify-content-center">
    {% if contents.has_previous %}
    <li class="page-item">
        <a class="page-link" href="javascript:sendGroupForm(1);">
            &laquo; first</a>
    </li>
    <li class="page-item">
        <a class="page-link" 
        href="javascript:sendGroupForm({{contents.previous_page_number}});">
            &laquo; prev</a>
    </li>
    {% else %}
    <li class="page-item">
        <a class="page-link">&laquo; first</a>
    </li>
    <li class="page-item">
        <a class="page-link">&laquo; prev</a>
    </li>
    {% endif %}
    <li class="page-item">
        <a class="page-link">
        {{contents.number}}/{{contents.paginator.num_pages}}</a>
    </li>
    {% if contents.has_next %}
    <li class="page-item">
        <a class="page-link" 
        href="javascript:sendGroupForm({{contents.next_page_number }});">
            next &raquo;</a>
    </li>
    <li class="page-item">
        <a class="page-link" 
        href="javascript:sendGroupForm({{contents.paginator.num_pages}});">
            last &raquo;</a>
    </li>
    {% else %}
    <li class="page-item">
        <a class="page-link">next &raquo;</a>
    </li>
    <li class="page-item">
        <a class="page-link">last &raquo;</a>
    </li>
    {% endif %}
</ul>
{% endblock %}

