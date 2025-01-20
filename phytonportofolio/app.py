import streamlit as st
from PIL import Image
import os

def get_image_path(image_name):
    """Helper function to construct correct image path"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(base_dir, 'img')
    os.makedirs(images_dir, exist_ok=True)
    return os.path.join(images_dir, image_name)

def show_portfolio_section():
    st.markdown("### 💼 My Projects")
    
    projects = [
        {
            "title": "Project 1 📊", 
            "description": "menganalisis sebuah data.", 
            "image_name": "analisisdata.PNG", 
            "link": "https://example.com/project1",
            "icon": "📈"
        },
        {
            "title": "Project 2 🌐", 
            "description": "membuat sebuah web crud dinamis.", 
            "image_name": "webcrud.PNG", 
            "link": "https://example.com/project2",
            "icon": "⚡"
        },
    ]
    
    for project in projects:
        with st.container():
            cols = st.columns([1, 3])
            with cols[0]:
                image_path = get_image_path(project["image_name"])
                try:
                    image = Image.open(image_path)
                    st.image(image, width=150)
                except Exception as e:
                    st.warning(f"Image not found: {project['image_name']}")
                    st.info("Please ensure your images are in the 'img' folder next to this script")
            with cols[1]:
                st.subheader(f"{project['icon']} {project['title']}")
                st.write(project["description"])
                st.markdown(f"[🔗 View Project]({project['link']})")

def show_contact_section():
    st.markdown("### 📬 Contact Me")
    st.write("Feel free to reach out through any of the following channels:")
    contact_info = """
    - 📧 Email: [your_email@example.com](mailto:your_email@example.com)
    - 💼 LinkedIn: [Your LinkedIn](https://linkedin.com)
    - 💻 GitHub: [Your GitHub](https://github.com)
    """
    st.markdown(contact_info)

def main():
    # Set page configuration
    st.set_page_config(
        page_title="My Portfolio ✨",
        page_icon="👨‍💻",
        layout="wide"
    )
    
    # Sidebar navigation
    st.sidebar.title("🧭 Navigation")
    pages = {
        "🏠 Home": "Home",
        "👋 About Me": "About Me",
        "💼 Portfolio": "Portfolio",
        "📬 Contact": "Contact"
    }
    selection = st.sidebar.radio("Go to:", list(pages.keys()))
    selection = pages[selection]  # Convert back to original page name
    
    # Header with decorative elements
    st.title("✨ Welcome to My Portfolio ✨")
    st.markdown("🚀 Your one-stop destination to explore my work, projects, and more!")
    
    # Dynamic page loading with enhanced headers
    if selection == "Home":
        st.header("🏠 Home")
        st.write("This is the homepage of my portfolio. Explore more using the navigation menu!")
        st.markdown("### 🌟 Quick Links")
        st.markdown("- 📁 Check out my latest projects\n- 📝 Read my blog\n- 🤝 Connect with me")
        
    elif selection == "About Me":
        st.header("👋 About Me")
        st.write("Hi! I'm ViaPutri, a passionate developer with expertise in machine learning, and web development. ✨")
        st.write("With over II years of experience, I have delivered solutions for clients worldwide. Let me help you bring your ideas to life! 🚀")
        
        # Add skills section with icons
        st.markdown("### 🛠️ Skills")
        st.markdown("""
        - 💻 Programming: Python, JavaScript, Java
        - 🤖 Machine Learning & AI
        - 🌐 Web Development
        - 📊 Data Analysis
        """)
        
    elif selection == "Portfolio":
        show_portfolio_section()
        
    elif selection == "Contact":
        show_contact_section()

if __name__ == "__main__":
    main()
