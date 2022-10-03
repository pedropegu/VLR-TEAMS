
let euw = fetch('https://api.henrikdev.xyz/valorant/v1/status/eu')
    .then((response) => {
    if (response["status"] == 200) {
      document.getElementById('status-euw').innerHTML = "EU: No recent issues or events to report  " + '<i class="bi bi-check-circle-fill"></i>' 
    } else {
      document.getElementById('status-euw').innerHTML = "EUW: " + response["data"]["incidents"] + '  <i class="bi bi-x"></i>'
    }
  })

  let na = fetch('https://api.henrikdev.xyz/valorant/v1/status/na')
  .then((response) => {
  if (response["status"] == 200) {
    document.getElementById('status-na').innerHTML = "NA: No recent issues or events to report  " + '<i class="bi bi-check-circle-fill"></i>' 
  } else {
    document.getElementById('status-na').innerHTML = "NA: " + response["data"]["incidents"] + '  <i class="bi bi-x"></i>'
  }
})

