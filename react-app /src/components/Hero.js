function Hero() {
  return (
    <div
      className="hero text-center text-light"
      style={{
        background: "linear-gradient(90deg, #4b6cb7, #182848)", // Gradient background
        padding: "60px 20px", // Adjusted padding for a smaller height
        position: "relative",
        height: "300px", // Reduced height
      }}
    >
      {/* Hero Content */}
      <div
        className="d-flex flex-column justify-content-center align-items-center h-100"
        style={{
          zIndex: 2,
        }}
      >
        <h1
          className="display-4 fw-bold"
          style={{
            fontFamily: "'Cinzel', serif",
            textShadow: "2px 2px 5px rgba(0, 0, 0, 0.7)",
          }}
        >
          Welcome to MyMusicMaestro
        </h1>
        <p
          className="lead"
          style={{
            fontFamily: "'Roboto', sans-serif",
            maxWidth: "600px",
            marginTop: "10px",
          }}
        >
          Your ultimate destination to explore, listen, and enjoy music like never before.
        </p>
      </div>
    </div>
  );
}

export default Hero;
