





  
  submit_btn = document.getElementById('btn_predict')
  input_form = document.getElementById('get_inputs')
testing_btn = document.getElementById('shw_output')
 
  prediction_output = document.getElementById('predator')
  let resukt
  form_baner = document.getElementById("h2")
  
  measles = document.getElementById('Measles')
  disease_type = document.getElementById('disease_label')

  wk1 = document.getElementById('icon_prefix')
  wk2 = document.getElementById('icon_telephone')
  wk3 = document.getElementById('icon_three')
  wk4 = document.getElementById('icon_4')
  wk5 = document.getElementById('icon_5')
  wk6 = document.getElementById('icon_6')
  wk7 = document.getElementById('icon_7')
  wk8 = document.getElementById('icon_8')
  
  lastEpidemicDate = document.getElementById('datepicker')
  
  
  
  try{measles.addEventListener('click', e=>{
    disease_type.innerHTML = "Mealses"
    console.log(disease_type.textContent)

  })}catch(error){}
  
  try {
    submit_btn.addEventListener('click',e=>{
    
      form_baner.innerHTML = "National  Measles Outbreak projections  in 12 weeks"
      
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({
    "week_1": wk1.value,
    "week_2": wk2.value,
    "week_3": wk3.value,
    "week_4": wk4.value,
    "week_5": wk5.value,
    "week_6": wk6.value,
    "week_7": wk7.value,
    "week_8": wk8.value
    });
    var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
    };
    fetch("http://127.0.0.1:8000/Measles_forecaster", requestOptions)
      .then(response => response.text())
      .then(result => { res = JSON.parse(result)
        convertDate = new Date(lastEpidemicDate.value)
        for(let i = 9; i <= 20 ;i++)
        {
          card = document.createElement('div')
          card.className = 'box'
          convertDate.setDate(convertDate.getDate()+7)
          card.innerHTML= "<p><strong>"+res[i]+ "</strong> " + disease_type.textContent + " Cases Projected</p><p> by <strong>" +convertDate.toDateString()+" </strong></p>"
          prediction_output.appendChild(card)

        }
      
      })
      .catch(error => console.log('error', error)
      );
      
      
      
      input_form.style.display = 'none'
      
   })
  } catch (error) {
    
  }
 
  testing_btn.addEventListener('click',e =>{
    
    console.log( lastEpidemicDate.value)
   
    console.log(typeof lastEpidemicDate.value)
    
    console.log(typeof convertDate)
    console.log(convertDate.toDateString())


  
 
  })

 