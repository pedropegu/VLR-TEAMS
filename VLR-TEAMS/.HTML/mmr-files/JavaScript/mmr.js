async function getMMR(){
    
    let User = document.getElementsByName('InputUser')[0].value
    let Hastag = document.getElementsByName('inputHastag')[0].value

    let responde = await fetch('https://api.henrikdev.xyz/valorant/v2/mmr/eu/{User}/{Hastag}');
    let data = await responde.json();

    let datos = data['data']['name'] + " " + data['data']['current_data']['currenttierpatched'] + " " + data['data']['current_data']['elo']
    alert(datos)    
}

