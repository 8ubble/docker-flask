$(function(){
    $('.first h1').addClass('animated fadeInDown');
    $('.first h2').addClass('animated fadeInUp');
});

$(window).scroll(function() {
    var value = $(this).scrollTop();
    if (value > 80){
        $(".navbar").css("background", "#22222e");
    }
    else{
        $(".navbar").css("background", "transparent");
        $(".navbar").css("padding-bottom", "2px");    
    }

});