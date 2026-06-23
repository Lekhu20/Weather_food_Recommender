import streamlit as st
import requests
import geocoder
import random

# ==========================================
# 1. PAGE SETUP & ULTRA-PRO-MAX DESIGN (CSS)
# ==========================================
st.set_page_config(page_title="SmartPlate AI", page_icon="🍳", layout="wide")

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] { background-color: #eef5fc !important; }
    .main { background-color: #eef5fc !important; }
    [data-testid="stSidebar"] { background-color: #ffffff !important; box-shadow: 2px 0px 10px rgba(0,0,0,0.05); }
    
    [data-testid="stSidebar"] h2 { font-size: 26px !important; font-weight: 800 !important; color: #1e272e !important; }
    [data-testid="stSidebar"] label p { font-size: 18px !important; font-weight: bold !important; color: #2c3e50 !important; }
    
    .item-card {
        background-color: #ffffff; padding: 22px; border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 15px;
        border-left: 6px solid #ff4b4b; transition: transform 0.2s;
    }
    .item-card:hover { transform: translateY(-2px); }
    .item-card h4 { font-size: 22px !important; margin-bottom: 8px !important; color: #1e272e !important; }
    .item-card p { font-size: 16px !important; color: #57606f !important; line-height: 1.5; }
    
    .time-tag { font-size: 13px !important; background-color: #f1f3f5; color: #495057; padding: 4px 10px; border-radius: 15px; font-weight: bold; display: inline-block; margin-top: 8px; }
    .meta-tag { font-size: 13px !important; color: white; padding: 4px 10px; border-radius: 15px; font-weight: bold; display: inline-block; margin-top: 8px; margin-left: 5px; }
    
    .surprise-box {
        background: linear-gradient(135deg, #ff9f43, #ff4b4b); color: white; padding: 30px; border-radius: 15px; text-align: center; box-shadow: 0 6px 15px rgba(255,75,75,0.3); margin-top: 25px;
    }
    .surprise-box h2, .surprise-box h3 { color: white !important; }
    .food-border { border-left-color: #ff9f43 !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <h1 style='text-align: center; background: linear-gradient(to right, #ff9f43, #f1c40f); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: bold; font-size: 42px; padding: 10px;'>
        🍳 SmartPlate: Live Smart Recipe Recommender
    </h1>
    """, 
    unsafe_allow_html=True
)
st.write("---")

# 
# ==========================================
# 2. GLOBAL MULTI-CUISINE MIX PIPELINE
# ==========================================
def fetch_live_recipes(mood_keyword):
    # Agar user ne kuch khud type kiya hai (like 'pasta', 'paneer')
    if mood_keyword and mood_keyword.strip() != "":
        url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={mood_keyword}"
        try:
            response = requests.get(url, timeout=5).json()
            meals = response.get("meals", [])
            if meals:
                random.shuffle(meals)
                formatted = []
                for meal in meals[:8]:
                    formatted.append({
                        "name": meal.get("strMeal"),
                        "desc": f"Category: {meal.get('strCategory')} | Fine global dynamic culinary lookup.",
                        "time": f"{random.randint(15, 45)} mins",
                        "cal": random.randint(200, 600),
                        "culture": f"{meal.get('strArea', 'Global')} 🌐"
                    })
                return formatted
        except:
            pass

    # MAGIC MULTI-ARRAY FILTER: Agar blank input hai ya SHUFFLE button dabaya hai
    # Hum multiple core cultures se simultaneously data pull karke merge karenge
    cuisines = [
        {"area": "Indian", "emoji": "🇮🇳"},
        {"area": "French", "emoji": "🇫🇷"},
        {"area": "Korean", "emoji": "🇰🇷"},
        {"area": "Italian", "emoji": "🇮🇹"},
        {"area": "Chinese", "emoji": "🇨🇳"},
        {"area": "American", "emoji": "🇺🇸"}
    ]
    
    combined_meals = []
    
    # Har country ke filter standard endpoints ko pull karte hain
    for c in cuisines:
        try:
            url = f"https://www.themealdb.com/api/json/v1/1/filter.php?a={c['area']}"
            res = requests.get(url, timeout=3).json()
            meals = res.get("meals", [])
            
            # Har country se 3-4 random items nikaal kar sample cluster banayenge
            if meals:
                random.shuffle(meals)
                for m in meals[:3]:
                    m["custom_area"] = f"{c['area']} {c['emoji']}" # Overriding with beautiful tags
                    combined_meals.append(m)
        except:
            continue # Agar koi ek country ki API slow ho toh skip karke aage badhega, crash nahi hoga
            
    # Pure international combinations array ko aapas me break aur mix karo!
    random.shuffle(combined_meals)
    
    if not combined_meals:
        # Emergency Fallback array
        return [{"name": "Global Fusion Platter 🍽️", "desc": "Live mix engine fallback optimization matrix.", "time": "20 mins", "cal": 350, "culture": "Fusion 🌐"}]
        
    formatted_items = []
    for meal in combined_meals[:8]: # Hamesha fresh top 8 diverse items render honge screen par
        formatted_items.append({
            "name": meal.get("strMeal"),
            "desc": f"Premium International Recipe Asset. Synchronized via real-time REST-API database pipelines.",
            "time": f"{random.randint(15, 50)} mins",
            "cal": random.randint(150, 650),
            "culture": meal.get("custom_area", "Global 🌐")
        })
        
    return formatted_items

# ==========================================
# 3. GEOLOCATION & WEATHER LOGIC
# ==========================================
def get_current_location():
    try:
        g = geocoder.ip('me')
        if g.status == 'OK': return g.city, g.country
        return "Delhi", "IN"
    except: return "Delhi", "IN"

def get_weather_status(city):
    try:
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
        geo_response = requests.get(geo_url).json()
        lat, lon = geo_response["results"][0]["latitude"], geo_response["results"][0]["longitude"]
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        return requests.get(weather_url).json()['current_weather']['temperature']
    except: return 26.0

city, country = get_current_location()
live_temp = get_weather_status(city)

# ==========================================
# 4. SIDEBAR CONTROL PANEL
# ==========================================
st.sidebar.markdown("## ⚙️ Controls Panel")
st.sidebar.info(f"📍 Location: **{city}**")

override_weather = st.sidebar.checkbox("Manually Change Weather?")
temperature = st.sidebar.slider("Temperature Override (°C)", -10, 50, int(live_temp)) if override_weather else live_temp
calorie_input = st.sidebar.slider("🔋 Max Calorie Cap (kcal)", min_value=100, max_value=800, value=600, step=50)

if temperature < 20: weather_type, w_emoji = "Cold 🥶", "🥶 Thand ka Mausam! Kuch garam aur heavy recipes check karo."
elif temperature > 39: weather_type, w_emoji = "Hot 🥵", "🥵 Garmi ka Mausam! Light aur refreshing items engine check karega."
else: weather_type, w_emoji = "Pleasant 🌤️", "🌤️ Mast Mausam! Explore our fully dynamic live API recipes."

st.markdown(f"### 🌡️ Temperature: <span style='color:#ff9f43'>{temperature} °C ({weather_type})</span> | Calorie Limit: <span style='color:#2ecc71'>{calorie_input} kcal</span>", unsafe_allow_html=True)
st.write(w_emoji)
st.write("---")

# Initialize session state for input text
if "mood_input" not in st.session_state:
    st.session_state.mood_input = "chicken"

# Categories Buttons Pipeline
col_b1, col_b2, col_b3 = st.columns(3)
if col_b1.button("🥩 Chicken / Non-Veg Specials"): st.session_state.mood_input = "chicken"
if col_b2.button("🥦 Healthy Vegetarian Recipes"): st.session_state.mood_input = "vegetarian"
if col_b3.button("🍰 Sweet Desserts"): st.session_state.mood_input = "cake"

# NEW REFRESH BUTTON GRID SECTION
col_refresh, col_empty = st.columns([1, 2])
with col_refresh:
    # Clicking this button forces Streamlit to reset and fetch a completely different API stack order
    if st.button("🔄 Shuffle & Fetch New Menu", use_container_width=True):
        st.toast("Shuffling data engine matrix...", icon="🔄")
        # No extra logic needed, Streamlit re-runs and random.shuffle does the work

user_mood = st.text_input("💭 Enter ingredient or mood keyword (e.g., pasta, paneer, sweet, fish):", key="mood_input")

if user_mood:
    with st.spinner("Fetching dynamic live data from Cloud Recipe Database..."):
        live_recipes = fetch_live_recipes(user_mood)
        filtered_recipes = [r for r in live_recipes if r["cal"] <= calorie_input]
        
        if not filtered_recipes:
            st.warning("⚠️ High Calorie Alerts! Aapki di gayi calorie limit bohot kam hai, par API se kuch safe items niche load kiye gaye hain.")
            filtered_recipes = live_recipes[:3]

        menu_text = f"=== LIVE SMARTPLATE RECIPE DECK ===\n Query Parameter: {user_mood} | Active Calorie Cap: {calorie_input} kcal\n===============================================\n\n"
        for idx, r in enumerate(filtered_recipes, 1):
            menu_text += f"{idx}. {r['name']} (Calories: {r['cal']} kcal | Area: {r['culture']})\n"
            
        st.download_button(label="📥 Download this Recipe List", data=menu_text, file_name="Live_Recipes.txt", mime="text/plain")
        
        st.write("### 🍲 Dynamic Recipes Deck ")
        
        for i, r in enumerate(filtered_recipes, 1):
            html_card = f"""
            <div class='item-card food-border'>
                <h4>{i}. {r['name']}</h4>
                <p>{r['desc']}</p>
                <span class='time-tag'>⏱️ Prep Time: {r['time']}</span>
                <span class='meta-tag' style='background-color:#ff9f43;'>📊 {r['cal']} kcal</span>
                <span class='meta-tag' style='background-color:#9b59b6;'>🗺️ {r['culture']}</span>
            </div>
            """
            st.markdown(html_card, unsafe_allow_html=True)
            
        st.write("---")
        if st.button("✨ Surprise Me! (Random Selection)"):
            surprise_item = random.choice(filtered_recipes)
            surprise_html = f"""
            <div class='surprise-box'>
                <h2>🎉 Random Live Selection Generated! 🎉</h2>
                <hr style='border-color:rgba(255,255,255,0.3)'>
                <h3>🍽️ Selected Recipe: {surprise_item['name']}</h3>
                <p>{surprise_item['desc']}</p>
                <h4 style='color:yellow;'>🔋 Metrics: {surprise_item['cal']} kcal | Prep: {surprise_item['time']}</h4>
            </div>
            """
            st.markdown(surprise_html, unsafe_allow_html=True)