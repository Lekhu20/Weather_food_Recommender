# Weather_food_Recommender
# 🍳 SmartPlate : Environment & Calorie Driven Live Recipe Recommender

SmartPlate AI is a dynamic, context-aware web application designed to eliminate meal indecisiveness. Unlike traditional static recipe apps, this engine synchronizes third-party environmental telemetries (Live Weather & Geolocation) with explicit user targets (Calorific Caps & Flavor Profiles) to compute a personalized global menu in real-time.

Built using **Python** and **Streamlit**, the application directly consumes data from live REST-API pipelines to provide a completely refreshed user experience on every interaction.

---

## 🚀 Live Demo
🔗 https://weatherfoodrecommender-nkkn3zf6h3qjrnezztqtss.streamlit.app/

---

## ✨ Key Features & Technical Highlights

* **🌍 Automated Geolocation Sync:** Utilizes IP-based location tracking (`Geocoder`) to identify the user's active city seamlessly without manual forms.
* **🌡️ Live Weather Telemetry:** Integrates the `Open-Meteo API` to pull real-time local temperatures, automatically adapting recommendations based on climate context (e.g., warm recipes for chilly weather, cooling refreshers for hot sunny days).
* **🌐 Global Multi-Cuisine Mix Engine:** Leverages a custom-merged backend array that hits `TheMealDB API` server endpoints concurrently to fetch and shuffle authentic recipes across diverse cultures like **Indian (🇮🇳), French (🇫🇷), Korean (🇰🇷), Italian (🇮🇹), and Chinese (🇨🇳)**.
* **🔋 Advanced Calorie Cap Filter:** Features a strict micro-management slider that filters incoming live API data payloads dynamically to stay within the user’s exact health thresholds.
* **🔄 State-Preserved Instant Shuffler:** Integrated with a seamless runtime Shuffler and Category filter pipeline utilizing Streamlit's `session_state` to instantly rebuild card layouts on user click without losing global variables.
* **📥 Structural Data Exporter:** Built-in capability to compile and download the computed menu directly into a structured plain-text file (`.txt`) for offline tracking.

---

## 🛠️ Tech Stack & Architecture

* **Frontend/UI:** Streamlit (Python Ecosystem)
* **Design & Styling:** Custom CSS Injection (Premium Micro-interactions & Visual Cards layout)
* **Data Pipelines & Consumption:** Python `requests` library
* **Public Core REST-APIs Consumed:**
  * **TheMealDB API:** (For dynamic multi-cuisine raw meal dataset lookup)
  * **Open-Meteo API:** (For real-time location-based temperature forecasting)
  * **Geocoder:** (For accurate backend IP network geolocation extraction)

---

