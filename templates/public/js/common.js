$(document).ready(function(){

    $(".navbar-default a").click(function() {
        var elementClick = $(this).attr("href")
        var destination = $(elementClick).offset().top;
        jQuery("html:not(:animated),body:not(:animated)").animate({
            scrollTop: destination
        }, 800);
        return false;
    });

    if ($('#video-gallery').length > 0)
    $('#video-gallery').lightGallery();

    if ($('.owl-carousel').length > 0)
        $('.owl-carousel.modal-carousel').owlCarousel({
            loop:false,
            margin:100,
            item: 2,
            dots: true,
            nav: true,
            autoplay: false,
            autoplayTimeout: 2000,
            smartSpeed: 1200,
            responsive:{
                0:{
                    items:1
                },
                600:{
                    items:1
                },
                1000:{
                    items:2
                }

            }
        });

    if ($('.owl-carousel').length > 0)
    $('.owl-carousel.partners-owl').owlCarousel({
        loop:true,
        margin:10,
        dots: true,
        nav: true,
        autoplay: false,
        autoplayTimeout: 2000,
        smartSpeed: 1200,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:3
            },
            1000:{
                items:5
            }
        }
    });

    if ($('.owl-carousel').length > 0)
    $('.owl-carousel.about-us').owlCarousel({
        loop:true,
        margin:10,
        dots: true,
        autoplay: false,
        autoplayTimeout: 2000,
        smartSpeed: 1200,
        // animateOut: 'fadeOut',
        nav:false,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:1
            },
            1000:{
                items:1
            }
        }
    });

    if ($('.owl-carousel').length > 0)
    $('.owl-carousel').owlCarousel({
        loop:true,
        margin:10,
        slideBy: 1,
        dots: true,
        autoplay: true,
        autoplayTimeout: 4000,
        autoplaySpeed:1000,
        smartSpeed: 1000,
        singleItem: true,
        // animateOut: 'fadeOut',
        nav:false,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:1
            },
            1000:{
                items:1
            }
        }
    });

    if ($('.news-revius .right-side .title p').length > 0)
        $('.news-revius .right-side .title p').readmore({
            collapsedHeight: 60,
            speed: 500,
            moreLink: '<a class="see-more" href="#">прочитать полностью</a>',
            lessLink: '<a class="see-more b" href="#">cкрыть</a>'
        });
});