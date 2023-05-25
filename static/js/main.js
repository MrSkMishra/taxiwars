console.log("varsha")

const csrftoken = $.cookie('csrftoken');

		function verifyDriver(driverId, button) {
			$.ajax({
				url: `/api/driver/verify/${driverId}/`,
				type: 'POST',
				headers: {
					'X-CSRFToken': csrftoken,
				},
				success: function(response) {
					// Handle the response, e.g., update the UI to show the driver as verified
					alert('Driver verified successfully!');
					// Change the button color to green
					button.css('background-color', '#4CAF50');
					// Disable the button
					button.prop('disabled', true);
				},
				error: function(error) {
					// Handle the error, e.g., show an error message to the user
					alert('Failed to verify driver.');
				}
			});
		}
	
		$(document).ready(function() {
			$('.verify-button').click(function() {
				var button = $(this);
				var driverId = button.attr('data-driver-id');
				verifyDriver(driverId, button);
			});
		});