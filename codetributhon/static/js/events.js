/**
 * Created by willkoua on 16-08-26.
 */

$(function(){

   var url = "";
   var codetriUrl = "http://codetributhon.com";

   //partager sur facebook
    $('.share_fb').on('click', function (e){
        e.preventDefault();

//        url=$(this).data('url');
        url=codetriUrl + $(this).data('url')
        var share_url = "https://www.facebook.com/sharer/sharer.php?u="+ encodeURIComponent(url) +"&amp;src=sdkprepars";

        sharePopupCenter(share_url, "Partagez sur Facebook1");
    });

    //partage sur twitter
    $('.share_tw').on('click', function (e) {
        e.preventDefault();

        url=codetriUrl + $(this).data('url')
        var share_url = "https://twitter.com/intent/tweet?&url="+ encodeURIComponent(url) +"&via=codetributhon2016"

        sharePopupCenter(share_url, "Partagez sur twitter");
    });
    
    //partage sur linkedin
    $('.share_lkdin').on('click', function (e) {
        e.preventDefault();

//        url=$(this).data('url')
        url=codetriUrl + $(this).data('url')
        var share_url = "https://www.linkedin.com/shareArticle?url="+ encodeURIComponent(url)

        sharePopupCenter(share_url, "Partagez sur linkedin");
    });


});

function sharePopupCenter(share_url, title, width, height) {
    var popupwidth = width || 320;
    var popupheight = height || 640;

    var top = window.screenTop || window.screenY;
    var left = window.screenLeft || window.screenX;
    var windowwidth = window.innerWidth || window.clientwidth;
    var windowheight = window.innerHeight || window.clientheight;


    var popupleft = left +windowwidth / 2 - popupwidth / 2;
    var popuptop= top +windowheight / 2 - popupheight / 2;

    window.open(share_url, title, "width="+ popupwidth +", height="+ popupheight +", top="+ popuptop +", left= "+popupleft  )
}

