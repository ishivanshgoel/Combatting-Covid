console.log("Connected to cutum.js")
let baseurl = 'http://localhost:8000/'

/**
 * @author ishivanshgoel
 * @function getDistricts fetches all districts
 */

// helper functions
async function getDistricts(state){
    return fetch('/helper/districts/?state='+state)
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

// modify calls
$('.btn-Modify').click(function(){
    console.log("Modify Function called")
    var url = $(this).data("url"); 
    console.log("URL ", url)
    $.ajax({
        url: baseurl + url,
        dataType: 'json',
        success: function(res) {

            // get the ajax response data
            var data = res.body;

            // update modal content here
            // you may want to format data or 
            // update other modal elements here too
            $('.modal-body').text(data);

            // show modal
            $('#modifyModal').modal('show');

        },
        error:function(request, status, error) {
            console.log("ajax call went wrong:" + request.responseText);
        }
    });
});


//public form submit
function submitForm(type){
    console.log("Form Submit")
    let state = document.getElementById("state").value
    let district = document.getElementById("city").value
    let queryString = `/${type}/?state=${state}&district=${district}`
    $("#myform").attr('action', queryString);
    $("myForm").submitForm()
}