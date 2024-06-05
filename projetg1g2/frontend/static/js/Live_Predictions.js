function sliceDictionary(dict, n) {
    const entries = Object.entries(dict);
    const slicedEntries = entries.slice(0, n);
    const slicedDict = Object.fromEntries(slicedEntries);
    return slicedDict;
}

var map = L.map('map').setView([20, 0], 2);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(map);

let markers = [];

function updateMap(num) {
    // Clear existing markers
    markers.forEach(marker => map.removeLayer(marker));
    markers = [];

    fetch('http://127.0.0.1:8000/airports')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            const slicedData = sliceDictionary(data, num);
            const positions = Object.values(slicedData);
            positions.forEach(position => {
                var marker = L.marker([position.lat, position.lon]).addTo(map);
                markers.push(marker);
                marker.on('click', () => {
                    fetch(`http://127.0.0.1:8000/airports/${position.code}/`)
                        .then(response => {
                            if (!response.ok) {
                                throw new Error('Network response was not ok ' + response.statusText);
                            }
                            return response.json();
                        })
                        .then(details => {
                            const detail = details[0]; // Assuming details is an array and we need the first item
                            document.getElementById('sidebar-title').textContent = detail.name;
                            document.getElementById('country').textContent = "country: " + detail.country;
                            document.getElementById('state').textContent = "state: " + detail.state;
                            document.getElementById('city').textContent = "city: " + detail.city;

                            const selectedDay = document.querySelector('input[name="day"]:checked');
                            const hourInput = document.getElementById('hour-input');
                            const hour = parseInt(hourInput.value);
                            
                            const dayIndex = parseInt(selectedDay.value);
                            const day = `day${dayIndex + 1}`;

                            fetch(`http://127.0.0.1:8000/airports_weather/${position.code}/`)
                                .then(response => {
                                    if (!response.ok) {
                                        throw new Error('Network response was not ok ' + response.statusText);
                                    }
                                    return response.json();
                                })
                                .then(weatherData => {
                                    document.getElementById('temperature').textContent = "temperature: " + weatherData.temperature_2m[day][hour];
                                    document.getElementById('snowfall').textContent = "snowfall: " + weatherData.snowfall[day][hour];
                                    document.getElementById('snowdepth').textContent = "snow depth: " + weatherData.snow_depth[day][hour];
                                    document.getElementById('wind').textContent = "wind speed 10m: " + weatherData.wind_speed_10m[day][hour];
                                })
                                .catch(error => console.error('Error fetching the weather data:', error));
                        })
                        .catch(error => console.error('Error fetching the airport details:', error));
                });
            });
        })
        .catch(error => console.error('Error fetching the airports:', error));
}

// Initial load
updateMap(10);

// Slider functionality
const slider = document.getElementById('airport-slider');
const sliderValue = document.getElementById('slider-value');

slider.addEventListener('input', function() {
    const num = parseInt(this.value);
    sliderValue.textContent = num;
    updateMap(num);
});
