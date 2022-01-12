//asset/js/setPlayer.js

function setScreen(entry,id,click){
    if(entry['type'] == 'OK'){
        var url = `//ok.ru/videoembed/${entry['id']}`
    }else if(entry['type'] == 'YouTube'){
        var url = `https://www.youtube.com/embed/${entry['id']}`
    }else if(entry['type'] == 'YouTubePlaylist'){
        var url = `https://www.youtube.com/embed/videoseries?list=${entry['id']}`
    }

    if(click){
        $('.Random-thumb .player .playlist #part'+clicked)
            .css({'background':'lightgrey','color':'rgb(87, 87, 87)'})
    }
    $('.Random-thumb .player .playlist #part'+id)
        .css({'background':'var(--foreground)','color':'white'})
    $('.Random-thumb .player .screen iframe').attr('src', url)
    clicked = id
}

