<!--views/frontend/post.tpl-->

<link href="/static/styles/frontend_post.css" rel="stylesheet"></link>
<link href="/static/styles/partials/front_menu.css" rel="stylesheet"></link>
<script src='/static/scripts/setPlayer.js'></script>

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

    %if 'post' in data:
    <div class='player'>
        <div class='screen'>
            <div class='video-wrapper'>
                <iframe src="" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
            <div class='text-content'>{{!data['post']['content']}}</div>
        </div>

        <script>
            var entries = JSON.parse('{{!data["post"]["entries"]}}')
        </script>

        <div class='playlist'>
            %import json
            %entries = json.loads(data['post']['entries'])
            %ending = ''
            %for v in range(len(entries)):
            %if v == len(entries)-1:
                %ending = entries[v]['ending']
            %end
            <div onclick='setScreen(entries[{{v}}],{{v}},true)'>
                <div id='part{{v}}' class='video-part'>
                    {{data['post']['title']}} ភាគ {{v+1}} {{ending}}
                </div>
            </div>
            %end
            <script>
                setScreen(entries[0],0,false)
            </script>
        </div>
    </div>
    <div class='comment'>
        <div id="disqus_thread"></div>
            <script>
                var disqus_config = function () {
                    this.page.url = "https://khmerweb-multimedia.vercel.app/post/{{data['post']['id']}}";  
                    this.page.identifier = "{{data['post']['id']}}"; 
                };
    
                (function() { // DON'T EDIT BELOW THIS LINE
                    var d = document, s = d.createElement('script');
                    s.src = 'https://multimedia-9.disqus.com/embed.js';
                    s.setAttribute('data-timestamp', +new Date());
                    (d.head || d.body).appendChild(s);
                })();
            </script>
            <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">
                comments powered by Disqus.</a>
            </noscript>
    </div>
    %end
</section>