document.addEventListener("DOMContentLoaded", function () {

    const mapContainer = document.getElementById("map");
    if (!mapContainer) return;

    let map = L.map('map').setView([20.5937, 78.9629], 5);
    let marker = null;

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap'
    }).addTo(map);

    map.on('click', function (e) {

        if (marker) map.removeLayer(marker);

        marker = L.marker([e.latlng.lat, e.latlng.lng]).addTo(map);

        fetch(`/api/predict-location?lat=${e.latlng.lat}&lon=${e.latlng.lng}`)
            .then(res => res.json())
            .then(data => {

                if (data.error) {
                    alert(data.error);
                    return;
                }

                document.getElementById("details").innerHTML = `
                    <div class="card">
                        <h3>📍 Location Details</h3>
                        <p><b>Latitude:</b> ${data.latitude}</p>
                        <p><b>Longitude:</b> ${data.longitude}</p>
                        <p><b>Temperature:</b> ${data.temperature} °C</p>
                        <p><b>Humidity:</b> ${data.humidity} %</p>
                        <p><b>Pressure:</b> ${data.pressure} hPa</p>
                        <p><b>Wind Speed:</b> ${data.wind_speed} m/s</p>
                        <h3>⚡ Predicted Power: ${data.power} kWh</h3>
                    </div>
                `;

            });

    });

});
