import React from "react";
import { Link } from "react-router-dom";
import { Card, Badge } from "react-bootstrap";

function AlbumCard({ album }) {
  // Add defensive checks for album and its properties
  if (!album) {
    return <div className="mb-4">No album data available</div>;
  }

  const {
    id = "",
    title = "Untitled Album",
    artist = "Unknown Artist",
    release_year = "Unknown Year",
    short_description = "",
    cover_image = "default_image_url.jpg"
  } = album || {};

  const truncatedDescription = short_description 
    ? (short_description.length > 100
        ? `${short_description.slice(0, 100)}...`
        : short_description)
    : "No description available";

  return (
    <Card
      className="mb-4 album-card"
      style={{
        borderRadius: "15px",
        overflow: "hidden",
        boxShadow: "0px 6px 15px rgba(0, 0, 0, 0.2)",
        transition: "transform 0.3s ease, box-shadow 0.3s ease",
      }}
      onMouseEnter={(e) => {
        e.currentTarget.style.transform = "translateY(-10px)";
        e.currentTarget.style.boxShadow = "0px 10px 20px rgba(0, 0, 0, 0.25)";
      }}
      onMouseLeave={(e) => {
        e.currentTarget.style.transform = "translateY(0)";
        e.currentTarget.style.boxShadow = "0px 6px 15px rgba(0, 0, 0, 0.2)";
      }}
    >
      {/* Album Cover */}
      <Card.Img
        variant="top"
        src={cover_image}
        alt={title}
        style={{
          width: "100%",
          height: "auto",
        }}
      />
      <Card.Body>
        {/* Album Title */}
        <Card.Title style={{ fontSize: "1.5rem", fontWeight: "bold" }}>
          <Link
            to={`/albums/${id}`}
            style={{
              textDecoration: "none",
              color: "#333",
            }}
          >
            {title}
          </Link>
        </Card.Title>
        {/* Artist and Release Year */}
        <Card.Text>
          <Badge bg="info" style={{ fontSize: "0.9rem", marginRight: "5px" }}>
            {artist}
          </Badge>
          <span style={{ color: "#6c757d", fontSize: "0.9rem" }}>
            {release_year}
          </span>
        </Card.Text>
        {/* Brief Description */}
        <Card.Text style={{ fontSize: "0.9rem", color: "#555" }}>
          {truncatedDescription}
        </Card.Text>
        {/* View Album Button */}
        <Link
          to={`/albums/${id}`}
          style={{
            display: "inline-block",
            backgroundColor: "#007BFF",
            color: "white",
            padding: "8px 15px",
            borderRadius: "10px",
            fontWeight: "500",
            textDecoration: "none",
            transition: "background-color 0.3s ease",
          }}
          onMouseEnter={(e) => (e.target.style.backgroundColor = "#0056b3")}
          onMouseLeave={(e) => (e.target.style.backgroundColor = "#007BFF")}
        >
          View Album
        </Link>
      </Card.Body>
    </Card>
  );
}

export default AlbumCard;