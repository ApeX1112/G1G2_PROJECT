
document.getElementById('cross').addEventListener('click', function() {
    document.getElementById('sidebar').style.display = 'none';
});
document.addEventListener("DOMContentLoaded", function() {
    var regularIconUrl = "/static/assets/marker-icon.png";
    var highlightedIconUrl = "/static/assets/red_marker.webp";

    var map = L.map('map').setView([20, 0], 2);
    document.getElementById('sidebar').style.display = 'none';
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
    }).addTo(map);

    let markers = [];

    const regularIcon = L.icon({
        iconUrl: regularIconUrl,
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
        shadowSize: [41, 41]
    });

    const highlightedIcon = L.icon({
        iconUrl: highlightedIconUrl,
        iconSize: [30, 45],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
        shadowSize: [41, 41]
    });

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
                const selectedDay = document.querySelector('input[name="day"]:checked');
                const hourInput = document.getElementById('hour-input');
                const hour = parseInt(hourInput.value);
                const dayIndex = parseInt(selectedDay.value);
                const day = `day${dayIndex + 1}`;

                positions.forEach(position => {
                    // Create a regular marker first
                    var marker = L.marker([position.lat, position.lon], { icon: regularIcon }).addTo(map);
                    markers.push(marker);

                    // Fetch weather data to check highlighted status
                    fetch(`http://127.0.0.1:8000/airports_weather/${position.code}/`)
                        .then(response => {
                            if (!response.ok) {
                                throw new Error('Network response was not ok ' + response.statusText);
                            }
                            return response.json();
                        })
                        .then(weatherData => {
                            // Check the highlighted array for the selected day and hour
                            if (weatherData.highlighted[24*dayIndex+hour]) {
                                marker.setIcon(highlightedIcon);
                            } else {
                                marker.setIcon(regularIcon);
                            }
                        })
                        .catch(error => console.error('Error fetching the weather data:', error));

                    marker.on('click', () => {
                        fetch(`http://127.0.0.1:8000/airports/${position.code}/`)
                            .then(response => {
                                if (!response.ok) {
                                    throw new Error('Network response was not ok ' + response.statusText);
                                }
                                return response.json();
                            })
                            .then(details => {
                                const detail = details[0];
                                document.getElementById('sidebar').style.display = 'block'; // Assuming details is an array and we need the first item
                                document.getElementById('sidebar-title').textContent = detail.name;
                                document.getElementById('country').textContent = "country: " + detail.country;
                                document.getElementById('state').textContent = "state: " + detail.state;
                                document.getElementById('city').textContent = "city: " + detail.city;

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
                                        document.getElementById('preds1').textContent = "alg1: " + weatherData.predictions_alg1[24*dayIndex+hour];
                                    })
                                    .catch(error => console.error('Error fetching the weather data:', error));
                            })
                            .catch(error => console.error('Error fetching the airport details:', error));
                    });
                });
            })
            .catch(error => console.error('Error fetching the airports:', error));
    }


    updateMap(10);

    
    const slider = document.getElementById('airport-slider');
    const sliderValue = document.getElementById('slider-value');

    slider.addEventListener('input', function() {
        const num = parseInt(this.value);
        sliderValue.textContent = num;
        updateMap(num);
    });

   
    document.querySelectorAll('input[name="day"]').forEach(dayInput => {
        dayInput.addEventListener('change', () => {
            const num = parseInt(slider.value);
            updateMap(num);
        });
    });

    document.getElementById('hour-input').addEventListener('input', () => {
        const num = parseInt(slider.value);
        updateMap(num);
    });
});

function sliceDictionary(dict, n) {
    const entries = Object.entries(dict);
    const slicedEntries = entries.slice(0, n);
    const slicedDict = Object.fromEntries(slicedEntries);
    return slicedDict;
}
