"""
Universal Classical Philological Web Engine.
Fully automated public engine with background engine orchestration.
"""

import streamlit as st
from ai_pipeline import PhilologicalPipelineOrchestrator

st.set_page_config(
    page_title="Universal Classical Philological Engine",
    page_icon="📜",
    layout="wide"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap');
    
    .main-title {
        font-family: 'Amiri', serif;
        font-size: 2.6rem;
        text-align: center;
        color: #D4AF37;
        margin-bottom: 5px;
    }
    .sub-title {
        text-align: center;
        color: #A0A0A0;
        font-size: 1rem;
        letter-spacing: 1px;
        margin-bottom: 25px;
    }
    .token-card {
        background-color: #1A1A1A;
        border: 1px solid #333333;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
    }
    .arabic-word {
        font-family: 'Amiri', serif;
        color: #D4AF37;
        font-size: 1.8rem;
        direction: rtl;
        text-align: right;
        margin: 0;
    }
    .arabic-syntax {
        font-family: 'Amiri', serif;
        font-size: 1.2rem;
        direction: rtl;
        text-align: right;
        color: #E0E0E0;
    }
    .meta-tag {
        color: #888888;
        font-size: 0.85rem;
        font-weight: bold;
        text-transform: uppercase;
    }
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🏛️ System Status")
st.sidebar.success("Engine Status: Active & Authenticated")
st.sidebar.markdown("""
---
**Mode:** Universal Philological Parser  
**Epistemological Grounding:** Basra & Kufa Schools  
**Metric Framework:** Al-Khalil ibn Ahmad (16 Meters)  
**Backend:** Autonomous Neural Philologist Agent
""")

st.markdown("<h1 class='main-title'>مُحَرِّكُ اللِّسَانِيَّاتِ وَالفِلُولُوجِيَا التُّرَاثِيَّة</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Universal Classical Arabic Semantic & Philological Reasoning Engine</p>", unsafe_allow_html=True)
st.divider()

default_sample = "الخَيلُ وَاللَيلُ وَالبَيداءُ تَعرِفُني وَالسَيفُ وَالرُمحُ وَالقِرطاسُ وَالقَلَمُ"
user_verse = st.text_area(
    "Enter ANY Classical Arabic Verse for Philological Dissection:", 
    value=default_sample,
    height=90
)

if st.button("Execute Universal Structural Breakdown"):
    with st.spinner("Executing dynamic metrics mapping and grammatical decomposition..."):
        try:
            result = PhilologicalPipelineOrchestrator.process_any_verse(user_verse)
            
            col_prosody, col_syntax = st.columns([1, 2])
            
            with col_prosody:
                st.subheader("1. Prosodic Engine (عِلْمُ العَرُوض)")
                st.success(f"**Meter:** {result.bahr_name_ar} ({result.bahr_name_en})")
                
                st.markdown("**Cadence Formula (التفاعيل):**")
                st.code(result.cadence_ar)
                
                st.markdown("**Binary Prosody (التقطيع العروضي):**")
                st.code(result.binary_notation)
                
                st.subheader("2. Context & Epistemology")
                st.info(result.thematic_depth)
                
            with col_syntax:
                st.subheader("3. Morpho-Syntactic Anatomy (التشريح الصرفي والإعراب)")
                for token in result.tokens:
                    st.markdown(f"""
                    <div class="token-card">
                        <div class="arabic-word">{token.word}</div>
                        <p><span class="meta-tag">Trilateral/Quadrilateral Root:</span> <strong>{token.root}</strong></p>
                        <div class="arabic-syntax">{token.morphology}</div>
                        <hr style="border: 0.5px solid #282828; margin: 8px 0;" />
                        <p style="color: #A5D6A7; margin-bottom: 0;"><span class="meta-tag">Syntactic Role:</span> {token.syntax_en}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
        except Exception as e:
            st.error(f"Execution Error: {str(e)}")