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
                            fetch(`http://127.0.0.1:8000/airports_weather/${position.code}/`)
                                .then(response=>response.json())
                                .then(data=>{
                        
                                    console.log(data.temperature_2m
                                    )
                        
                                })
                    .catch(error => console.error('Error fetching the weather data:', error));
                        })
                    })
                    
                    .catch(error => console.error('Error fetching the JSON data:', error));
                
                
            });
        });
    })
    .catch(error => console.error('Error fetching the JSON file:', error));