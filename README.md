# ⚡ ChargeGenie — EV Charging Route Planner

ChargeGenie is a **full-stack EV route planning application** that helps electric vehicle users find the **best charging stations along a route**, using **real-world charging data** and **intelligent recommendations**.

It combines:
- 🗺️ **Google Directions** (routing)
- 🔌 **OpenChargeMap** (EV charger data)
- 🧠 **Deterministic ranking**
- 🔐 **Role-based authentication**
- 📊 **Admin station management**
- 🖥️ **Modern React UI**

---

## 🚀 Key Features Implemented

### 👤 User Authentication (JWT)
- Secure **signup & login**
- JWT-based authentication
- Auto session restore on refresh
- Role-based access:
  - **EV User**
  - **Station Admin**

---

### 🧭 Route Planning
- Users enter **Source → Destination**
- Backend uses **Google Directions API**
- Returns:
  - Decoded polyline
  - Total distance (km)
  - Estimated duration (min)

---

### 🔌 EV Charging Station Discovery (OpenChargeMap)
- **Google Places fully replaced**
- Charging stations fetched from **OpenChargeMap API**
- Stations filtered to **≤ 3 km from route**
- Station metadata includes:
  - 📍 Distance from route
  - ⚡ Power (kW)
  - 🔌 Connector type
  - 🏢 Operator
  - 💰 Price per kWh (admin-controlled)
  - 🚦 Availability (admin-controlled)

---

### 🗺️ Interactive Map (Frontend)
- Google Maps JavaScript API
- Features:
  - Route polyline
  - Auto-fit bounds
  - Station markers with color-coded availability
  - Clickable info windows

---

### 🧠 Intelligent Charging Recommendations
- Backend shortlists stations based on:
  - Vehicle range
  - Battery percentage
  - Reachability
  - Availability
- Returns **Top 5 stations**
- Includes **human-readable explanation**
- Graceful fallback if no AI candidates found

---

### 🚗 Vehicle Profile
- User inputs:
  - Vehicle range (km)
  - Current battery %
- Used dynamically in recommendation logic

---

### ⭐ Recommendation Panel (UI)
- Displays:
  - Top 5 recommended stations
  - Power, connector, operator
  - Reason for recommendation
- Automatically updates per route search

---

### 🛠️ Admin Dashboard
- Separate admin login
- Admins can:
  - Set **price per kWh**
  - Update **availability**
- Admin data is merged dynamically into user results

---

### 🔐 Route Protection & Logout
- Dashboard protected by role
- Admin/User redirected correctly
- Logout supported on both dashboards

---

## 🧩 Tech Stack

### Frontend
- React (Hooks)
- React Router
- Tailwind CSS
- Axios
- Google Maps JS API

### Backend
- FastAPI
- MongoDB (PyMongo)
- JWT Authentication
- OpenChargeMap API
- Google Directions API

---

## 📂 Project Structure
```text
ChargeGenie/
│
├── backend/
│ ├── app/
│ │ ├── auth/
│ │ ├── maps/
│ │ │ ├── opencharge.py
│ │ │ ├── normalizer.py
│ │ │ └── service.py
│ │ ├── recommendations/
│ │ ├── stations/
│ │ ├── vehicle/
│ │ └── main.py
│ └── requirements.txt
│
├── frontend/
│ ├── src/
│ │ ├── pages/
│ │ ├── components/
│ │ ├── context/
│ │ └── services/
│ └── package.json
│
├── .gitignore
└── README.md
```

## 🔑 Environment Variables

Create a `.env` file in `backend/`:

```env
GOOGLE_MAPS_API_KEY=your_google_maps_key
OPENCHARGE_API_KEY=your_openchargemap_key
GEMINI_API_KEY=your_gemini_key   # optional (future AI)
MONGO_URI=MONGODB_ATLAS_CONNECTION_STRING

⚠️ Important
The .env file is ignored via .gitignore and is never committed to GitHub.

```
## ▶️ Running the Project

## 🔧 Backend
  - cd backend
  - python -m venv venv
  - venv\Scripts\activate   # Windows
  - pip install -r requirements.txt
  - uvicorn app.main:app --reload

## 🎨 Frontend
  - cd frontend
  - npm install
  - npm start

## 🌐 Access URLs

- Frontend → http://localhost:3000

- Backend API → http://127.0.0.1:8000

- Swagger Docs → http://127.0.0.1:8000/docs

## ✅ Current Status

- ✔ Route rendering with Google Directions
- ✔ Charging station markers visible on map
- ✔ OpenChargeMap fully integrated
- ✔ Deterministic charging recommendations
- ✔ Role-based dashboards (User / Admin)
- ✔ Secure authentication & logout
- ✔ MongoDB-based admin overrides

## 🔮 Future Enhancements (Planned)

## 📊 Admin Data Analytics

- Charging demand heatmaps

- Revenue insights

- Usage trends by region

- Peak-hour analytics

## 🤖 AI Chatbot Assistant

- Natural language queries such as:

- “Where should I charge next?”

- “Is this station suitable for my car?”

- Powered by Gemini / LLM

- Context-aware using route & vehicle data

## 🎨 Polished UI / UX

- Station list synced with map view

- Filters (fast chargers, cheapest stations)

- Dark mode






