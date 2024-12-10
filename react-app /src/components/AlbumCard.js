import React from "react";
import { Link } from "react-router-dom";
import { Card } from "react-bootstrap";

function AlbumCard({ album }) {
  return (
    <Card
      className="mb-3 album-card"
      style={{
        borderRadius: "15px",
        overflow: "hidden",
        boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.1)",
        transition: "transform 0.3s ease, box-shadow 0.3s ease",
      }}
      onMouseEnter={(e) => {
        e.currentTarget.style.transform = "translateY(-10px)";
        e.currentTarget.style.boxShadow = "0px 8px 15px rgba(0, 0, 0, 0.2)";
      }}
      onMouseLeave={(e) => {
        e.currentTarget.style.transform = "translateY(0)";
        e.currentTarget.style.boxShadow = "0px 4px 10px rgba(0, 0, 0, 0.1)";
      }}
    >
      <Card.Img
        variant="top"
        src={album.cover_image || "default_image_url.jpg"}
        alt={album.title}
        style={{
          width: "100%", // Ensure the image spans the full width of the card
          height: "auto", // Maintain original aspect ratio
        }}
      />
      <Card.Body>
        <Card.Title>
          <Link to={`/albums/${album.id}`} style={{ textDecoration: "none", color: "#333" }}>
            {album.title}
          </Link>
        </Card.Title>
        <Card.Text>
          <small>{album.artist}</small>
          <br />
          <small>£{album.price}</small>
        </Card.Text>
      </Card.Body>
    </Card>
  );
}

export default AlbumCard;
