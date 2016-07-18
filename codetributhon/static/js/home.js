/**
 * Created by willy on 2016-06-16.
 */


$(function(){

    $('#slider-wrapper').backstretch([
        "../static/img/bg/1.jpeg",
        "../static/img/bg/2.jpg",
        "../static/img/bg/3.jpg"
    ], {duration: 3000, fade: 750});

    $('.carousel').carousel({
        pause: "null"
    })

});
