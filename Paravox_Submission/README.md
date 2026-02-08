# Paravox Smart Glove: AI-Powered Assistive Technology

<p align="center">
  <img src="https://via.placeholder.com/800x400?text=Paravox+Smart+Glove" alt="Paravox Banner">
</p>

## 🚀 Project Overview
**Paravox** is a revolutionary smart glove designed to empower the mute and deaf community by translating sign language into spoken speech using **Generative AI (Gemini 1.5 Flash)**. It goes beyond simple translation by acting as a **Guardian System**, monitoring the user's health and safety in real-time.

---

## 🌟 Key Features
*   **Gestures to Speech:** Real-time translation of sign language into natural speech.
*   **Generative Conversations:** Uses LLMs to form complete, grammatically correct sentences from simple gestures.
*   **Guardian Safety System:** Autonomous Fall Detection and Heart Rate Monitoring.
*   **Hybrid Architecture:** Edge Processing (ESP32) for speed + Cloud AI (Gemini) for intelligence.
*   **Cost-Effective:** Built on affordable hardware (~$20) compared to expensive medical devices.

---

## 🛠️ Technology Stack
*   **Hardware:** ESP32 Microcontroller, Flex Sensors, MPU6050 Accelerometer.
*   **Mobile App:** Android Studio (Java/Kotlin).
*   **AI Engine:** Google Gemini 1.5 Flash API.
*   **Connectivity:** Bluetooth Serial (SPP), WiFi.
*   **Backend:** Python (Flask) Bridge.

---

## 📂 Repository Structure
*   `app.py`: The Python Bridge Server acting as a gateway to the Gemini API.
*   `your_hackthon_problemstatement.pdf`: Detailed problem statement and solution analysis.
*   `your projectpresntation.pptx`: The complete project presentation.

---

## ⚙️ Setup & Installation
1.  **Clone the Repository**
    ```bash
    git clone https://github.com/YourUsername/Paravox-Smart-Glove.git
    cd Paravox-Smart-Glove
    ```

2.  **Install Dependencies**
    ```bash
    pip install flask requests
    ```

3.  **Run the Bridge Server**
    ```bash
    python app.py
    ```

---

## 👥 Team
*   **Lead Developer / Visionary:** [Your Name]
*   **Hardware Engineer:** [Name]
*   **AI Specialist:** [Name]

---

> *Built for [Hackathon Name] 2026. Empowering Voices, Saving Lives.*
