import streamlit as st

@st.cache
def get_location():
    lat = st.request.args.get("lat")
    lng = st.request.args.get("lng")
    return lat, lng

def main():
    st.set_page_config(page_title="My App", page_icon=":guardsman:", layout="wide")
    st.title("My App")
    st.markdown("""
    <script>
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            var lat = position.coords.latitude;
            var lng = position.coords.longitude;
            console.log("Latitude: " + lat + "\nLongitude: " + lng);
            window.location.href = '/your_callback_endpoint?lat='+lat+'&lng='+lng
        });
    } else {
        console.log("Geolocation is not supported by this browser.");
    }
    </script>
    """, unsafe_allow_html=True)
    
    lat,lng = get_location()
    st.write("Your Location:", lat, lng)

if __name__ == "__main__":
    main()