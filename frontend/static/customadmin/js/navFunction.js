$(document).ready(function() {

    $("#iconShow").click(function() {
            // $(".openMenu").animate({opacity: '0.5'},'slow');
            $(".blurOnsidenavOn").fadeIn({duration: 500});
            $(".menuItems").css({opacity: '0'});
            $("#iconHide").css("opacity", 0);
            $(".openMenu").delay(60).animate({ left: '242px', opacity: 0 }, { duration: 300, easing: 'linear' });
            $("#sideNavContainerToggle").animate({ width: 'show' }, {duration: 300, easing: 'linear', complete: function() {
                        $(".openMenu").animate({ opacity: '0' }, {
                            complete: function() {
                                $(".openMenu").css('display', 'none');
                             }
                        });
                    $("#iconHide").animate({opacity: '1'},'slow');
                    $(".menuItems").animate({opacity: 1});
                }
            });

     });

    $("#iconHide").click(function() {
        $("#iconHide").animate({ opacity:0});
        $(".menuItems").animate({opacity: 0,right:'300px'},{duration:300,complete: function(){
            $(".openMenu").css('display', 'block');
            $(".openMenu").animate({opacity: 1,left:'0px'},{duration: 250});
            $("#sideNavContainerToggle").animate({ width: 'hide', },{duration: 300, easing: 'linear'});
            $(".blurOnsidenavOn").fadeOut({duration: 300});
        }});

    });


});