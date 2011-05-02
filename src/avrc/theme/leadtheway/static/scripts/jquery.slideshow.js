(function($){
	$(window).load(
		    function(){ //$(window).load() must be used instead of $(document).ready() because of Webkit compatibility
		        $("#slideshow").sliderkit({
		                autospeed:3000,
		                panelbtnshover:false,
		                circular:true
		        });
		        
		        $("#portaltab-manifesto a").click(
		            function (){
		                $("#manifesto-popup").css("display","block");
		                $(this).addClass("highlight");
		            }
		        );
		        $(".manifesto-close").click(
		            function () {
		                $(this).parent().css("display","none");
		                $("#portaltab-manifesto a").removeClass("highlight");
		            }
		        );
		        $("#manifesto-popup").click(
		            function () {
		                $(this).css("display","none");
		                $("#portaltab-manifesto a").removeClass("highlight");
		            }
		        );
		        
		        $('a.popup').fancybox({'padding':0});
		        $('.scroll-pane').jScrollPane();
		    }
		);
})(jQuery)
