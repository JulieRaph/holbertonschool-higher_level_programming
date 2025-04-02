document.addEventListener("DOMContentLoaded", function() {
    fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
        .then(response => response.json()).then(data => {
            document.getElementById("character").textContent = data.name;
        })
        .catch(e => {
            console.error("Error fetching data:", e);
        })
});


// document.addEventListener("DOMContentLoaded", async () => {
//     const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";
//     try {
//         const response = await fetch(url);
//         const data = await response.json();
//         const characterElement = document.getElementById("character");
//         characterElement.textContent = data.name;
//     } catch (error) {
//         console.error("Error fetching data:", error);
//     }
// });