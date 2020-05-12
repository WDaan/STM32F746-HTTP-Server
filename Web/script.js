window.setInterval(
    () => {
        console.log("test");
				fetch("temp.cgi")
					.then((res) => res.text())
					.then((res) => {
						console.log(res)
					});
    },
    3000
);