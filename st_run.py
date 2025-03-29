import streamlit as st

# Custom CSS for styling, dark mode, and smooth transitions
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    
    body {
        font-family: 'Roboto', sans-serif;
        background-color: #f0f2f6;
        color: #333;
        transition: all 0.3s ease;
    }
    .dark-mode {
        background-color: #2b2b2b;
        color: #f0f2f6;
    }
    .hero {
        text-align: center;
        padding: 60px 0;
        animation: fadeIn 1s ease-in;
    }
    .hero h1 {
        font-size: 2.5em;
        margin-bottom: 20px;
        color: #6c63ff;
    }
    .hero img {
        max-width: 80%;
        height: auto;
        border-radius: 10px;
    }
    .cta-button {
        background-color: #6c63ff;
        color: white;
        padding: 12px 24px;
        border-radius: 5px;
        text-decoration: none;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }
    .cta-button:hover {
        background-color: #87ceeb;
    }
    .section {
        padding: 40px 20px;
    }
    .section h2 {
        color: #6c63ff;
        margin-bottom: 20px;
    }
    .feature {
        text-align: center;
        margin-bottom: 30px;
    }
    .feature img {
        max-width: 80px;
        margin-bottom: 15px;
    }
    .form-input {
        width: 100%;
        padding: 10px;
        margin-bottom: 20px;
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    .form-button {
        background-color: #6c63ff;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .form-button:hover {
        background-color: #87ceeb;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @media (max-width: 768px) {
        .hero h1 {
            font-size: 1.8em;
        }
        .section {
            padding: 20px 10px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Dark mode toggle in sidebar
dark_mode = st.sidebar.checkbox("Dark Mode", value=False)
if dark_mode:
    st.markdown('<style>body { background-color: #2b2b2b; color: #f0f2f6; }</style>', unsafe_allow_html=True)

# Navigation menu
page = st.sidebar.selectbox("Navigate", ["Home", "How It Works", "Features", "Science & Research", "About Us", "Early Access & Contact"])

# Home Page
if page == "Home":
    st.markdown("""
    <div class="hero">
        <h1>Better Sleep, Smarter Technology</h1>
        <img src="https://via.placeholder.com/600x400.png?text=Smart+Sleep+Mask" alt="Smart Sleep Mask">
        <br><br>
        <a href="#" class="cta-button">Join the Waitlist</a>
    </div>
    """, unsafe_allow_html=True)

# How It Works Page
elif page == "How It Works":
    st.markdown('<div class="section"><h2>How It Works</h2></div>', unsafe_allow_html=True)
    st.write("""
    Transcutaneous vagus nerve stimulation (tVNS) is a non-invasive technique that uses gentle electrical impulses delivered via a TENS device to stimulate the vagus nerve. This nerve plays a crucial role in regulating relaxation and sleep. By enhancing parasympathetic activity, our smart sleep mask helps you fall asleep faster and enjoy deeper, more restorative rest.
    """)
    st.markdown("""
    <!-- Placeholder for animations/illustrations -->
    <div style="text-align: center;">
        <img src="https://via.placeholder.com/300x200.png?text=tVNS+Illustration" alt="tVNS Illustration">
    </div>
    """, unsafe_allow_html=True)

# Features Page
elif page == "Features":
    st.markdown('<div class="section"><h2>Features</h2></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="feature">
            <img src="https://via.placeholder.com/80.png?text=Deep+Sleep" alt="Deep Sleep">
            <p><strong>Enhances Deep Sleep</strong><br>Promotes deeper, more restful sleep cycles.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="feature">
            <img src="https://via.placeholder.com/80.png?text=Anxiety" alt="Reduce Anxiety">
            <p><strong>Reduces Anxiety</strong><br>Calms the mind for a peaceful night.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="feature">
            <img src="https://via.placeholder.com/80.png?text=Comfort" alt="Comfortable Design">
            <p><strong>Non-Invasive & Comfortable</strong><br>Designed for all-night wear.</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("""
    <div class="feature" style="text-align: center;">
        <img src="https://via.placeholder.com/80.png?text=App" alt="Mobile App">
        <p><strong>Mobile App Integration</strong><br>Control and monitor your sleep experience.</p>
    </div>
    """, unsafe_allow_html=True)

# Science & Research Page
elif page == "Science & Research":
    st.markdown('<div class="section"><h2>Science & Research</h2></div>', unsafe_allow_html=True)
    st.write("""
    The neuroscience behind tVNS shows that stimulating the vagus nerve increases parasympathetic activity, which regulates heart rate, stress levels, and sleep quality. Research indicates improved deep sleep and reduced anxiety with consistent use.
    """)
    st.markdown("""
    <p>Learn more:</p>
    <ul>
        <li><a href="https://www.ncbi.nlm.nih.gov" target="_blank">Study on tVNS and Sleep</a></li>
        <li><a href="https://www.sciencedirect.com" target="_blank">Vagus Nerve Stimulation Research</a></li>
    </ul>
    """, unsafe_allow_html=True)

# About Us Page
elif page == "About Us":
    st.markdown('<div class="section"><h2>About Us</h2></div>', unsafe_allow_html=True)
    st.write("""
    **Mission Statement:** At DREAMS, we're revolutionizing sleep with cutting-edge neurotechnology. Our smart sleep mask harnesses tVNS to help you achieve better sleep and improved well-being.
    """)
    st.write("""
    **Founder:** Jane Doe, a neuroscientist with over 10 years of experience in sleep research, founded DREAMS to bring innovative solutions to those struggling with sleep and stress.
    """)

# Early Access & Contact Page
elif page == "Early Access & Contact":
    st.markdown('<div class="section"><h2>Early Access & Contact</h2></div>', unsafe_allow_html=True)
    st.write("Be the first to experience the future of sleep. Sign up for early access or contact us!")
    with st.form("waitlist_form"):
        email = st.text_input("Email Address", key="email")
        submit = st.form_submit_button("Join Waitlist", help="Submit your email")
        if submit:
            st.success("Thank you for joining the waitlist!")
    st.markdown("""
    <p><strong>Contact:</strong> <a href="mailto:contact@dreams.com">contact@dreams.com</a></p>
    <p><strong>Follow Us:</strong> 
        <a href="#">Twitter</a> | 
        <a href="#">Instagram</a> | 
        <a href="#">LinkedIn</a>
    </p>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; padding: 20px; font-size: 0.9em;">
    &copy; 2023 DREAMS | <a href="#">Privacy Policy</a> | <a href="#">Terms of Service</a>
</div>
""", unsafe_allow_html=True)