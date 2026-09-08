import streamlit as st
import streamlit.components.v1 as components
import os

# Sæt sidens opsætning
st.set_page_config(page_title="Fødselsdags-Mysteriet 🎁", page_icon="🔦", layout="centered")

st.title("🎁 Tillykke med fødselsdagen!")
st.write("Løs de 4 mystiske gåder for at låse op for din fødselsdagsgave. Held og lykke!")

# Hold styr på appens tilstand
if "trin" not in st.session_state:
    st.session_state.trin = 1

# Funktion til sikker afspilning af lokal MP3
def afspil_lydfil(filnavn):
    if os.path.exists(filnavn):
        with open(filnavn, "rb") as f:
            audio_bytes = f.read()
        st.audio(audio_bytes, format="audio/mp3")
    else:
        st.warning(f"⚠️ Kunne ikke finde lydfilen '{filnavn}' i mappen. Husk at placere den ved siden af app.py!")

# ------------------------------------------------------------------------------
# GÅDE 1: Musikalsk spor (The Weeknd via anonym lokal afspiller)
# ------------------------------------------------------------------------------
if st.session_state.trin == 1:
    st.subheader("Gåde 1: Et lysende hit")
    st.write("Afspil lyden nedenfor. Hvad er titlen på det track, du hører?")
    
    afspil_lydfil("1.mp3")
    
    svar3 = st.text_input("Hvad hedder sangen?", key="svar3").strip().lower()
    
    if st.button("Tjek svar", key="knap3"):
        if "blinding lights" in svar3 or "blinding" in svar3:
            st.success("Ja! 'Blinding Lights' af The Weeknd!")
            st.session_state.trin = 4
            st.rerun()
        else:
            st.error("Det var ikke det rigtige nummer.")


# ------------------------------------------------------------------------------
# GÅDE 2: Det bibelske citat
# ------------------------------------------------------------------------------
elif st.session_state.trin == 2:
    st.subheader("Gåde 2: De første ord")
    st.write("*Hvad sagde Gud ifølge Første Mosebog kapitel 1, vers 3?*")
    
    svar2 = st.text_input("Skriv dit svar her:", key="svar2").strip().lower()
    renset_svar = svar2.replace(".", "").replace(",", "")
    
    if st.button("Tjek svar", key="knap2"):
        if renset_svar == "der skal være lys":
            st.success("Præcis! Og der blev lys!")
            st.session_state.trin = 3
            st.rerun()
        else:
            st.error("Ikke helt rigtigt. Der skal være...)")
            
