import streamlit as st

st.set_page_config(layout="wide", page_title="HAVEN - Search Campaigns")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');

    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #f0f2f5;
        color: #333;
    }

    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 20px;
        padding-right: 20px;
    }

    .stApp > header {
        display: none;
    }

    .main-layout-container {
        display: flex;
        max-width: 1200px;
        margin: 20px auto;
        gap: 20px;
        padding: 0px 0px;
    }

    .sidebar-container {
        width: 220px;
        background-color: #ffffff;
        padding: 20px 0;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.08);
        flex-shrink: 0;
        height: fit-content;
    }

    .sidebar-menu ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    .sidebar-menu li {
        margin-bottom: 5px;
    }
    .sidebar-menu a {
        text-decoration: none;
        color: #333;
        display: flex;
        align-items: center;
        padding: 12px 20px;
        transition: background-color 0.2s ease, color 0.2s ease;
        font-size: 15px;
        font-weight: 500;
    }
    .sidebar-menu a:not(.active) {
        font-weight: bold;
    }
    .sidebar-menu a i {
        margin-right: 10px;
        color: #555;
    }
    .sidebar-menu a:hover {
        background-color: #e6e9ed;
        color: #1a1a1a;
    }
    .sidebar-menu a.active {
        background-color: #e0e6f0;
        color: #1a1a1a;
        font-weight: bold;
        position: relative;
    }
    .sidebar-menu a.active::before {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 4px;
        background-color: #6a0dad;
        border-top-right-radius: 2px;
        border-bottom-right-radius: 2px;
    }
    .sidebar-user-profile {
        margin-top: 30px;
        text-align: center;
        padding: 20px;
        border-top: 1px solid #eee;
        color: #666;
        font-size: 13px;
    }
    .sidebar-user-profile p {
        margin: 5px 0;
    }
    .sidebar-user-profile p.user-name {
        font-weight: bold;
        color: #333;
    }

    .content-area-container {
        flex-grow: 1;
        padding-right: 0px;
        padding-left: 0px;
    }

    .top-content-area {
        background-color: #f8f8f8;
        padding: 30px 40px;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        margin-bottom: 30px;
        text-align: center;
    }

    .main-logo-text {
        font-family: 'Playfair Display', serif;
        font-size: 3.5em;
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
        line-height: 1;
    }
    .main-logo-subtitle {
        font-size: 1.2em;
        color: #666;
        margin-bottom: 30px;
    }

    .stTextInput>div>div>input {
        padding: 14px 20px 14px 50px !important;
        border: 1px solid #ddd !important;
        border-radius: 30px !important;
        font-size: 1.05em !important;
        outline: none !important;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.05) !important;
        background-color: #fff;
    }
    .stTextInput label {
        display: none;
    }
    div[data-testid="stTextInput"] {
        position: relative;
        width: 70%;
        max-width: 600px;
        margin: 0 auto;
    }
    div[data-testid="stTextInput"]::before {
        content: "\\f002";
        font-family: "Font Awesome 5 Free";
        font-weight: 900;
        position: absolute;
        left: 20px;
        top: 50%;
        transform: translateY(-50%);
        color: #999;
        font-size: 1.2em;
        z-index: 1;
    }

    .campaigns-section {
        background-color: #f8f8f8;
        padding: 30px;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }
    .campaigns-section h2 {
        font-size: 1.8em;
        color: #333;
        margin-bottom: 10px;
    }
    .campaigns-section .section-subtitle {
        font-size: 1em;
        color: #666;
        margin-bottom: 25px;
        border-bottom: 2px solid #eee;
        padding-bottom: 10px;
    }
    .campaign-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 25px;
    }
    .campaign-card {
        background-color: #fcfcfc;
        border: 1px solid #e5e5e5;
        border-radius: 10px;
        overflow: hidden;
        padding: 20px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }
    .campaign-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    .campaign-image-placeholder {
        width: 100%;
        height: 180px;
        background-color: #e0e0e0;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: flex-start;
        padding: 10px;
        color: #666;
        font-size: 1.3em;
        font-weight: bold;
        margin-bottom: 15px;
        border-radius: 5px;
        position: relative;
        box-sizing: border-box;
    }
    .campaign-image-placeholder .badge {
        position: absolute;
        top: 10px;
        right: 10px;
        background-color: rgba(0, 0, 0, 0.7);
        color: #fff;
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 0.8em;
        font-weight: normal;
        display: flex;
        align-items: center;
        z-index: 2;
    }
    .campaign-image-placeholder .badge i {
        margin-right: 5px;
    }
    .campaign-image-placeholder .image-size {
        position: absolute;
        bottom: 10px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 0.9em;
        color: rgba(255, 255, 255, 0.8);
        background-color: rgba(0, 0, 0, 0.5);
        padding: 3px 8px;
        border-radius: 5px;
        z-index: 2;
    }
    .campaign-card h3 {
        font-size: 1.3em;
        color: #333;
        margin: 0 0 8px 0;
        text-align: left;
    }
    .campaign-card .campaign-description {
        font-size: 0.95em;
        color: #555;
        line-height: 1.5;
        margin-bottom: 15px;
        text-align: left;
        flex-grow: 1;
    }
    .campaign-card .campaign-author {
        font-size: 0.85em;
        color: #888;
        margin: 0;
        text-align: left;
    }
    .campaign-progress-container {
        width: 100%;
        margin-top: 15px;
        margin-bottom: 10px;
    }
    .campaign-progress-bar {
        width: 100%;
        background-color: #e0e0e0;
        border-radius: 5px;
        height: 6px;
        overflow: hidden;
    }
    .campaign-progress-fill {
        height: 100%;
        background-color: #6a0dad;
        border-radius: 5px;
    }
    .campaign-stats {
        display: flex;
        justify-content: space-between;
        font-size: 0.9em;
        color: #555;
        margin-top: 8px;
    }
    .campaign-stats .amount-funded {
        font-weight: bold;
        color: #333;
    }

    .category-buttons {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-bottom: 25px;
        justify-content: center;
    }
    .category-button {
        background-color: #fff;
        border: 1px solid #ddd;
        border-radius: 20px;
        padding: 8px 15px;
        font-size: 0.9em;
        color: #555;
        cursor: pointer;
        transition: background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease;
    }
    .category-button:hover {
        background-color: #e6e9ed;
        border-color: #c0c4c8;
    }
    .category-button.active {
        background-color: #6a0dad;
        color: #fff;
        border-color: #6a0dad;
    }

    @media (max-width: 768px) {
        .main-layout-container {
            flex-direction: column;
            padding: 10px;
            margin-top: 20px;
        }
        .sidebar-container {
            width: 100%;
            padding: 10px 0;
            margin-bottom: 20px;
        }
        .sidebar-menu ul {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
        }
        .sidebar-menu li {
            margin: 5px;
        }
        .sidebar-menu a {
            padding: 8px 12px;
            font-size: 14px;
        }
        .sidebar-user-profile {
            display: none;
        }
        .content-area-container {
            padding-right: 0;
        }
        .top-content-area {
            padding: 20px;
        }
        .main-logo-text {
            font-size: 2.5em;
        }
        .main-logo-subtitle {
            font-size: 1em;
        }
        div[data-testid="stTextInput"] {
            width: 90%;
        }
        .campaigns-section {
            padding: 20px;
        }
        .campaigns-section h2 {
            font-size: 1.6em;
        }
        .campaigns-section .section-subtitle {
            font-size: 0.9em;
        }
        .campaign-grid {
            grid-template-columns: 1fr;
        }
        .category-buttons {
            justify-content: flex-start;
        }
    }
