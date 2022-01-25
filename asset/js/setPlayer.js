//asset/js/setPlayer.js

function setScreen(entry,id,click){
    if(entry['type'] == 'OK'){
        var url = `//ok.ru/videoembed/${entry['id']}`
    }else if(entry['type'] == 'YouTube'){
        var url = `https://www.youtube.com/embed/${entry['id']}`
    }else if(entry['type'] == 'YouTubePlaylist'){
        var url = `https://www.youtube.com/embed/videoseries?list=${entry['id']}`
    }else if(entry['type'] === "Facebook"){
        var url = `https://www.facebook.com/watch/?v=${entry['id']}`
    }

    if(entry['type'] !== 'Facebook'){
        var iframe = `<div>
        <iframe id="video-player" src="${url}" frameborder="0" allowfullscreen></iframe>
        </div>`;
      }else{
        var iframe = `<div class="fb-video" data-href="${url}" data-width="auto" data-show-captions="true"></div>`;
    }

    if(click){
        $('.Random-thumb .player .playlist #part'+clicked)
            .css({'background':'lightgrey','color':'rgb(87, 87, 87)'})
    }
    $('.Random-thumb .player .playlist #part'+id)
        .css({'background':'var(--foreground)','color':'white'})


    $('.Random-thumb .player .screen .video-wrapper').html(iframe)
    if((entry['type'] === "Facebook")&&(fb_api)){
        FB.XFBML.parse()
    }  
         
    fb_api == true
    clicked = id
}

