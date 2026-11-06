  banner = document.getElementById('banner')
  login_btn = document.getElementById('logger')
  user = document.getElementById('staticEmail')
  pwd = document.getElementById('inputPassword')

  try{
    login_btn.addEventListener('click', e=>{
      if ( user.value == "sam" && pwd.value == 123)
      {
        window.location.replace("prediction_outputs.html");
      }
      else{
        alert("errorMessage: wrong user or password");
      }
    })
  } catch(error){}