</style>
""", unsafe_allow_html=True)

all_campaign_data = [
    {"name": "EcoDrone: AI for Reforestation", "description": "Help us build AI-powered drones that plant trees and monitor forest health. Revolutionizing conservation efforts.", "author": "By GreenFuture Now", "funded": 25000, "goal": 50000, "days_left": 15, "category": "Technology"},
    {"name": "Echoes of Tomorrow - Indie Sci-Fi Film", "description": "Support our ambitious independent science fiction film exploring themes of memory and identity in a dystopian future.", "author": "By Nova Pictures", "funded": 75000, "goal": 100000, "days_left": 30, "category": "Arts & Culture"},
    {"name": "The Art Hive: Community Art Space", "description": "We are creating a vibrant, accessible art studio and gallery space for everyone in our community.", "author": "By Local Artists Collective", "funded": 10000, "goal": 20000, "days_left": 7, "category": "Community"},
    {"name": "Melody Weaver - Debut Album", "description": "Help me record and release my debut folk-pop album, filled with heartfelt stories and enchanting melodies.", "author": "By Seraphina Moon", "funded": 3000, "goal": 18000, "days_left": 60, "category": "Music"},
    {"name": "ReThread: Sustainable Fashion Line", "description": "Launching a new line of clothing made entirely from recycled materials and ethical practices.", "author": "By EarthWear Designs", "funded": 5000, "goal": 15000, "days_left": 20, "category": "Fashion"},
    {"name": "Future Farms: Hydroponic Innovation", "description": "Developing modular hydroponic systems for sustainable urban farming, reducing water usage by 90%.", "author": "By AgroTech Solutions", "funded": 40000, "goal": 60000, "days_left": 25, "category": "Technology"},
    {"name": "Historic Landmark Restoration", "description": "Raise funds to restore the dilapidated town hall, preserving its historical integrity for future generations.", "author": "By Heritage Keepers", "funded": 15000, "goal": 30000, "days_left": 10, "category": "Community"},
    {"name": "Interactive STEM Workshops for Kids", "description": "Providing hands-on STEM education to underprivileged children through engaging workshops and resources.", "author": "By Bright Minds Initiative", "funded": 8000, "goal": 12000, "days_left": 18, "category": "Education"},
]

if 'active_page' not in st.session_state:
    st.session_state.active_page = 'Explore' # Keeping 'Explore' active for now

if 'selected_category' not in st.session_state:
    st.session_state.selected_category = 'All'

col1, col2 = st.columns([220, 1000])

with st.container():
    st.markdown('<div class="main-layout-container">', unsafe_allow_html=True)

    with col1:
        st.markdown('<div class="sidebar-container">', unsafe_allow_html=True)
        st.markdown(f"""
            <div class="sidebar-menu">
                <ul>
                    <li><a href="#" class="{'active' if st.session_state.active_page == 'Home' else ''}" onclick="window.parent.document.querySelector('[data-testid=\"stMarkdownContainer\"]').dispatchEvent(new CustomEvent('streamlit:update-session-state', {{ detail: {{ key: 'active_page', value: 'Home' }} }}))"><i class="fas fa-home"></i> Home</a></li>
                    <li><a href="#" class="{'active' if st.session_state.active_page == 'Explore' else ''}" onclick="window.parent.document.querySelector('[data-testid=\"stMarkdownContainer\"]').dispatchEvent(new CustomEvent('streamlit:update-session-state', {{ detail: {{ key: 'active_page', value: 'Explore' }} }}))"><i class="fas fa-compass"></i> Explore</a></li>
                    <li><a href="#" class="{'active' if st.session_state.active_page == 'Create Campaign' else ''}" onclick="window.parent.document.querySelector('[data-testid=\"stMarkdownContainer\"]').dispatchEvent(new CustomEvent('streamlit:update-session-state', {{ detail: {{ key: 'active_page', value: 'Create Campaign' }} }}))"><i class="fas fa-plus-circle"></i> Create Campaign</a></li>
                </ul>
            </div>
            <div class="sidebar-user-profile">
                <p class="user-name">User Name</p>
                <p>username@email.com</p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="content-area-container">', unsafe_allow_html=True)

        st.markdown("""
            <div class="top-content-area">
                <div class="main-logo-text">HAVEN</div>
                <p class="main-logo-subtitle">Search for campaigns that inspire you.</p>
        """, unsafe_allow_html=True)

        search_query = st.text_input("", placeholder="Enter keywords to search campaigns...", key="search_bar_main")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("""
            <div class="campaigns-section">
                <h2>Search Results</h2>
                <p class="section-subtitle">Filter results by category.</p>
        """, unsafe_allow_html=True)

        # Retaining the category buttons as provided in the previous request
        st.markdown(f"""
            <div class="category-buttons">
                <button class="category-button {'active' if st.session_state.selected_category == 'All' else ''}" onclick="window.parent.document.querySelector('[data-testid=\"stMarkdownContainer\"]').dispatchEvent(new CustomEvent('streamlit:update-session-state', {{ detail: {{ key: 'selected_category', value: 'All' }} }}))"> All </button>
                <button class="category-button {'active' if st.session_state.selected_category == 'Technology' else ''}" onclick="window.parent.document.querySelector('[data-testid=\"stMarkdownContainer\"]').dispatchEvent(new CustomEvent('streamlit:update-session-state', {{ detail: {{ key: 'selected_category', value: 'Technology' }} }}))"> Technology </button>
                <button class="category-button {'active' if st.session_state.selected_category == 'Arts & Culture' else ''}" onclick="window.parent.document.querySelector('[data-testid=\"stMarkdownContainer\"]').dispatchEvent(new CustomEvent('streamlit:update-session-state', {{ detail: {{ key: 'selected_category', value: 'Arts & Culture' }} }}))"> Arts & Culture </button>
                <button class="category-button {'active' if st.session_state.selected_category == 'Community' else ''}" onclick="window.parent.document.querySelector('[data-testid=\"stMarkdownContainer\"]').dispatchEvent(new CustomEvent('streamlit:update-session-state', {{ detail: {{ key: 'selected_category', value: 'Community' }} }}))"> Community </button>
                <button class="category-button {'active' if st.session_state.selected_category == 'Music' else ''}" onclick="window.parent.document.querySelector('[data-testid=\"stMarkdownContainer\"]').dispatchEvent(new CustomEvent('streamlit:update-session-state', {{ detail: {{ key: 'selected_category', value: 'Music' }} }}))"> Music </button>
                <button class="category-button {'active' if st.session_state.selected_category == 'Fashion' else ''}" onclick="window.parent.document.querySelector('[data-testid=\"stMarkdownContainer\"]').dispatchEvent(new CustomEvent('streamlit:update-session-state', {{ detail: {{ key: 'selected_category', value: 'Fashion' }} }}))"> Fashion </button>
                <button class="category-button {'active' if st.session_state.selected_category == 'Education' else ''}" onclick="window.parent.document.querySelector('[data-testid=\"stMarkdownContainer\"]').dispatchEvent(new CustomEvent('streamlit:update-session-state', {{ detail: {{ key: 'selected_category', value: 'Education' }} }}))"> Education </button>
            </div>
        """, unsafe_allow_html=True)

        filtered_campaigns = []
        for campaign in all_campaign_data:
            matches_category = (st.session_state.selected_category == "All" or campaign["category"] == st.session_state.selected_category)
            matches_search = (search_query.lower() in campaign["name"].lower() or search_query.lower() in campaign["description"].lower())
            if matches_category and matches_search:
                filtered_campaigns.append(campaign)

        if not filtered_campaigns:
            st.markdown("<p style='text-align: center; color: #888;'>No campaigns found matching your criteria. Try a different search or filter!</p>", unsafe_allow_html=True)
        else:
            st.markdown('<div class="campaign-grid">', unsafe_allow_html=True)
            for campaign in filtered_campaigns:
                progress_percentage = (campaign['funded'] / campaign['goal']) * 100 if campaign['goal'] > 0 else 0
                st.markdown(f"""
                    <div class="campaign-card">
                        <div class="campaign-image-placeholder">
                            <span class="badge trending"><i class="fas fa-chart-line"></i> Trending</span>
                            <span class="image-size">600 x 400</span>
                        </div>
                        <h3>{campaign['name']}</h3>
                        <p class="campaign-description">{campaign['description']}</p>
                        <p class="campaign-author">{campaign['author']}</p>
                        <div class="campaign-progress-container">
                            <div class="campaign-progress-bar">
                                <div class="campaign-progress-fill" style="width: {progress_percentage:.0f}%"></div>
                            </div>
                            <div class="campaign-stats">
                                <span class="amount-funded">₹{campaign['funded']:,} raised {progress_percentage:.0f}%</span>
                                <span>{campaign['days_left']} days left</span>
                            </div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
