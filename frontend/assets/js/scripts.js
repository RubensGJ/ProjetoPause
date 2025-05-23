$(document).ready(function(){
	$('#action_menu_btn').click(function(){
		$('.action_menu').toggle();
	});
});
$(document).ready(function() {
    $('#night-mode-btn').on('click', function() {
        $('body').toggleClass('night-mode');
        $('.card').toggleClass('night-mode');
        $('.contacts_body').toggleClass('night-mode');
        $('.msg_card_body').toggleClass('night-mode');
        $('.input-group-text').toggleClass('night-mode');
        $('.btn-outline-primary').toggleClass('night-mode');
    });
});