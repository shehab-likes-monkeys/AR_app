import streamlit as st
import streamlit.components.v1 as components
import qrcode
from io import BytesIO

st.set_page_config(page_title="3D Model with AR", layout="centered")

# Hosted model links (replace with your own!)
glb_url = "https://modelviewer.dev/shared-assets/models/Astronaut.glb"
usdz_url = "https://modelviewer.dev/shared-assets/models/Astronaut.usdz"

st.title("🚀 3D Model with AR Preview")

# --- Embed <model-viewer> for 3D + AR ---
html_code = f"""
<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>

<model-viewer
  src="{glb_url}"
  ios-src="{usdz_url}"
  alt="3D model"
  ar
  camera-controls
  auto-rotate
  style="width: 100%; height: 500px; background-color: #f0f0f0;">
  <button slot="ar-button" style="
    background:#0a84ff;
    color:white;
    border:none;
    padding:10px 16px;
    border-radius:8px;
    font-size:16px;
    position:absolute;
    bottom:20px;
    left:50%;
    transform:translateX(-50%);
  ">👀 View in your space</button>
</model-viewer>
"""

components.html(html_code, height=550)

# --- QR Code Section ---
st.subheader("📱 Scan to View in Browser")

# The trick: point QR to THIS streamlit app's public URL
# (example below assumes it's deployed to Streamlit Cloud)
app_url = "https://your-streamlit-app.streamlit.app"  # 👈 change this after deployment

qr = qrcode.QRCode(box_size=8, border=2)
qr.add_data(app_url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
buf = BytesIO()
img.save(buf, format="PNG")

st.image(buf.getvalue(), caption="Scan this to open the AR viewer in your phone browser")