# ------------------------------------------------------------------------------
# GÅDE 3: Den Visuelle Dynamo-Udfordring (Fuld opdateret sekvens)
# ------------------------------------------------------------------------------
elif st.session_state.trin == 3:
    st.subheader("Gåde 3: Det evige strømproblem")
    st.write("Lad os se, om du kan få gang i cyklen...")
    
    # Skjult Python-knap, som JavaScript "klikker på" i baggrunden, når hjulet rammer 100%
    if st.button("Skjult_Knap_Naviger", key="skjult_knap", help="Ignorer denne"):
        st.session_state.trin = 2
        st.balloons()
        st.rerun()

    visuelt_spil_html = """
    <div style="font-family: sans-serif; background: #f0f2f6; padding: 20px; border-radius: 10px; text-align: center;">

        <!-- TRIN 1: STOP ALARMEN -->
        <div id="trin1_alarm">
            <p><strong>Trin 1: Åh nej! Alarmen ringer!</strong></p>
            <div style="font-size: 60px; margin: 10px 0; animation: shake 0.5s infinite;">⏰</div>
            <button onclick="stopAlarm()" style="padding: 12px; background: #ff4b4b; color: white; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; width: 100%;">
                ⏹️ STOP ALARMEN!
            </button>
        </div>

        <!-- TRIN 2: TÆND LYGTERNE -->
        <div id="trin2_lygte" style="display: none;">
            <p style="font-size: 20px; font-weight: bold; color: #ff4b4b;">⏰ 19:10</p>
            <p><strong>Åh nej, jeg kommer for sent til træning!</strong></p>
            <p>Det er mørkt udenfor, så du skal have lys på cyklen. Prøv at tænde lygten:</p>
            <div style="font-size: 60px; margin: 10px 0;">🔦</div>
            <button onclick="taendLygte()" style="padding: 12px; background: #007bff; color: white; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; width: 100%;">
                💡 Klik for at tænde cykellygten
            </button>
        </div>

         <!-- TRIN 3: SMID BATTERIERNE UD (MED MOBIL-TOUCH LOGIK) -->
        <div id="trin3_batteri" style="display: none; height: 180px; position: relative;">
            <p><strong>Ingen lys... Cykellygterne er helt døde!</strong></p>
            <p>Batterierne er løbet tør. Ud med det skrammel!</p>
            <div style="display: flex; justify-content: space-around; align-items: center; margin: 20px 0; position: relative; height: 90px;">
                <!-- Batteri med touch-action none for at forhindre at skærmen scroller når man trækker -->
                <div id="battery" draggable="true" ondragstart="drag(event)" onclick="smidBatteriUd()" 
                     style="font-size: 50px; cursor: grab; touch-action: none; user-select: none; position: absolute; left: 20%; z-index: 10;">🔋</div>
                <!-- Skraldespand -->
                <div id="trash" ondrop="drop(event)" ondragover="allowDrop(event)" 
                     style="font-size: 60px; padding: 10px; border: 3px dashed #ff4b4b; border-radius: 10px; width: 80px; height: 80px; display:flex; justify-content:center; align-items:center; position: absolute; right: 20%;">🗑️</div>
            </div>
            <p style="font-size: 12px; color: #555; margin-top: 10px;"></p>
        </div>
        
        <!-- TRIN 4: LED EFTER OPLADEREN -->
        <div id="trin4_oplader" style="display: none;">
            <p><strong>Trin 4: Find USB-kablet i rodet for at lade cykellygten op!</strong></p>
            <p style="font-size: 14px; color: #555;">Hvor ligger det? Klik rundt for at lede:</p>
            <div style="display: flex; justify-content: space-around; margin: 20px 0;">
                <button onclick="alert('❌ Nej... Kun gammelt slikpapir og en masse vigtige papirer.')" style="padding: 10px; background: #fff; border: 1px solid #ccc; border-radius: 5px; cursor: pointer;">I skuffen 🗄️</button>
                <button onclick="alert('❌ Forbi! Her ligger bare en enlig sok og noget støv.')" style="padding: 10px; background: #fff; border: 1px solid #ccc; border-radius: 5px; cursor: pointer;">Under sengen 🛏️</button>
                <button onclick="alert('❌ Heller ikke! Kun nøgler og en masse krøllede kvitteringer.')" style="padding: 10px; background: #fff; border: 1px solid #ccc; border-radius: 5px; cursor: pointer;">I jakkelommen 🧥</button>
            </div>
            <button onclick="visTrin5()" style="margin-top: 10px; padding: 12px; background: #ff4b4b; color: white; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; width: 100%;">
                ❌ Giv op, opladeren er væk for evigt!
            </button>
        </div>

        <!-- TRIN 5: CYKELHJUL / DYNAMO -->
        <div id="trin5_dynamo" style="display: none;">
            <p><strong>Trin 5: Du skal bruge en anden energikilde... Generer din egen strøm!</strong></p>
            <p>Drej cykelhjulet rundt for at tænde dynamoen!</p>
            <div id="wheel" onclick="rotateWheel()" style="font-size: 80px; display: inline-block; transition: transform 0.1s ease; cursor: pointer; user-select: none; margin: 20px;">🚲</div>
            <p id="statusTekst" style="font-weight: bold; color: #ff9800;">Strøm genereret: 0%</p>
            <p style="font-size: 12px; color: #555;">(Klik/tap hurtigt direkte på cyklen 10 gange for at spinde hjulet rundt!)</p>
            
            <!-- Den grønne knap popper op her -->
            <button id="streamlitKnap" onclick="gaaVidereTilPython()" style="display: none; margin-top: 20px; padding: 14px; background: #28a745; color: white; border: none; border-radius: 5px; font-weight: bold; font-size: 16px; cursor: pointer; width: 100%; animation: shake 0.8s infinite;">
                🔦 TÆND DYNAMOLYGTEN AND GÅ VIDERE!
            </button>
        </div>
    </div>

    <style>
        @keyframes shake {
            0% { transform: translate(1px, 1px) rotate(0deg); }
            10% { transform: translate(-1px, -2px) rotate(-1deg); }
            20% { transform: translate(-3px, 0px) rotate(1deg); }
            30% { transform: translate(0px, 2px) rotate(0deg); }
            40% { transform: translate(1px, -1px) rotate(1deg); }
            50% { transform: translate(-1px, 2px) rotate(-1deg); }
            60% { transform: translate(-3px, 1px) rotate(0deg); }
            70% { transform: translate(2px, 1px) rotate(-1deg); }
            80% { transform: translate(-1px, -1px) rotate(1deg); }
            90% { transform: translate(2px, 2px) rotate(0deg); }
            100% { transform: translate(1px, -2px) rotate(-1deg); }
        }
    </style>

    <script>
        function stopAlarm() {
            document.getElementById("trin1_alarm").style.display = "none";
            document.getElementById("trin2_lygte").style.display = "block";
        }

        function taendLygte() {
            document.getElementById("trin2_lygte").style.display = "none";
            document.getElementById("trin3_batteri").style.display = "block";
        }

        // ÆGTE DRAG AND DROP FUNKTIONER RETUR
        function allowDrop(ev) { ev.preventDefault(); }
        function drag(ev) { ev.dataTransfer.setData("text", ev.target.id); }
        function drop(ev) {
            ev.preventDefault();
            smidBatteriUd();
        }

        function smidBatteriUd() {
            document.getElementById("trin3_batteri").style.display = "none";
            document.getElementById("trin4_oplader").style.display = "block";
        }

        function visTrin5() {
            document.getElementById("trin4_oplader").style.display = "none";
            document.getElementById("trin5_dynamo").style.display = "block";
        }

        var clicks = 0;
        var degrees = 0;
        function rotateWheel() {
            if (clicks >= 10) return;
            
            clicks++;
            degrees += 36;
            document.getElementById("wheel").style.transform = "rotate(" + degrees + "deg)";
            
            var procent = clicks * 10;
            document.getElementById("statusTekst").innerText = "Strøm genereret: " + procent + "%";
            
            if (clicks >= 10) {
                document.getElementById("statusTekst").innerText = "🔋 100% STRØM! LYGTEN LYSER FOR EVIGT!";
                document.getElementById("statusTekst").style.color = "#28a745";
                document.getElementById("streamlitKnap").style.display = "block";
            }
        }

        // RETTET: Finder Streamlits egen usynlige knap i Python og klikker mekanisk på den!
        function gaaVidereTilPython() {
            var buttons = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < buttons.length; i++) {
                if (buttons[i].textContent.includes('Skjult_Knap_Naviger')) {
                    buttons[i].click();
                    break;
                }
            }
        }
    </script>
    """
    
    components.html(visuelt_spil_html, height=400)
            

