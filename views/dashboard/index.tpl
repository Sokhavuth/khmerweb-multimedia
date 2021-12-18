<!--views/dashboard/index.tpl-->
% rebase('base.tpl')

<link href="/static/styles/partials/header.css" rel="stylesheet"></link>
<script src="/static/scripts/paginate.js"></script>
<section class='Head'>
    <header class='region'>
        <div class='site-logo'>{{ data['siteLogo'] }}</div>

        <form action='/dashboard/search' method='post'>
            <select name="select">
                <option>ការផ្សាយ</option>
                <option>ជំពូក</option>
                <option>សៀវភៅ</option>
                <option>អ្នក​ប្រើប្រាស់</option>
            </select>
            <input type='text' name="q" placeholder="Search" required />
            <input type="submit" value='បញ្ជូន'​ />
        </form>

        <div class='logout'><a href='/dashboard/logout'>ចេញ​ក្រៅ</a></div>
    </header>
</section>

<link href="/static/styles/partials/body.css" rel="stylesheet"></link>
<section class='Body region'>
    %include('dashboard/menu.tpl')

    <%
    if 'post' in data['route']:
        include('dashboard/post.tpl')
    elif 'category' in data['route']:
        include('dashboard/category.tpl')
    elif 'book' in data['route']:
        include('dashboard/book.tpl')
    elif 'upload' in data['route']:
        include('dashboard/upload.tpl')
    elif 'user' in data['route']:
        include('dashboard/user.tpl')
    end
    %>
</section>

<link href="/static/styles/partials/listing.css" rel="stylesheet"></link>
<section class='Listing region'>
    %if 'count' in data:
        <div class='info'>សរុប​ទាំងអស់​​មាន​ចំនួនៈ {{data['count']}}</div>
    %else:
        <div class='info'>សរុប​ទាំងអស់​​មាន​ចំនួនៈ</div>
    %end

    <div class='items'>
        %if 'items' in data:
        %for item in data['items']:
            <div class='item'>
                %if data['route'] == 'user':
                <style>
                .Listing .items .item{
                    grid-template-columns: 13% auto 20%;
                }
                .Listing .items .item .thumb{
                    border-radius: 50%;
                }
                </style>
                %end
                <a href="/{{data['route']}}/{{item[3]}}"><img class='thumb' src="{{item[1]}}" /></a>
               

                <div class='wrapper'>
                    <a href="/{{data['route']}}/{{item[3]}}">{{item[0]}}</a>
                    <p class='date'></p>
                    <script>
                        $('.items .item .date').html(new Date("{{item[2]}}").toLocaleDateString()) 
                    </script>
                </div>
                
                <div class='icon'>
                    <a href='/dashboard/{{data["route"]}}/edit/{{item[3]}}'><img src='/static/images/edit.png' /></a>
                    <a href='/dashboard/{{data["route"]}}/delete/{{item[3]}}'><img src='/static/images/delete.png' /></a>
                </div>
            </div>
        %end
        %end
    </div>

    <script>
        var route = "{{data['route']}}"
    </script>

    <div class='load-more'><img onclick='paginate(route)' src="/static/images/load-more.png" /></div>
</section>