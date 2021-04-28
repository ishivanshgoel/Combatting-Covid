let baseurl = 'http://localhost:8000/'

/**
 * @author ishivanshgoel
 * @function getDistricts fetches all districts
 */

// helper functions
async function getDistricts(state){
    return fetch(baseurl+'helper/districts/?state='+state)
    .then(response => response.json())
}

// to append fetched districts
document.getElementById("state").addEventListener("change", async ()=>{
    let state = document.getElementById("state").value
    getDistricts(state).then(data => {

        var c = document.getElementById("city")
        c.innerHTML = ''
        let option = document.createElement("option")
        option.text='Click to choose your District'
        option.value=null
        c.add(option, c[0])
        data.map((city, index)=>{
            let option = document.createElement("option")
            option.text=city
            option.value=city
            c.add(option, c[index+1])
        })
    })
});