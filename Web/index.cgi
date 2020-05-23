t <!doctype html>
t <html lang="en">
t   <head>
t     <!-- Required meta tags -->
t     <meta charset="utf-8">
t     <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
t     <!-- Bootstrap CSS -->
t     <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
t integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
t     <title>Micro3 - Webserver</title>
t   </head>
t   <body style="background-color: #f8fafc">
t     <div>
t      <nav class="navbar navbar-expand-md navbar-light bg-white shadow-sm sticky-top" style="padding: 3px 8px 3px 8px;">
t             <div class="container">
t                 <a class="navbar-brand" href="/">
t                     <img src="/vives-logo.png" style="width: 40px; margin-right: 10px;"></img>
t                 </a>
t                 <div>
t                     <!-- Right Side Of Navbar -->
t                     <ul class="navbar-nav ml-auto text-center">
t                         <!-- Authentication Links -->
t                         <li class="nav-item">
t                             <a class="nav-link" href="/">Home</a>
t                         </li>
t                     </ul>
t                 </div>
t             </div>
t         </nav>
t         <div class="container">
t           <div style="text-align: center" class="mt-5">
t             <h1> Micro3 - Webserver </h1>
t           </div>
t           <div class="mx-auto" style="margin-top: 100px; max-width: 800px">
t             <div class="card">
t                 <h5 class="card-header">Thermostaat</h5>
t                 <div class="card-body text-center">
t                   <h5 class="card-title">Temperatuur: 
c y                       <span id="temp">%d</span> &#8451;
t                   </h5>
t                   <h5 class="card-title">Ventilator status: 
t                       <button class="btn btn-primary disabled" style="padding: 10px; cursor:default;" id="status"></button>
t                   </h5>
t                   <div class="mx-auto" style="max-width: 200px; margin-top: 50px;">
t                     <form action="index.cgi" method="POST" name="wantedTemperature">
t                       <div class="form-group">
t                         <label for="wantedTemperature">Gewenste temperatuur</label>
c f 					  <input type=number name=wtemp min=10 max=35 value="%d" class="form-control">
t                       </div>
t                       <button value="Send" type="submit" class="btn btn-primary OnClick="submit();">Submit</button>
t                     </form>
t                   </div>
t                 </div>
t               </div>
t           </div>
t         </div>
t       </div>
t     <!-- Optional JavaScript -->
t     <!-- jQuery first, then Popper.js, then Bootstrap JS -->
t     <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" 
t 		integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous">
t 	  </script>
t     <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" 
t 		integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous">
t  	  </script>
t     <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" 
t 			integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous">
t 	 </script>
t     <script src="script.js"></script>
t   </body>
t </html>
.