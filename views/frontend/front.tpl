<!--views/frontend/front.tpl-->

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
        %if v == 4:
            %break
        %end
    %end
    </div>

    <div class="reload">
        <a href='/'><img src="/static/images/left.png" /></a>
        <a href='/'><img src="/static/images/home.png" /></a>
        <a href='/'><img src="/static/images/right.png" /></a>
    </div>

    <div class='Column'>
        <ul class=>
        %for v in range(5, len(data['posts'])): 
            <li>
                <a href='/post/{{data["posts"][v]["id"]}}'>
                    {{data["posts"][v]["title"]}}
                </a> 
            </li>
            %if v == 19:
                %break
            %end
        %end
        </ul>

        <ul>
            %for v in range(20, len(data['posts'])): 
                <li>
                    <a href='/post/{{data["posts"][v]["id"]}}'>
                        {{data["posts"][v]["title"]}}
                    </a> 
                </li>
                %if v == 34:
                    %break
                %end
            %end
        </ul>

        <ul>
            %for v in range(35, len(data['posts'])): 
                <li>
                    <a href='/post/{{data["posts"][v]["id"]}}'>
                        {{data["posts"][v]["title"]}}
                    </a> 
                </li>
            %end
        </ul>
    </div>
    %end
</section>