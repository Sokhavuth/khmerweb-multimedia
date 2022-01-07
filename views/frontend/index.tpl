<!--views/frontend/front.tpl-->
% rebase('base.tpl')

<link href="/static/styles/partials/header.css" rel="stylesheet"></link>
<script src="/static/scripts/paginate.js"></script>
<section class='Head'>
    <header class='region'>
        <div class='site-logo'>{{ data['pageTitle'] }}</div>

        <form action='/backend/search' method='post'>
            <select name="select">
                <option>ការផ្សាយ</option>
                <option>សៀវភៅ</option>
                
            </select>
            <input type='text' name="q" placeholder="Search" required />
            <input type="submit" value='បញ្ជូន'​ />
        </form>

        <div class='logout'><a href='/login'>ចូល​ក្នុង</a> | <a href='/login/register'>ចុះ​ឈ្មោះ</a></div>
    </header>
</section>

<link href="/static/styles/partials/frontend_body.css" rel="stylesheet"></link>
<section class='Body region'>
    
    %#include('frontend/menu.tpl')

    <%
    if 'front' in data['route']:
        include('frontend/front.tpl')
    end
    %>

</section>