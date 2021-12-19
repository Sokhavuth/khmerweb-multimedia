//asset/js/paginate.js
var page = 0

function paginate(route){
    $('.load-more img').attr('src', '/static/images/loading.gif')
    page += 1
    
    $.get(`/dashboard/${route}/paginate/${page}`, function(data, status){
        appendItem(data.items, route)
    })
}

function appendItem(items, route){
    var html = ''
    
    if(items){
        for(var item in items){
            html += `<div class='item'>`
            html += `<a href="/${route}/${items[item][3]}"><img class='thumb' src="${items[item][1]}" /></a>`
            html += `<div class='wrapper'>`
            html += `<a href="/${route}/${items[item][3]}">${items[item][0]}</a>`
            html += `<p class='date'></p>`
            html += `<script>`
            html += `$('.items .item .date').html(new Date("${items[item][2]}").toLocaleDateString())`
            html += `</script>`
            html += `</div>`
            html += `<div class='icon'>`
            html += `<a href='/dashboard/${route}/edit/${items[item][3]}'><img src='/static/images/edit.png' /></a>`
            html += `<a href='/dashboard/${route}/delete/${items[item][3]}'><img src='/static/images/delete.png' /></a>`
            html += `</div>`
            html += `</div>`
        }
    }
    $('.items').append(html)
    $('.load-more img').attr('src', '/static/images/load-more.png')
}
