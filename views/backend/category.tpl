<!--views/dashboard/category-->
<link href='/static/styles/category.css' rel='stylesheet' />

<section class='Category'>
    %if 'edit' in data:
    <form action='/dashboard/category' method='post'>
        <a>ឈ្មោះ​ជំពូកៈ</a><input type='text' value="{{data['item'][0]}}" name="name" required />
        <a>តំណរភ្ជាប់​រូបៈ</a><input type='text' value="{{data['item'][1]}}" name='link' required />
        <a>ពេល​បង្កើតៈ</a><input type='datetime-local' value="{{data['item'][2]}}" name='datetime' required />
        <a></a><input type='submit' value='បញ្ជូន' />
        <a></a><input type='hidden' value="{{data['item'][3]}}" name="editid" />
    </form>
    %else:
    <form action='/dashboard/category' method='post'>
        <a>ឈ្មោះ​ជំពូកៈ</a><input type='text' name="name" required />
        <a>តំណរភ្ជាប់​រូបៈ</a><input type='text' name='link' required />
        <a>ពេល​បង្កើតៈ</a><input type='datetime-local' name='datetime' required />
        <a></a><input type='submit' value='បញ្ជូន' />
    </form>
    %end
</section>