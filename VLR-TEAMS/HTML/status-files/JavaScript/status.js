
 var img = new Image();
 var div = document.getElementById('status');
let response = fetch('https://api.henrikdev.xyz/valorant/v1/status/eu')
    .then((response) => {
    div.innerHTML = "EUW: "
  })
image = div.appendChild(img)
img.src ='../../favicon.png'

