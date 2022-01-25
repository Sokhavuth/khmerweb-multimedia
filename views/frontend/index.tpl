<!--views/frontend/front.tpl-->
% rebase('base.tpl')

<script>
    var fb_api = false;
    window.fbAsyncInit = function(){
        fb_api == true
    };
</script>
<div id="fb-root"></div>
<script async defer src="https://connect.facebook.net/km_KH/sdk.js#xfbml=1&version=v3.2"></script>

<link href="/static/styles/partials/header.css" rel="stylesheet"></link>

<section class='Head'>
    <header class='region'>
        <div class='site-logo'>{{ data['pageTitle'] }}</div>

        <form action='/search' method='post'>
            <select name="select">
                <option>ភាពយន្ត</option>
                <option>សៀវភៅ</option>
                
            </select>
            <input type='text' name="q" placeholder="Search" required />
            <input type="submit" value='បញ្ជូន'​ />
        </form>

        <div class='logout'><a href='/login'>ចូល​ក្នុង</a> | <a href='/login/register'>ចុះ​ឈ្មោះ</a></div>
    </header>
</section>

<section class='Body region'>

    <%
    if 'front' in data['route']:
        include('frontend/front.tpl')
    elif 'post' in data['route']:
        include('frontend/post.tpl')
    elif 'search' in data['route']:
        include('frontend/search.tpl')
    end
    %>

</section>