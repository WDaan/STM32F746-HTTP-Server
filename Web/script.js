window.setInterval(
    () => {
        console.log("Update");
				fetch("temp.cgi")
					.then((res) => res.text())
					.then((res) => {
							console.log(res);
							document.getElementById('temp').innerHTML = res;
					});
					
				fetch("wanted-temp.cgi")
					.then((res) => res.text())
					.then((res) => {
							console.log(res);
							if(res == 'ON'){
							 $('#status')
								.addClass('btn-success')
								.removeClass('btn-primary')
								.removeClass('btn-danger')
							}else if(res == 'OFF'){
								 $('#status')
								.addClass('btn-danger')
								.removeClass('btn-primary')
								.removeClass('btn-success')
							}
					});
    },
    3000
);