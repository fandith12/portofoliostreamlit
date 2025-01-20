import streamlit as st
from PIL import Image

# Fungsi untuk menampilkan bagian portofolio
def show_portfolio_section():
    st.markdown("### My Projects")

    projects = [
        {"title": "Project 1", "description": "menganalisis sebuah data.", "image": "/img/analisisdata.png", "link": "https://example.com/project1"},
        {"title": "Project 2", "description": "membuat sebuah web crud dinamis.", "image": "/img/webcrud.png", "link": "https://example.com/project2"},
    ]

    for project in projects:
        with st.container():
            cols = st.columns([1, 3])
            with cols[0]:
                st.image(project["image"], width=150)
            with cols[1]:
                st.subheader(project["title"])
                st.write(project["description"])
                st.markdown(f"[View Project]({project['link']})")

# Fungsi untuk menampilkan kontak
def show_contact_section():
    st.markdown("### Contact Me")
    st.write("Feel free to reach out through any of the following channels:")

    st.markdown(
        """- Email: [your_email@example.com](mailto:your_email@example.com)
        - LinkedIn: [Your LinkedIn](https://linkedin.com)
        - GitHub: [Your GitHub](https://github.com)
        """
    )

# Halaman utama aplikasi
def main():
    # Sidebar navigation
    st.sidebar.title("Navigation")
    pages = ["Home", "About Me", "Portfolio", "Contact"]
    selection = st.sidebar.radio("Go to:", pages)

    # Header
    st.title("Welcome to My Portfolio")
    st.markdown("Your one-stop destination to explore my work, projects, and more.")

    # Dynamic page loading
    if selection == "Home":
        st.header("Home")
        st.write("This is the homepage of my portfolio. Explore more using the navigation menu!")
    elif selection == "About Me":
        st.header("About Me")
        st.write("Hi! I'm ViaPutri, a passionate developer with expertise in machine learning, and web development.")
        st.write("\n")
        st.write("With over II years of experience, I have delivered solutions for clients worldwide. Let me help you bring your ideas to life!")
    elif selection == "Portfolio":
        show_portfolio_section()
    elif selection == "Contact":
        show_contact_section()

# Jalankan aplikasi jika file dijalankan langsung
if __name__ == "__main__":
    main()
