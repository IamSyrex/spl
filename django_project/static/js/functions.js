function thumbing() {
	jQuery('.thumb-it-up').click(function(e){
		var rId = jQuery(this).attr('data-toid');
		console.log(rId);
		var r = jQuery('#'+rId);
		console.log(r);
		jQuery(r).removeClass('green red');
		jQuery(r).addClass('red');
		jQuery(r).html('<a href="/login">Please login to vote.</a>');
	});
	jQuery('.thumb-it-down').click(function(e){
		var rId = jQuery(this).attr('data-toid');
		console.log(rId);
		var r = jQuery('#'+rId);
		console.log(r);
		jQuery(r).removeClass('green red');
		jQuery(r).addClass('red');
		jQuery(r).html('<a href="/login">Please login to vote.</a>');
	});
}
jQuery(document).ready(function(){
	thumbing();
});