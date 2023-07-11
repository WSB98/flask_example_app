


async function getBootData(){
     let txt;
    // send an http request to python script
    await fetch('/basic-request', {
        method:'POST',
        headers: {
            'Content-Type':'application/json'
        }
    }).then((response) => {
        console.log(response)
        return response.json()
    })
    .then((myJson) => {
        console.log(myJson.message); 
        txt = myJson.message
    })
    .catch((error) => {
        console.log(error)
        txt = error
    })
    // put it in the result area
    document.getElementById('resultArea1').innerText = txt;
    return txt
}

// loads the basic request
getBootData();


var averageButton = document.getElementById('button2');
averageButton.addEventListener('click', async(e) => {
    var inputValue = document.getElementById('input2').value;
    let txt;
    // send an http request to python script
    await fetch('/average-request', {
        method:'POST',
        headers: {
            'Content-Type':'application/json'
        },
        body: JSON.stringify(inputValue)
    }).then((response) => {
        console.log(response)
        return response.json()
    })
    .then((myJson) => {
        console.log(myJson.message); 
        txt = myJson.message
    })
    .catch((error) => {
        console.log(error)
        txt = error
    })
    // put it in the result area
    document.getElementById('resultArea2').innerText = txt;
    return txt
})