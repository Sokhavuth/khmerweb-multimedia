<!--views/frontend/login.tpl-->
% rebase('base.tpl')
<link href="/static/styles/login.css" rel="stylesheet"></link>

<section>
    <header>​ចុះ​ឈ្មោះចូល​ទំព័រ​គ្រប់គ្រង</header>
    <form method="post" action="/login">
        <a>Email:</a><input type='email' name="email" value="" required />
        <a>ពាក្យ​សំងាត់ៈ</a><input type='password' name="password" value="" required />
        <a></a><input type='submit' value='បញ្ជូន' />
        <a></a><div>{{ data['message'] }}</div>
    </form>
</section>