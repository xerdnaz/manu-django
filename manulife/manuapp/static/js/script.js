$('.drop-down-button').on('click', function () {
		var $dropDownList = $('#drop-down-list');
		var $dropArrow = $('.drop-down .drop-arrow');
	
		$dropDownList.slideToggle('fast');
	
		if ($dropArrow.hasClass('arrow-up')) {
				$dropArrow.removeClass('arrow-up');
		} else {
				$dropArrow.addClass('arrow-up');
		}
});