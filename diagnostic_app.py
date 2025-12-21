import streamlit as st
from datetime import datetime, date
import json

# --- Page Config ---
st.set_page_config(page_title="Service Master", page_icon="💻", layout="centered")

def main():
    # --- CSS Styles (Windows 11 Fluent Design - FORCE LIGHT) ---
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Segoe+UI&display=swap');

        /* 1. FORCE LIGHT THEME AT ROOT LEVEL */
        :root {
            color-scheme: light !important;
        }

        /* 2. Global Layout & Fonts */
        .stApp {
            background-color: #F3F3F3 !important;
            color: #000000 !important;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
            direction: rtl; /* Right-to-Left layout */
            text-align: right;
        }

        /* 3. Text Styling - Force Black */
        h1, h2, h3, h4, h5, p, label, .stMarkdown, .stText, div, span, li, b, strong {
            color: #000000 !important;
            text-align: right;
        }
        h1 {
            text-align: center !important;
            color: #0078D4 !important;
            font-weight: 600;
        }

        /* 4. EXPANDERS */
        .streamlit-expanderHeader {
            background-color: #FFFFFF !important;
            color: #000000 !important;
            border: 1px solid #D1D1D1 !important;
            border-radius: 4px !important;
        }
        div[data-testid="stExpander"] details summary {
            background-color: #FFFFFF !important;
            color: #000000 !important;
        }
        div[data-testid="stExpander"] details summary:hover {
            background-color: #F9F9F9 !important;
            color: #000000 !important;
        }
        div[data-testid="stExpander"] svg {
            fill: #000000 !important;
        }
        .streamlit-expanderContent {
            background-color: #FAFAFA !important;
            border: 1px solid #D1D1D1 !important;
            border-top: none !important;
            color: #000000 !important;
        }

        /* 5. CODE BLOCKS */
        [data-testid="stCodeBlock"] {
            background-color: #FFFFFF !important;
            border: 1px solid #D1D1D1 !important;
            border-radius: 4px !important;
            margin-bottom: 1rem;
        }
        [data-testid="stCodeBlock"] pre {
            background-color: #FFFFFF !important;
        }
        [data-testid="stCodeBlock"] code {
            color: #000000 !important;
            background-color: #FFFFFF !important;
            font-family: 'Consolas', monospace !important;
        }
        [data-testid="stCodeBlock"] span {
            color: #000000 !important;
        }
        [data-testid="stCopyButton"] {
            color: #000000 !important;
        }
        [data-testid="stCopyButton"] svg {
            fill: #000000 !important;
        }

        /* 6. INPUTS */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea {
            background-color: #FFFFFF !important;
            color: #000000 !important;
            border: 1px solid #D1D1D1 !important;
            border-bottom: 2px solid #D1D1D1 !important;
            border-radius: 4px !important;
        }
        ::placeholder {
            color: #666 !important;
            opacity: 1 !important;
        }

        /* 7. DROPDOWNS */
        div[data-baseweb="select"] > div {
            background-color: #FFFFFF !important;
            color: #000000 !important;
            border: 1px solid #D1D1D1 !important;
        }
        div[data-baseweb="select"] span {
            color: #000000 !important;
        }
        div[data-baseweb="select"] svg {
            fill: #000000 !important;
        }
        div[data-baseweb="popover"], div[data-baseweb="menu"], ul[data-baseweb="menu"] {
            background-color: #FFFFFF !important;
            border: 1px solid #D1D1D1 !important;
        }
        li[role="option"] {
            background-color: #FFFFFF !important;
            color: #000000 !important;
            text-align: right !important;
            direction: rtl !important;
        }
        li[role="option"]:hover {
            background-color: #E6F7FF !important;
        }

        /* 8. BUTTONS */
        .stButton > button {
            background-color: #0078D4 !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 4px !important;
            font-weight: 600 !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .stButton > button:hover {
            background-color: #0067C0 !important;
        }
        .stButton > button p {
            color: #FFFFFF !important;
        }

        /* 9. Link Buttons */
        .stLinkButton a {
            background-color: #0078D4 !important;
            color: #FFFFFF !important;
            border-radius: 4px !important;
            text-decoration: none !important;
            display: inline-block;
            padding: 0.5rem 1rem;
        }
        .stLinkButton a:hover {
            color: #FFFFFF !important;
        }
        
        /* 10. Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 5px;
        }
        .stTabs [data-baseweb="tab"] {
            background-color: #FFFFFF;
            border-radius: 4px;
            color: #000000;
        }
        .stTabs [aria-selected="true"] {
            background-color: #E6F7FF !important;
            color: #0078D4 !important;
            font-weight: bold;
        }

        /* Hide Streamlit Menu */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

    # --- HEADER ---
    st.title("🛡️ מערכת חכמה לניהול תקלות")
    st.markdown("<h5 style='text-align: center; color: #666 !important;'>מותאמת ללקוח (Service Master)</h5>", unsafe_allow_html=True)
    st.markdown("---")

    # ==========================================
    # 1. IDENTIFICATION
    # ==========================================
    st.markdown("### 1️⃣ זיהוי הלקוח והציוד")
    
    with st.expander("❓ איפה מוצאים את המספר הסידורי (S/N)?"):
        st.info("בדרך כלל זו מדבקה לבנה בתחתית המחשב הנייד או בגב המחשב הנייח.")
        
        st.markdown("**אם המחשב דולק, ניתן למצוא דרך הטרמינל (PowerShell):**")
        st.markdown("""
        <div style="background-color: #E6F7FF; padding: 10px; border-radius: 4px; border: 1px solid #91D5FF; color: black; margin-bottom: 10px;">
        <strong>איך לפתוח?</strong> לחץ <b>קליק ימני</b> על כפתור <b>"התחל" (Start)</b> ובחר <b>Windows Terminal</b> או <b>PowerShell</b>.
        </div>
        """, unsafe_allow_html=True)
        
        # New PowerShell command for SerialNumber
        st.code("(Get-CimInstance Win32_BIOS).SerialNumber", language="powershell")
        
        st.markdown("**או צלם את המדבקה למטה:**")

    col1, col2 = st.columns(2)
    with col1:
        client_name = st.text_input("שם לקוח / ארגון")
    with col2:
        serial_number = st.text_input("מספר סידורי (S/N)", help="למשל: 5CD1234567")

    if not serial_number:
        with st.expander("📷 לחץ כאן לצילום המספר הסידורי"):
            st.info("💡 בטלפון נייד: ניתן להחליף מצלמה (קדמית/אחורית) בכפתור בתוך המצלמה.")
            start_cam = st.checkbox("הפעל מצלמה", key="cam_sn")
            if start_cam:
                sn_photo = st.camera_input("צלם את המדבקה", key="sn_img")
                if sn_photo:
                    st.success("התמונה נשמרה!")

    device_type = st.selectbox(
        "סוג המכשיר:",
        ["", "מחשב נייד (Laptop)", "מחשב נייח (PC)", "מחשב הכל-באחד (AIO)", "שרת (Server)", "רכיב (Component)"]
    )

    if not device_type:
        st.info("נא לבחור סוג מכשיר כדי להמשיך.")
        st.stop()

    # Data collection containers
    priority = "Normal"
    is_critical_damage = False
    is_wrong_item = False

    # ==========================================
    # 2. HISTORY & WINDOWS TOOLS
    # ==========================================
    with st.expander("📅 היסטוריה וכלים ל-Windows", expanded=True):
        st.markdown("**האם זה המוצר הנכון?**")
        wrong_item = st.radio("בדיקת משלוח:", ["כן, זה מה שהזמנתי", "לא, קיבלתי דגם אחר"], label_visibility="collapsed")
        
        if "לא" in wrong_item:
            st.error("📦 עצור: טעות במשלוח. נא לא לפתוח את האריזה.")
            is_wrong_item = True
            priority = "Logistics Error"
        
        st.markdown("---")
        col_h1, col_h2 = st.columns(2)
        with col_h1:
            received_date = st.date_input("תאריך קבלה", value=date.today())
        with col_h2:
            first_boot = st.date_input("תאריך הפעלה ראשונה", value=date.today())
            
        initial_status = st.radio("מצב ראשוני:", ["עבד תקין", "לא עבד מההתחלה (DOA)"])
        if "DOA" in initial_status:
            st.warning("🚨 שים לב: תקלת DOA (Dead On Arrival).")
            priority = "Critical (DOA)"

        st.markdown("---")
        st.markdown("#### 🛠️ כלי עזר לטכנאי (Windows)")
        
        # Updated Tabs with new functionality
        t1, t2, t3, t4 = st.tabs(["🔑 מפתח מוצר", "🔄 שינוי גרסה", "⚙️ לוח הבקרה", "♻️ איפוס"])
        
        with t1:
            st.caption("פתיחת PowerShell (קליק ימני על התחל):")
            st.code("(Get-CimInstance SoftwareLicensingService).OA3xOriginalProductKey", language="powershell")
        
        with t2:
            st.markdown("##### שדרוג מ-Home ל-Pro")
            st.markdown("""
            1. **חובה:** נתק את האינטרנט!
            2. לך ל: `הגדרות` > `מערכת` > `הפעלה` > `שנה מפתח מוצר`.
            3. הכנס את המפתח הגנרי:
            """)
            st.code("VK7JG-NPHTM-C97JM-9MPGT-3V66T", language="text")
            st.markdown("4. המחשב יעשה ריסט. לאחר מכן חבר אינטרנט והכנס את המפתח החוקי.")

        with t3:
            st.caption("פתיחת לוח הבקרה הישן (Control Panel):")
            st.code("control", language="bash")
            st.caption("לחץ Win+R והדבק את הפקודה.")

        with t4:
            st.caption("איפוס למצב יצרן (Reset):")
            st.code("systemreset --factoryreset", language="bash")
            st.caption("לחץ Win+R והדבק את הפקודה.")

    if is_wrong_item:
        st.warning("התהליך נעצר עקב טעות במשלוח.")
        st.stop()

    # ==========================================
    # 3. PHYSICAL INSPECTION
    # ==========================================
    st.markdown("### 2️⃣ בדיקה חיצונית")
    has_damage = st.radio("האם יש נזק פיזי?", ["לא, נראה שלם", "כן, יש שבר/מכה"])
    
    visual_report = {}
    if "כן" in has_damage:
        priority = "High (Physical)"
        st.error("🛑 זוהה נזק פיזי. נדרש תיקון חומרה.")
        is_critical_damage = True
        
        damage_list = st.multiselect("פירוט הנזק:", ["מסך שבור", "שקע טעינה", "נוזלים/קורוזיה", "פלסטיקה שבורה"])
        box_status = st.selectbox("מצב הקופסה:", ["תקינה", "מעוכה/קרועה"])
        
        if "מעוכה" in box_status:
            st.warning("📦 חשוב: צלם את הקופסה לביטוח!")

        with st.expander("📷 צילום הנזק (פתח מצלמה)"):
            st.info("ניתן להחליף מצלמה בכפתור המובנה בממשק.")
            start_dmg_cam = st.checkbox("הפעל מצלמה", key="cam_dmg")
            if start_dmg_cam:
                dmg_img = st.camera_input("צלם נזק", key="dmg_cap")
                
        visual_report = {"damages": damage_list, "box": box_status}

    # ==========================================
    # 4. POWER CHECK
    # ==========================================
    st.markdown("### 3️⃣ בדיקת חשמל")
    if "נייד" in device_type or "AIO" in device_type:
        original_charger = st.radio("האם המטען מקורי?", ["כן", "לא / אוניברסלי"], horizontal=True)
        
        # New Voltage Check
        voltage_match = st.radio(
            "האם המתח (V) והזרם (A) הרשומים על המטען תואמים למדבקה על המחשב?", 
            ["כן, תואם", "לא / לא בטוח"], 
            horizontal=True
        )
        
        if voltage_match == "לא / לא בטוח":
            st.warning("⚠️ מתח לא תואם עלול לגרום לנזק לרכיבים או לבעיות טעינה.")

    # ==========================================
    # 5. SYMPTOMS & ANYDESK
    # ==========================================
    diag_report = {}
    if not is_critical_damage:
        st.markdown("### 4️⃣ בעית תוכנה")
        symptom = st.selectbox("מה התקלה?", ["לא נדלק", "מסך כחול", "איטי", "בעית תוכנה"])
        
        if symptom in ["איטי", "בעית תוכנה"]:
            st.info("ננסה להתחבר מרחוק.")
            has_net = st.checkbox("יש אינטרנט במחשב?")
            if has_net:
                st.success("מעולה! הורד את תוכנת התמיכה:")
                st.link_button("⬇️ הורד תוכנת תמיכה - המלצה על AnyDesk", "https://150.co.il/")
                st.text_input("הקלד את המספר (ID) שמופיע בתוכנה:")

    # ==========================================
    # 6. SUMMARY & REPORT
    # ==========================================
    st.markdown("---")
    st.markdown("### 🏁 סיום")
    notes = st.text_area("הערות נוספות:")

    if st.button("שלח טופס (Generate Ticket)"):
        # Create Data Structure
        ticket = {
            "meta": {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "client": client_name,
                "sn": serial_number,
                "device": device_type
            },
            "history": {
                "doa": initial_status,
                "software": software_changes
            },
            "physical": visual_report,
            "priority": priority,
            "notes": notes
        }
        
        st.success("✅ הטופס נשלח בהצלחה!")
        st.json(ticket)
        
        # HTML Report Generation
        html_report = f"""
        <div dir="rtl" style="font-family: sans-serif; padding: 20px;">
            <h1 style="color: #0078D4;">דוח שירות: {client_name}</h1>
            <hr>
            <p><strong>תאריך:</strong> {ticket['meta']['date']}</p>
            <p><strong>מספר סידורי:</strong> {ticket['meta']['sn']}</p>
            <p><strong>מכשיר:</strong> {ticket['meta']['device']}</p>
            <p><strong>סטטוס DOA:</strong> {ticket['history']['doa']}</p>
            <p><strong>עדיפות:</strong> {ticket['priority']}</p>
            <div style="background: #eee; padding: 10px; margin-top: 10px;">
                <strong>הערות:</strong> {notes}
            </div>
        </div>
        """
        
        st.download_button(
            "📄 הורד דוח (HTML/PDF)",
            data=html_report,
            file_name=f"Report_{serial_number}.html",
            mime="text/html"
        )

if __name__ == "__main__":
    main()