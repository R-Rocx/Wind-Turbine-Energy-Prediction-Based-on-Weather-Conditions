let liveChart;
let currentWeather = {};

function showLoader(show) {
    const loader = document.getElementById("globalLoader");
    if (!loader) return;
    loader.classList.toggle("hidden", !show);
}

function getWeather() {

    const city = document.getElementById("city").value;

    if (!city) {
        alert("Enter city name");
        return;
    }

    showLoader(true);

    fetch(`/api/weather/${city}`)
    .then(res => res.json())
    .then(data => {

        showLoader(false);

        if (data.error) {
            alert(data.error);
            return;
        }

        currentWeather = data;

        document.getElementById("temperature").innerText = data.temperature;
        document.getElementById("humidity").innerText = data.humidity;
        document.getElementById("wind_speed").innerText = data.wind_speed;
        document.getElementById("wind_direction").innerText = data.wind_direction;

    })
    .catch(() => {
        showLoader(false);
        alert("Weather fetch failed");
    });
}

function predictPower() {

    if (!currentWeather.temperature) {
        alert("Fetch weather first");
        return;
    }

    showLoader(true);

    fetch("/api/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(currentWeather)
    })
    .then(res => res.json())
    .then(data => {

        showLoader(false);

        document.getElementById("power_result").innerText =
            "⚡ Predicted Energy: " + data.power + " kWh";

        updateChart(data.power);

    })
    .catch(() => {
        showLoader(false);
        alert("Prediction failed");
    });
}

function updateChart(power) {

    const ctx = document.getElementById("liveChart");

    if (!liveChart) {

        liveChart = new Chart(ctx, {
            type: "bar",
            data: {
                labels: ["Predicted Energy"],
                datasets: [{
                    label: "Energy Output (kWh)",
                    data: [power],
                    backgroundColor: "#00e676",
                    borderRadius: 8
                }]
            },
            options: {
                responsive: true,
                animation: {
                    duration: 1200
                },
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });

    } else {

        liveChart.data.datasets[0].data[0] = power;
        liveChart.update();
    }
}

