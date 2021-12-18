<!--views/dashboard/post.tpl-->
<link rel='stylesheet' href='/static/styles/post.css' />
<script src="/static/scripts/ckeditor/ckeditor.js"></script>
<script src="/static/scripts/video.js"></script>

<section class='Main'>
    <div class='content'>
        <form action='/dashboard/post' method='post' >
            %if 'edit' in data:
            <input type='text' name='title' value='{{data["item"][0]}}' placeholder='ចំណងជើង' required />
            <textarea name="content" id="editor" >{{data["item"][4]}}</textarea>
            <div class='wrapper'>
                <select name='category' class='category' >
                    %for category in data['categories']:
                        <option>{{ category[0] }}</option>
                    %end
                </select>
                <script>$(".category").val("{{data['item'][5]}}").change();</script>
                <input type='text' name='thumb' value='{{data["item"][1]}}' required placeholder="តំណរ​ភ្ជាប់​រូប​តំណាង" />
                <input type='datetime-local' value='{{data["item"][2]}}' name='datetime' required />
                <input type='hidden' name='editid' value='{{data["item"][3]}}' />
                <input type='submit' value='ចុះ​ផ្សាយ' />
            </div>
            <input name='entries' value='{{!data["item"][6]}}' type='hidden' />
            %else:
            <input type='text' name='title' placeholder='ចំណងជើង' required />
            <textarea name="content" id="editor" ></textarea>
            <div class='wrapper'>
                <select name='category'>
                    %for category in data['categories']:
                        <option>{{ category[0] }}</option>
                    %end
                </select>
                <input type='text' name='thumb' required placeholder="តំណរ​ភ្ជាប់​រូប​តំណាង" />
                <input type='datetime-local' value='' name='datetime' required />
                <input type='submit' value='ចុះ​ផ្សាយ' />
            </div>
            <input name='entries' value='' type='hidden' />
            %end
        </form>

        <div class='form'>
            <select name='type'>
                <option>YouTube</option>
                <option>YouTubePlaylist</option>
                <option>Facebook</option>
                <option>OK</option>
                <option>Dailymotion</option>
                <option>Vimeo</option>
            </select>
            <input name='id' type='text' placeholder="អត្តសញ្ញាណវីដេអូ" required />
            <select name='ending'>
                <option>ចប់​ហើយ</option>
                <option>មិន​ទាន់ចប់</option>
            </select>
            <input onclick='genJson()' type="button" value="បញ្ចូល​វីដេអូ" />
        </div>

        <table class='viddata'></table>
        
        %if 'edit' in data:
            <script>
                var entries = JSON.parse('{{!data["item"][6]}}')
            </script>
        %end

        <script>
        if(entries.length > 0){

            let html = ``
            for(let v in entries){
                episode += 1
                html += `<tr>`
                html += `<td title="Delete" onClick="deleteRow(event)" class="episode">${episode}</td>`
                html += `<td class="td${episode}">${entries[v].type}</td>`
                html += `<td class="td${episode}">${entries[v].id}</td>`
                html += `<td class="td${episode}">${entries[v].ending}</td>`
                html += `</tr>`
            }

            if($('.viddata').html() === ''){
                $('.viddata').append('<tr>')
                $('.viddata').append('<th>ភាគ/លុប</th>')
                $('.viddata').append('<th>ប្រភេទ​</th>')
                $('.viddata').append('<th>អត្តសញ្ញាណ​</th>')
                $('.viddata').append('<th>ចប់ឬ​នៅ?</th>')
                $('.viddata').append('</tr>')
            }

            $('.viddata').append(`${html}`)

        }
        </script>

        <script src="/static/scripts/ckeditor/config.js"></script>
    </div>
</section>