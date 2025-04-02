document.addEventListener('DOMContentLoaded', async () => {
    try {
        const response = await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');
        const data = await response.json();
        const helloElement = document.querySelector('#hello');
        helloElement.append(data.hello);
    } catch (error) {
        console.error('Error fetching data:', error);
    }});

