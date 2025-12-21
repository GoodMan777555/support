import streamlit as st
from datetime import datetime, date

# --- הגדרות עמוד (Page Settings) ---
st.set_page_config(page_title="Service Master - Windows 11 Style", page_icon="💻", layout="centered")

def main():
    # --- עיצוב בסגנון Windows 11 (Fluent Design CSS) ---
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Segoe+UI&display=swap');

        /* 1. FORCE LIGHT THEME AT ROOT LEVEL */
        :root {
            color-scheme: light !important;
        }

        /* 2. Global Reset */
        .stApp {
            background-color: #F3F3F3 !important;
            color: #000000 !important;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
            direction: rtl !important;
            text-align: right !important;
        }

        /* 3. Text Visibility Override */
        h1, h2, h3, h4, h5, h6, p, span, div, label, li, a, .stMarkdown, .stText, b, strong {
            color: #000000 !important;
            text-align: right !important;
        }

        h1 { text-align: center !important; }

        /* 4. CUSTOM CODE BOX STYLE (HTML) */
        .custom-code-box {
            background-color: #FFFFFF !important;
            border: 1px solid #0078D4 !important; /* Blue border to stand out */
            color: #000000 !important;
            padding: 10px;
            border-radius: 4px;
            font-family: 'Consolas', monospace;
            direction: ltr !important; /* Code is LTR */
            text-align: left !important;
            margin-bottom: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }

        /* 5. EXPANDERS */
        .streamlit-expanderHeader {
            background-color: #FFFFFF !important;
            color: #000000 !important;
            border: 1px solid #D1D1D1 !important;
            border-radius: 4px !important;
            direction: rtl !important;
        }
        .streamlit-expanderContent {
            background-color: #FAFAFA !important;
            color: #000000 !important;
            border: 1px solid #D1D1D1 !important;
            border-top: none !important;
            direction: rtl !important;
        }
        div[data-testid="stExpander"] details summary {
            background-color: #FFFFFF !important;
            color: #000000 !important;
        }
        div[data-testid="stExpander"] svg {
            fill: #000000 !important;
        }

        /* 6. INPUT FIELDS */
        input, textarea, select {
            background-color: #FFFFFF !important;
            color: #000000 !important;
            caret-color: #000000 !important;
            text-align: right !important;
            direction: rtl !important;
        }
        .stTextInput > div > div, 
        .stTextArea > div > div, 
        .stNumberInput > div > div, 
        .stDateInput > div > div {
            background-color: #FFFFFF !important;
            color: #000000 !important;
            border: 1px solid #D1D1D1 !important;
            border-radius: 4px !important;
            direction: rtl !important;
        }

        /* 7. DROPDOWNS */
        div[data-baseweb="select"] > div {
            background-color: #FFFFFF !important;
            color: #000000 !important;
            border: 1px solid #D1D1D1 !important;
            direction: rtl !important;
        }
        div[data-baseweb="popover"], div[data-baseweb="menu"], ul[data-baseweb="menu"] {
            background-color: #FFFFFF !important;
            direction: rtl !important;
            text-align: right !important;
        }
        li[role="option"] {
            background-color: #FFFFFF !important;
            color: #000000 !important;
            text-align: right !important;
            direction: rtl !important;
        }
        li[role="option"]:hover {
            background-color: #E5E5E5 !important;
        }

        /* 8. BUTTONS */
        .stButton button {
            background-color: #0078D4 !important;
            border: none !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
        }
        .stButton button p, .stButton button span {
            color: #FFFFFF !important;
        }
        
        /* 9. ALERTS */
        .stAlert {
            background-color: #FFFFFF !important;
            border: 1px solid #D1D1D1 !important;
            direction: rtl !important;
            text-align: right !important;
        }
        
        /* 10. ICONS & TABS */
        div[data-baseweb="select"] svg, div[data-testid="stDateInput"] svg {
            fill: #000000 !important;
            color: #000000 !important;
        }
        .stTabs [data-baseweb="tab-list"] {
            background-color: #FFFFFF !important;
        }
        .stTabs [data-baseweb="tab"] {
            color: #000000 !important;
            background-color: #FFFFFF !important;
        }
        .stTabs [aria-selected="true"] {
            background-color: #E1DFDD !important;
        }
        img {
            margin-left: auto;
            margin-right: 0;
        }

        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

    # כותרות (Main Title)
    st.title("🛡️ מערכת חכמה לניהול תקלות - מותאמת ללקוח")
    
    # ==========================================
    # חלק 1: זיהוי וציוד (Identification)
    # ==========================================
    st.markdown("### 1️⃣ זיהוי הלקוח והציוד")
    
    with st.expander("❓ איפה מוצאים את המספר הסידורי (S/N)?"):
        st.info("בדרך כלל זו מדבקה לבנה בתחתית המחשב הנייד או בגב המחשב הנייח.")
        
        st.markdown("**אם המחשב דולק, ניתן למצוא את המספר דרך שורת הפקודה (CMD):**")
        
        # Инструкция CMD
        st.markdown("""
        <div style="background-color: #E6F7FF; padding: 10px; border-radius: 5px; border: 1px solid #1890FF; margin-bottom: 5px; color: black;">
        <strong>איך לפתוח?</strong> לחץ על <kbd>Win</kbd> + <kbd>R</kbd>, הקלד <code>cmd</code> ולחץ <strong>Enter</strong>.
        </div>
        """, unsafe_allow_html=True)
        
        # ВМЕСТО ST.CODE ИСПОЛЬЗУЕМ HTML (Гарантированно белый фон)
        st.markdown("""
        <div class="custom-code-box">
        wmic bios get serialnumber
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**אם קשה לקרוא את המספר, ניתן לצלם אותו בשלב הבא.**")

    col1, col2 = st.columns(2)
    with col1:
        client_name = st.text_input("שם לקוח / ארגון")
    with col2:
        serial_number = st.text_input(
            "מספר סידורי (S/N)",
            help="נמצא על מדבקה לבנה, מתחיל בדרך כלל ב-SN, S/N או Service Tag"
        )

    if not serial_number:
        st.caption("או צלם את המדבקה אם קשה לקרוא את הכתב:")
        with st.expander("📷 לחץ כאן כדי לצלם (פתח מצלמה)"):
            start_sn_cam = st.checkbox("הפעל מצלמה (Start Camera)", key="start_sn_cam")
            if start_sn_cam:
                sn_photo = st.camera_input("צלם מדבקת מספר סידורי", key="sn_cam")
                if sn_photo:
                    st.success("תמונה נקלטה! הטכנאי יפענח את המספר.")

    device_type = st.selectbox(
        "איזה מכשיר יש ברשותך?",
        ["", "מחשב נייד (Laptop)", "מחשב נייח (PC)", "מחשב הכל-באחד (All-in-One)", "שרת (Server)", "רכיב בודד (כרטיס/מעבד)"],
        index=0
    )

    if not device_type:
        st.info("אנא בחר את סוג המכשיר כדי להמשיך.")
        st.stop()

    ticket_data = {}
    priority = "רגיל"
    is_critical_damage = False
    is_wrong_item = False

    # ==========================================
    # חלק 2: היסטוריה ותאימות הזמנה
    # ==========================================
    with st.expander("📅 היסטוריית המכשיר (מתי הגיעה, מה קרה)", expanded=True):
        
        st.markdown("**בדיקת המוצר שקיבלת:**")
        wrong_item_check = st.radio(
            "האם זה המוצר שהזמנת?",
            ("כן, זה המוצר הנכון", "לא - קיבלתי דגם אחר ממה שהזמנתי")
        )

        if wrong_item_check == "לא - קיבלתי דגם אחר ממה שהזמנתי":
            st.error("📦 **עצור:** נראה שיש טעות במשלוח. נא לא לפתוח את האריזה! נציג יצור קשר להחלפה.")
            priority = "לוגיסטיקה (טעות במשלוח)"
            is_wrong_item = True
        
        st.markdown("---")
        
        col_h1, col_h2 = st.columns(2)
        with col_h1:
            received_date = st.date_input("מתי קיבלת את המכשיר?", value=date.today())
        with col_h2:
            first_boot_date = st.date_input("מתי הדלקת אותו לראשונה?", value=date.today())

        initial_state = st.radio(
            "האם המכשיר עבד בהתחלה?", 
            ("כן, עבד תקין", "לא - המכשיר הגיע מקולקל (לא נדלק ישר מהקופסה)", "לא יודע / לא אני פתחתי")
        )

        if initial_state == "לא - המכשיר הגיע מקולקל (לא נדלק ישר מהקופסה)":
            st.warning("🚨 **תקלת DOA (מקולקל מהאריזה):** אנא שמור את כל הניילונים והקופסה להחלפה.")
            priority = "קריטי (DOA)"

        st.markdown("---")
        software_changes = st.selectbox(
            "האם התקנת משהו לפני שהתקלה קרתה?",
            ["לא, השתמשתי רגיל", "התקנתי תוכנה או משחק חדש", "ניסיתי להתקין ווינדוס מחדש", "עדכון ביוס (BIOS)", "לא יודע / לא בטוח"]
        )

        st.markdown("---")
        st.markdown("#### 🛠️ כלי עזר ל-Windows")
        
        tab_key, tab_edition = st.tabs(["🔑 מציאת מפתח מוצר", "🔄 שינוי גרסה (Edition)"])
        
        with tab_key:
            st.markdown("""
            <div style="background-color: #E6F7FF; padding: 10px; border-radius: 5px; border: 1px solid #1890FF; margin-bottom: 5px; color: black;">
            <strong>פתח PowerShell:</strong> <kbd>Win</kbd> + <kbd>X</kbd> ➜ בחר <strong>Windows PowerShell</strong>
            </div>
            """, unsafe_allow_html=True)
            
            # HTML CODE BLOCK
            st.markdown("""
            <div class="custom-code-box">
            wmic path softwarelicensingservice get OA3xOriginalProductKey
            </div>
            """, unsafe_allow_html=True)
        
        with tab_edition:
            st.markdown("""
            <div style="margin-bottom: 5px;">
            <strong>שדרוג מ-Home ל-Pro (מפתח גנרי):</strong>
            </div>
            """, unsafe_allow_html=True)
            
            # HTML CODE BLOCK
            st.markdown("""
            <div class="custom-code-box">
            VK7JG-NPHTM-C97JM-9MPGT-3V66T
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            **הוראות:**
            1. נתק אינטרנט.
            2. לך ל: **הגדרות > עדכון ואבטחה > הפעלה**.
            3. לחץ **"שנה מפתח מוצר"** והדבק את הקוד.
            """)

    if is_wrong_item:
        st.warning("⚠️ הדיאגנוסטיקה הסתיימה עקב טעות במשלוח.")
    else:
        # ==========================================
        # חלק 3: בדיקה ויזואלית (Visual Inspection)
        # ==========================================
        st.markdown("### 2️⃣ בדיקה חיצונית")
        has_damage = st.radio("הסתכל על המכשיר מכל הצדדים - האם רואים נזק?", ("לא, נראה שלם", "כן, יש שבר או מכה"))

        visual_report = {}

        if has_damage == "כן, יש שבר או מכה":
            priority = "גבוה (נזק פיזי)"
            damage_options = []
            if "נייד" in device_type:
                damage_options = ["מסך שבור / סדוק", "פלסטיק שבור", "צירים עקומים", "נשפכו מים/קפה", "שקע טעינה רופף"]
            elif "שרת" in device_type:
                damage_options = ["אוזני ברזל עקומות", "מכה בפח", "חיבורים שבורים"]
            elif "רכיב" in device_type:
                damage_options = ["פינים עקומים", "חלקים תלושים", "סימני שרוף"]
            else:
                damage_options = ["מכה בגוף המחשב", "זכוכית שבורה", "יציאות USB שבורות"]

            specific_damage = st.multiselect("מה בדיוק ניזוק? (אפשר לבחור כמה)", damage_options)
            critical_markers = ["מסך שבור / סדוק", "נשפכו מים/קפה", "סימני שרוף", "פינים עקומים"]
            if any(item in specific_damage for item in critical_markers):
                is_critical_damage = True
                st.error("🛑 **נזק קריטי זוהה:** נראה שהמחשב דורש תיקון פיזי במעבדה. אין טעם להמשיך בשאלות תוכנה.")

            box_condition = st.radio("באיזה מצב הקופסה החיצונית?", ["שלמה ותקינה", "מעוכה קצת", "קרועה / רטובה / חור בקרטון", "זרקתי את הקופסה"])
            if "קרועה" in box_condition:
                st.warning("📦 **חשוב:** צלם את הקרטון! זה יעזור לנו מול חברת המשלוחים.")

            st.write("📷 **תיעוד הנזק:**")
            dmg_photo_cam = None
            with st.expander("📷 לחץ כאן כדי לצלם תמונה (פתח מצלמה)"):
                start_dmg_cam = st.checkbox("הפעל מצלמה (Start Camera)", key="start_dmg_cam")
                if start_dmg_cam:
                    dmg_photo_cam = st.camera_input("צלם את הנזק", key="dmg_cam")

            dmg_photo_file = st.file_uploader("או בחר קובץ מהגלריה", accept_multiple_files=True)
            visual_report = {
                "damage_details": specific_damage,
                "box_status": box_condition,
                "photos_attached": bool(dmg_photo_cam or dmg_photo_file)
            }

        st.markdown("### 3️⃣ חיבורים לחשמל ולמסך")
        power_report = {}

        if "נייד" in device_type or "הכל-באחד" in device_type:
            st.write("בדיקת מטען:")
            is_original = st.radio("האם אתה משתמש במטען המקורי שהגיע בקופסה?", ("כן", "לא - מטען אחר / אוניברסלי"))
            if st.checkbox("יש לי מטען עם חיבור USB-C (החיבור האליפטי הקטן)"):
                st.info("💡 **טיפ:** נסה לחבר את המטען הזה לטלפון שלך.")
                phone_test = st.radio("האם הטלפון מראה שהוא נטען?", ("כן, הטלפון נטען", "לא, אין תגובה"))
                if phone_test == "לא, אין תגובה":
                    st.error("❌ נראה שהמטען מקולקל. ייתכן שהמחשב תקין ורק צריך מטען חדש.")
                    power_report['adapter_status'] = "Dead"

        if "נייח" in device_type:
            has_gpu = st.radio("האם יש למחשב כרטיס מסך נפרד (לגיימינג/עריכה)?", ("כן", "לא / לא יודע"))
            if has_gpu == "כן":
                st.markdown("#### 🔌 איפה חיברת את כבל המסך?")
                st.caption("זוהי הטעות הנפוצה ביותר! השווה לתמונות למטה:")
                col_img1, col_img2 = st.columns(2)
                with col_img1:
                    st.image("https://placehold.co/400x300/ffcccc/red?text=Motherboard+(WRONG)", caption="❌ חיבור למעלה (לוח אם) - לא נכון")
                with col_img2:
                    st.image("https://placehold.co/400x300/ccffcc/green?text=GPU+Card+(CORRECT)", caption="✅ חיבור למטה (כרטיס מסך) - נכון!")

                cable_pos = st.radio("איפה הכבל מחובר אצלך?", ("כמו בתמונה הימנית (למטה - כרטיס מסך)", "כמו בתמונה השמאלית (למעלה - לוח אם)"))
                if cable_pos == "כמו בתמונה השמאלית (למעלה - לוח אם)":
                    st.warning("💡 **נמצאה הבעיה האפשרית!** כאשר מחברים את המסך לחיבור העליון, המחשב לא משתמש בכרטיס המסך ולכן אין תמונה. נא להעביר את הכבל לחיבורים התחתונים (האופקיים) ולעשות ריסט.")
                    st.stop()

        diag_report = {}
        if not is_critical_damage:
            st.markdown("### 4️⃣ אבחון תוכנה")
            boot_status = st.selectbox(
                "לחץ על כפתור ההפעלה. מה אתה רואה?",
                ["כלום - שקט מוחלט, אין אורות", "המחשב מרעיש, אבל המסך נשאר שחור", "הווינדוס מתחיל להיטען ואז נתקע", "מסך כחול עם כיתוב לבן (שגיאה)", "המחשב איטי / מרעיש / מתחמם", "אחר / לא יודע להסביר"]
            )
            
            if boot_status in ["הווינדוס מתחיל להיטען ואז נתקע", "המחשב איטי / מרעיש / מתחמם", "אחר / לא יודע להסביר"]:
                st.info("ℹ️ נראה שהמחשב עובד חלקית. אולי נוכל לתקן מרחוק בלי שתגיע למעבדה!")
                can_remote = st.radio("האם יש לך אינטרנט במחשב הזה?", ("לא - אין אינטרנט / לא נכנס לווינדוס", "כן - יש אינטרנט"))
                if can_remote == "כן - יש אינטרנט":
                    st.success("✅ מעולה! אנא הורד את תוכנת התמיכה כדי שנוכל להתחבר.")
                    st.link_button("⬇️ הורד תוכנת תמיכה", "https://150.co.il/")
                    st.text_input("הקלד כאן את המספר שמופיע בתוכנה (ID):")
                    diag_report['remote_available'] = True
                else:
                    diag_report['remote_available'] = False
            
            if "מסך שחור" in boot_status:
                beeps = st.text_input("האם שמעת צפצופים מהמחשב? (אם כן, נסה לתאר)", placeholder="למשל: 3 צפצופים קצרים")
                diag_report['beeps'] = beeps
            
            elif "מסך כחול" in boot_status:
                 diag_report['error_code'] = st.text_input("אם רשום קוד שגיאה באנגלית, הקלד אותו כאן:", placeholder="למשל: CRITICAL_PROCESS_DIED")

        else:
            st.markdown("---")
            st.info("ℹ️ הדיאגנוסטיקה הסתיימה (נזק פיזי).")

    st.markdown("---")
    st.markdown("### 🏁 סיכום ושליחה")
    notes = st.text_area("האם יש עוד משהו שחשוב שנדע?")

    if st.button("שלח טופס לטיפול"):
        final_ticket = {
            "meta": {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "client": client_name,
                "sn": serial_number,
                "device": device_type
            },
            "logistics": {
                "wrong_item": is_wrong_item,
                "box_status": locals().get('box_condition', 'N/A')
            },
            "history": {
                "doa_status": locals().get('initial_state', 'N/A'),
                "software_changes": locals().get('software_changes', 'N/A')
            },
            "physical_inspection": locals().get('visual_report', 'N/A'),
            "diagnosis": locals().get('diag_report', {}),
            "priority": priority,
            "notes": notes
        }

        if priority == "קריטי (DOA)" or is_wrong_item:
            st.error(f"🚨 הטופס נשלח בדחיפות גבוהה: {priority}")
        elif is_critical_damage:
            st.warning("🛠️ הטופס נשלח: המכשיר יועבר למעבדת חומרה לתיקון פיזי.")
        else:
            st.success("✅ הטופס נשלח בהצלחה! ניצור איתך קשר בהקדם.")

        st.json(final_ticket)

if __name__ == "__main__":
    main()