var map = L.map('map').setView([20, 0], 2);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(map);
fetch('http://127.0.0.1:8000/airports')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        data.forEach(position => {
            var marker = L.marker([position.lat, position.lon]).addTo(map);
            marker.on('click', () => {
                fetch(`http://127.0.0.1:8000/airports/${position.code}/`)
                    .then(response => response.json())
                    .then(data => {
                        data.forEach(detail=>{                         
                            document.getElementById('sidebar-title').textContent = detail.name;
                            document.getElementById('country').textContent = "country:" + detail.country;
                            document.getElementById('state').textContent = "state:" + detail.state;
                            document.getElementById('city').textContent = "city:" + detail.city;

                            const selectedDay = document.querySelector('input[name="day"]:checked');
                            const hourInput = document.getElementById('hour-input');
                            const hour = parseInt(hourInput.value, 10);
                            const dayIndex =parseInt(selectedDay.value, 10);
                            const day =`day ${dayIndex+1}`

                            fetch(`http://127.0.0.1:8000/airports_weather/${position.code}/`)
                                .then(response=>response.json())
                                .then(data=>{
                        
                                    document.getElementById('temperature').textContent = "temperature:" + data.temperature_2m[day][hour];
                                    document.getElementById('snowfall').textContent = "snowfall:" + data.snowfall[day][hour];
                                    document.getElementById('snowdepth').textContent = "snow depth:" + data.snow_depth[day][hour];
                                    document.getElementById('wind').textContent = "wind speed 10m:" + data.wind_speed_10m[day][hour];
                                    
                                    
                        
                                })
                    .catch(error => console.error('Error fetching the weather data:', error));
                        })
                    })
                    
                    .catch(error => console.error('Error fetching the JSON data:', error));
                
                
            });
        });
    })
    .catch(error => console.error('Error fetching the JSON file:', error));