<!--views/frontend/search.tpl-->

<link href="/static/styles/frontend_post.css" rel="stylesheet"></link>
<link href="/static/styles/partials/front_menu.css" rel="stylesheet"></link>

<section class='Random-thumb region'>
    %if 'posts' in data:
    <div class='wrapper'>
    %for v in range(len(data['posts'])):
        <div class='thumb'>
            <a href='/post/{{data["posts"][v]["id"]}}'>
                <img src='{{data["posts"][v]["thumb"]}}' />
            </a> 
        </div>
    %end
    </div>

    <div class="reload">
        <a href='/'><img src="/static/images/left.png" /></a>
        <a href='/'><img src="/static/images/home.png" /></a>
        <a href='/'><img src="/static/images/right.png" /></a>
    </div>
    %end

    
</section>