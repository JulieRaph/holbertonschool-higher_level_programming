document.addEventListener("DOMContentLoaded", async () => {
    const url = "https://swapi-api.hbtn.io/api/films/?format=json";
    try {
        const response = await fetch(url);
        const data = await response.json();
        const filmElement = document.getElementById("list_movies");
        
        data.results.forEach(film => {
            const newItem = document.createElement('li');
            newItem.textContent = film.title;
            filmElement.append(newItem);
        })

    } catch (error) {
        console.error("Error fetching data:", error);
     }
});