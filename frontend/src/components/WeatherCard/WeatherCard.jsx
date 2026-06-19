import "./WeatherCard.css";
import { CloudSun } from "lucide-react";

function WeatherCard() {
  return (
    <div className="weather-card">
      <div className="weather-header">
        <CloudSun size={26}/>
        <h2>Weather</h2>
      </div>

      <h1>28°C</h1>

      <p>Bhubaneswar</p>

      <span>Mostly Clear</span>
    </div>
  );
}

export default WeatherCard;