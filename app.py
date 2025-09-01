import streamlit as st
import streamlit.components.v1 as components
import qrcode
from io import BytesIO

st.set_page_config(page_title="3D Model with AR", layout="centered")

# ---------------------------------------------------------------------
# 🔹 Replace these links with YOUR model URLs
glb_url = "https://modelviewer.dev/shared-assets/models/Astronaut.glb"
usdz_url = "https://modelviewer.dev/shared-assets/models/Astronaut.usdz"

# 🔹 Your Streamlit Cloud public app URL
app_url = "https://ar-app.streamlit.app/"
# ---------------------------------------------------------------------

st.title("🚀 3D Model with AR Preview")

# --- Embed <model-viewer> ---
html_code = f"""
<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>

<model-viewer
  src="{glb_url}"
  ios-src="{usdz_url}"
  alt="3D model"
  ar
  ar-scale="fixed"
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

# --- Detect device type ---
browser_info = st.runtime.get_browser_info()
user_agent = browser_info.get("user_agent", "").lower()

is_mobile = any(m in user_agent for m in ["iphone", "android", "ipad"])

# --- Show QR only on desktop ---
if not is_mobile:
    st.subheader("📱 Scan to View in Browser")

    qr = qrcode.QRCode(box_size=8, border=2)
    qr.add_data(app_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buf = BytesIO()
    img.save(buf, format="PNG")

    st.image(buf.getvalue(), caption="Scan this to open the AR viewer on your phone")

