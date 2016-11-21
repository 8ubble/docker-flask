$(function(){
    $('.first h1').addClass('animated fadeInDown');
    $('.first h2').addClass('animated fadeInUp');
});

$(window).scroll(function() {
    var value = $(this).scrollTop();
    if (value > 80)
        $(".navbar").css("background", "#212121");
    else
        $(".navbar").css("background", "transparent");
});