import streamlit as st
from datetime import datetime, date

# --- הגדרות עמוד ---
st.set_page_config(page_title="Service Master - עברית", page_icon="🛡️", layout="centered")

def main():
    st.title("🛡️ אשף קליטה ודיאגנוסטיקה")
    st.markdown("**מערכת מאוחדת לניהול תקלות חומרה ותוכנה**")
    st.markdown("---")

    # ==========================================
    # חלק 1: זיהוי וציוד
    # ==========================================
    st.subheader("1️⃣ פרטי הציוד והלקוח")
    col1, col2 = st.columns(2)
    with col1:
        client_name = st.text_input("שם לקוח / ארגון")
    with col2:
        serial_number = st.text_input("מספר סידורי (S/N)")

    device_type = st.selectbox(
        "סוג הציוד:",
        ["", "מחשב נייד (Laptop)", "מחשב נייח / תחנת עבודה (PC)", "מחשב הכל-באחד (All-in-One)", "שרת (Enterprise Server)", "רכיבים בודדים (CPU/MB/GPU)"],
        index=0
    )

    if not device_type:
        st.info("נא לבחור סוג ציוד כדי להתחיל.")
        st.stop()

    # משתנים לאיסוף נתונים
    ticket_data = {}
    priority = "רגיל"
    is_critical_damage = False  # דגל לעצירת שאלות מיותרות (Stop-Factor)
    is_wrong_item = False       # דגל לטעות במשלוח

    # ==========================================
    # חלק 2: היסטוריה ותאימות הזמנה (חדש!)
    # ==========================================
    with st.expander("📅 היסטוריה, תאימות הזמנה ו-DOA", expanded=True):
        
        # --- בדיקת תאימות הזמנה (חדש) ---
        st.markdown("**בדיקת משלוח:**")
        wrong_item_check = st.radio(
            "האם המוצר שקיבלת הוא המוצר שהזמנת?",
            ("כן, זה המוצר הנכון", "לא - קיבלתי דגם/מפרט שגוי")
        )

        if wrong_item_check == "לא - קיבלתי דגם/מפרט שגוי":
            st.error("📦 **טעות לוגיסטית:** סומן כטעות במשלוח. אין לפתוח את האריזה המקורית אם לא חייבים!")
            priority = "לוגיסטיקה (טעות במשלוח)"
            is_wrong_item = True
        
        st.markdown("---")
        
        col_h1, col_h2 = st.columns(2)
        with col_h1:
            received_date = st.date_input("תאריך קבלה", value=date.today())
        with col_h2:
            first_boot_date = st.date_input("תאריך הפעלה ראשונה", value=date.today())

        # בדיקת DOA
        initial_state = st.radio(
            "מצב המכשיר בעת הפעלה ראשונה (מהקופסה):", 
            ("עבד תקין", "DOA - לא עבד מהרגע הראשון", "לא ידוע / לא רלוונטי")
        )

        if initial_state == "DOA - לא עבד מהרגע הראשון":
            st.error("🚨 **שים לב: DOA!** חובה לשמור את כל האריזות.")
            priority = "קריטי (DOA)"

        # שינויי תוכנה
        software_changes = st.selectbox(
            "האם בוצעו שינויים לפני הופעת התקלה?",
            ["לא, עבדו רגיל", "התקנת תוכנה חדשה / משחק", "התקנה מחדש של מערכת הפעלה", "עדכון ביוס (BIOS Update)"]
        )

    # אם זה מוצר לא נכון, אין טעם לשאול על שריטות או חשמל
    if is_wrong_item:
        st.warning("⚠️ הדיאגנוסטיקה הטכנית נעצרה מכיוון שהתקבל מוצר שגוי.")
    else:
        # ==========================================
        # חלק 3: בדיקה ויזואלית (Visual Inspection)
        # ==========================================
        st.markdown("---")
        st.subheader("2️⃣ בדיקה ויזואלית (Visual Inspection)")
        
        has_damage = st.radio("האם יש נזק פיזי גלוי לעין?", ("לא, המצב נראה תקין", "כן, יש נזק פיזי"))

        visual_report = {}

        if has_damage == "כן, יש נזק פיזי":
            priority = "גבוה (נזק פיזי)"
            
            damage_options = []
            if device_type == "מחשב נייד (Laptop)":
                damage_options = ["שבר מסך", "סדקים בגוף", "צירים שבורים", "קורוזיה/נוזלים", "שקע טעינה שבור"]
            elif device_type == "שרת (Enterprise Server)":
                damage_options = ["אוזני עגינה עקומות", "מכות בשאסי", "פגיעה ב-Backplane", "תפסניות שבורות"]
            elif device_type == "רכיבים בודדים (CPU/MB/GPU)":
                damage_options = ["פינים עקומים (Socket)", "רכיבי SMD תלושים", "סימני חריכה", "שריטות על הלוח"]
            else:
                damage_options = ["מכות/שריטות", "זכוכית שבורה", "יציאות USB שבורות", "סימני פתיחה"]

            specific_damage = st.multiselect("פירוט הנזק:", damage_options)
            
            critical_markers = ["שבר מסך", "קורוזיה/נוזלים", "סימני חריכה", "פינים עקומים (Socket)", "רכיבי SMD תלושים"]
            
            if any(item in specific_damage for item in critical_markers):
                is_critical_damage = True
                st.error("🛑 **STOP-FACTOR:** נזק פיזי קריטי. הדיאגנוסטיקה תעצור כאן.")

            box_condition = st.radio("מצב האריזה (לביטוח משלוחים):", 
                ["אריזה מושלמת", "מעוכה/משופשפת", "קרועה/רטובה (נזק משלוח)", "ללא אריזה"])
            
            if box_condition == "קרועה/רטובה (נזק משלוח)":
                st.warning("📦 **חשוב:** צלם את הקרטון מיד!")

            uploaded_files = st.file_uploader("צרף תמונות נזק:", accept_multiple_files=True)
            
            visual_report = {
                "damage_details": specific_damage,
                "box_status": box_condition,
                "photos_count": len(uploaded_files) if uploaded_files else 0
            }

        # ==========================================
        # חלק 4: חשמל וחיבורים
        # ==========================================
        if not is_critical_damage:
            st.markdown("---")
            st.subheader("3️⃣ חשמל וחיבורים")

            power_report = {}

            if device_type in ["מחשב נייד (Laptop)", "מחשב הכל-באחד (All-in-One)"]:
                is_original = st.radio("האם המטען מקורי?", ("כן", "לא / אוניברסלי"))
                
                if st.checkbox("בדיקת מטען (Type-C בלבד)"):
                    st.info("חבר את המטען לטלפון נייד לבדיקה.")
                    phone_test = st.radio("האם הטלפון נטען?", ("כן", "לא"))
                    if phone_test == "לא":
                        st.error("❌ המטען תקול.")
                        power_report['adapter_status'] = "Dead"

            if device_type == "מחשב נייח / תחנת עבודה (PC)":
                has_gpu = st.radio("האם יש כרטיס מסך נפרד?", ("כן", "לא"))
                if has_gpu == "כן":
                    cable_pos = st.radio("לאן מחובר המסך?", ("לכרטיס המסך (למטה)", "ללוח האם (למעלה)"))
                    if cable_pos == "ללוח האם (למעלה)":
                        st.error("🛑 **שגיאה:** העבר את הכבל לכרטיס המסך!")
                        st.stop()

            if device_type in ["מחשב נייח / תחנת עבודה (PC)", "שרת (Enterprise Server)"]:
                standby = st.radio("חיבור לחשמל (ללא הפעלה) - מה קורה?", ["שקט מוחלט", "נורית בלוח דולקת", "נדלק לבד"])
                power_report['standby'] = standby

        # ==========================================
        # חלק 5: סימפטומים טכניים + חיבור מרחוק (חדש!)
        # ==========================================
        diag_report = {}

        if not is_critical_damage:
            st.markdown("---")
            st.subheader("4️⃣ תיאור התקלה ובדיקה מרחוק")
            
            boot_status = st.selectbox(
                "מה קורה בעת לחיצה על כפתור ההפעלה?",
                ["אין תגובה (מת)", "נדלק ללא תמונה", "נתקע בטעינת Windows", "מסך כחול (BSOD)", "איטיות / רעש / התחממות"]
            )
            
            # --- לוגיקת חיבור מרחוק (חדש!) ---
            # מציגים את זה רק אם המחשב מצליח להגיע למערכת הפעלה או נתקע בדרך
            remote_possible = False
            if boot_status in ["נתקע בטעינת Windows", "איטיות / רעש / התחממות"]:
                st.info("ℹ️ המערכת זיהתה שהמחשב נדלק.")
                can_remote = st.radio(
                    "האם יש אינטרנט וניתן להתחבר מרחוק לאבחון?",
                    ("לא - אין אינטרנט / לא נכנס למערכת", "כן - אפשר להתחבר (AnyDesk / TeamViewer)")
                )
                
                if can_remote == "כן - אפשר להתחבר (AnyDesk / TeamViewer)":
                    st.success("✅ מעולה! ציין בהערות את המספר להתחברות (ID).")
                    remote_possible = True
                    diag_report['remote_available'] = True
                else:
                    diag_report['remote_available'] = False
            
            # המשך דיאגנוסטיקה רגילה
            if boot_status == "נדלק ללא תמונה":
                beeps = st.text_input("האם יש צפצופים?")
                diag_report['beeps'] = beeps
            
            elif boot_status == "מסך כחול (BSOD)":
                 diag_report['error_code'] = st.text_input("קוד שגיאה (למשל 0x00..):")

        else:
            st.markdown("---")
            st.info("ℹ️ שלב אבחון תוכנה דולג עקב נזק פיזי קריטי.")
            diag_report['status'] = "Skipped due to Physical Damage"

    # ==========================================
    # חלק 6: סיום
    # ==========================================
    st.markdown("---")
    st.subheader("🏁 סיכום")
    
    notes = st.text_area("הערות נוספות / מזהה AnyDesk:")

    if st.button("צור קריאת שירות"):
        final_ticket = {
            "meta": {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "client": client_name,
                "sn": serial_number,
                "device": device_type
            },
            "logistics": {
                "wrong_item_received": is_wrong_item, # שדה חדש ב-JSON
                "box_status": locals().get('box_condition', 'N/A')
            },
            "history": {
                "doa_status": locals().get('initial_state', 'N/A'),
                "software_changes": locals().get('software_changes', 'N/A')
            },
            "physical_inspection": locals().get('visual_report', 'N/A'),
            "power_check": locals().get('power_report', "N/A"), 
            "diagnosis": locals().get('diag_report', {}),
            "priority": priority,
            "notes": notes
        }

        if priority == "קריטי (DOA)" or is_wrong_item:
            st.error(f"🚨 הקריאה נוצרה בעדיפות: {priority}")
        elif is_critical_damage:
            st.warning("🛠️ הקריאה נוצרה: נדרש תיקון חומרה")
        else:
            st.success("✅ הקריאה נוצרה בהצלחה")

        st.json(final_ticket)

if __name__ == "__main__":
    main()