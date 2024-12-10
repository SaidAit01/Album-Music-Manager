import { Navbar, Nav } from "react-bootstrap";

function AppNavbar() {
  return (
    <Navbar
      expand="lg"
      sticky="top" // Makes the navbar stick to the top
      style={{
        background: "linear-gradient(90deg, #4b6cb7, #182848)", // Matching gradient
        color: "#fff",
        boxShadow: "0 2px 5px rgba(0, 0, 0, 0.3)", // Subtle shadow for depth
        zIndex: 10, // Ensures it stays above other elements
        transition: "background 0.5s ease", // Smooth transition for scroll effects
      }}
      id="app-navbar"
    >
      <Navbar.Brand
        href="/"
        style={{
          fontFamily: "'Cinzel', serif",
          fontSize: "1.8rem",
          color: "#fff",
          display: "flex",
          alignItems: "center",
          gap: "10px",
        }}
      >
        <img
          src="https://img.icons8.com/ios-filled/50/ffffff/musical-notes.png" // Example icon
          alt="Logo"
          style={{ height: "30px", width: "30px" }}
        />
        MyMusicMaestro
      </Navbar.Brand>
      <Nav className="ms-3 d-flex align-items-center">
        <Nav.Link
          href="/"
          style={{
            color: "#fff",
            fontFamily: "'Roboto', sans-serif",
            fontSize: "1.1rem",
            transition: "color 0.3s ease",
          }}
          onMouseEnter={(e) => (e.target.style.color = "#a3cef1")} // Hover effect
          onMouseLeave={(e) => (e.target.style.color = "#fff")}
        >
          Home
        </Nav.Link>
      </Nav>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="ms-auto">
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
}

export default AppNavbar;
