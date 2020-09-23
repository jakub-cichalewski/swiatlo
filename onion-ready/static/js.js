var light_state = true;

function change_image(){
  var filename = light_state ? "/static/on.png" : "/static/off.png"
  document.getElementById("bulb").src = filename;
}


function get_state(){

  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if(xhr.readyState === 4){
      var json = JSON.parse(xhr.response);
      light_state = json.state;
      change_image()
    }
  }

  xhr.open('GET', '/check', true);
  xhr.send('');
}


function toggle(){
  var xhr = new XMLHttpRequest();

  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      var json = JSON.parse(xhr.response);
      light_state = json.state;
      change_image()
    }
  }

  xhr.open('GET', '/toggle', true);
  xhr.send('');
}
