(function($){
    $(window).load(function(){ //$(window).load() must be used instead of $(document).ready() because of Webkit compatibility
        $("#slideshow").sliderkit({
            autospeed:5000,
            panelbtnshover:false,
            circular:true
        });
    });
})(jQuery)
