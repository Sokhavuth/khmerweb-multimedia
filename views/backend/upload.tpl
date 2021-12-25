<!--views/dashboard/upload.tpl-->
<link href='/static/styles/category.css' rel='stylesheet' />

<section class='Category'>
    %if 'uploaded' in data:
    <form action='/dashboard/upload' method='post' enctype="multipart/form-data">
        <a>តំណរភ្ជាប់ៈ</a>
        <input type='text' name="link" value='{{data["url"]}}' required />
        <script>
            $("input[type='text']").on("click", function () {
                $(this).select();
            });
        </script>
    </form>
    %else:
    <form action='/dashboard/upload' method='post' enctype="multipart/form-data">
        <a></a><input type='file' name="upload" required />
        <a></a><input type='submit' value='Upload' />
    </form>
    %end
</section>