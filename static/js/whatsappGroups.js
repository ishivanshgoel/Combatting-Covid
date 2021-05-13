console.log("Whatsapp script attached!!")

/**
 * @author ishivanshgoel
 * @param push all the whatsapp groups data
 */

let whatsappGroups = {
    Maharashtra: "https://chat.whatsapp.com/GZveR14GtzD0y7bO0wfMkm",
    UttarPradesh: "https://chat.whatsapp.com/LD5aPbi47SX2gpNUZC2k69",
    Gujarat: "https://chat.whatsapp.com/HbcsNnLdoG077zpBLLVMZg",
    Rajasthan: "https://chat.whatsapp.com/KWDq0bQYIE3IMFDSkCua3C",
    TamilNadu: "https://chat.whatsapp.com/EIS4yuo6EXbBZEIEmohOkW",
    WestBengal: "https://chat.whatsapp.com/KQcXMnKy3bV17lMXco9ULN",
    Uttarakhand: "https://chat.whatsapp.com/KQcXMnKy3bV17lMXco9ULN",
    Odisha: "https://chat.whatsapp.com/KQcXMnKy3bV17lMXco9ULN",
    ArunachalPradesh: "https://chat.whatsapp.com/KQcXMnKy3bV17lMXco9ULN",
    Bihar: "https://chat.whatsapp.com/Cw7pkIAxJxZ98zcZtaFM4Y",
    Jharkhand: "https://chat.whatsapp.com/Cw7pkIAxJxZ98zcZtaFM4Y",
    MadhyaPradesh: "https://chat.whatsapp.com/Dh5bkqLYxuk1SeJLuGr08c",
    Chhattisgarh: "https://chat.whatsapp.com/Dh5bkqLYxuk1SeJLuGr08c",
    DelhiNCR1: "https://chat.whatsapp.com/BsgSwWzlZAN9CjDbwZIqiu",
    DelhiNCR2: "https://chat.whatsapp.com/HnJW3exSXFIJKvyGJr1ioB",
    Punjab: "https://chat.whatsapp.com/EKd79nEf5NH3BDPdgkE1bB",
    Haryana: "https://chat.whatsapp.com/EKd79nEf5NH3BDPdgkE1bB",
    AndhraPradesh: "https://chat.whatsapp.com/KUkGcSKFmY8FcMiOMmYajc",
    Karnataka: "https://chat.whatsapp.com/KUkGcSKFmY8FcMiOMmYajc",
    Telangana: "https://chat.whatsapp.com/KUkGcSKFmY8FcMiOMmYajc",
    JammuKashmir: "https://chat.whatsapp.com/BQ3S13Geisc5FfA2RT0TGk"
}

// option element
let whatsappNode = document.getElementById('selectWhatsappGroups')
whatsappNode.classList = "custom-select form-control py-2"

// create dummy option
let option = document.createElement("option")
let index = 1

// iterate over objects and push the key values
for (let [key, value] of Object.entries(whatsappGroups)) {
    let option = document.createElement("option")
    option.text = key
    option.value = key
    whatsappNode.add(option, whatsappNode[index])
    index=index+1
}

// push 1st link from data bydefault
let whatsappButton = document.getElementById('joinWhatsappButton')
whatsappButton.href = whatsappGroups[Object.keys(whatsappGroups)[0]]
whatsappButton.target = '_blank'


// push state group link in the whatsapp button
document.getElementById("selectWhatsappGroups").addEventListener("change",()=>{
    let state = document.getElementById('selectWhatsappGroups').value
    whatsappButton.href = whatsappGroups[state]
    whatsappButton.target = '_blank'
})