# ------------------------------------------------------------------------------
# GÅDE 4: Kontrasten (Rocks vs. Rav via lokale lydafspillere)
# ------------------------------------------------------------------------------
elif st.session_state.trin == 4:
    st.subheader("Gåde 4: Den endelige opgradering")
    st.write("Du skal nu løse det sidste mysterium for at undgå mere af dét her:")
    afspil_lydfil("2.mp3")
    
    st.write("**I stedet finde meget mere:**")
    afspil_lydfil("3.mp3")
    
    st.write("---")
    st.write("*Spørgsmål: Hvad har alle disse gåder til fælles?*")
    
    svar4 = st.text_input("Hvad er gaven?", key="svar4").strip().lower()
    
    if st.button("LÅS GAVEN OP! 🔓"):
        if any(ordet in svar4 for ordet in ["lygte", "lommelygte", "lys", "cykellygte", "cykellygter"]):
            st.session_state.trin = 5
            st.rerun()
        else:
            st.error("Næsten!")

# ------------------------------------------------------------------------------
# AFSLØRINGEN
# ------------------------------------------------------------------------------
elif st.session_state.trin == 5:
    st.balloons()
    st.snow()
    st.subheader("🎉 TILLYKKE! DU HAR LØST MYSTERIET! 🎉")
    st.write("Du har gættet det helt rigtigt! Værsgo' at åbne gaven")
