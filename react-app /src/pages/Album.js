import React from "react";
import { useParams } from "react-router-dom";
import { useQuery } from "react-query";
import { API } from "../constants";
import { Container, Spinner, Alert, Row, Col, Card, ListGroup, Badge } from "react-bootstrap";

function Album() {
  const { id } = useParams();

  const fetchAlbumDetails = async () => {
    const response = await fetch(`${API}albums/${id}`);
    if (!response.ok) throw new Error("Failed to fetch album details");
    return response.json();
  };

  const { data: album, isLoading, error } = useQuery(["album", id], fetchAlbumDetails);

  // Helper function to format total playtime into MM:SS
  const formatPlaytime = (totalSeconds) => {
    const minutes = Math.floor(totalSeconds / 60);
    const seconds = totalSeconds % 60;
    return `${minutes}:${seconds < 10 ? "0" : ""}${seconds}`;
  };

  if (isLoading) return <Spinner animation="border" />;
  if (error) return <Alert variant="danger">{error.message}</Alert>;

  return (
    <Container className="py-4">
      {/* Breadcrumb */}
      <Row>
        <Col>
          <nav aria-label="breadcrumb">
            <ol className="breadcrumb">
              <li className="breadcrumb-item">
                <a href="/">Albums</a>
              </li>
              <li className="breadcrumb-item active" aria-current="page">
                {album.title}
              </li>
            </ol>
          </nav>
        </Col>
      </Row>

      {/* Album Details */}
      <Row className="align-items-center mb-4">
        <Col md={4}>
          <img
            src={album.cover_image || "default_image_url.jpg"}
            alt={album.title}
            style={{
              width: "100%",
              height: "auto",
              borderRadius: "15px",
              boxShadow: "0px 6px 15px rgba(0, 0, 0, 0.2)",
            }}
          />
        </Col>
        <Col md={8}>
          <h1 style={{ fontWeight: "bold", marginBottom: "15px" }}>{album.title}</h1>
          <h5>
            <Badge bg="info">{album.artist}</Badge>
            <span style={{ marginLeft: "10px", color: "#6c757d" }}>({album.release_year})</span>
          </h5>
          <p style={{ fontSize: "1rem", color: "#555", marginTop: "15px" }}>
            {album.short_description}
          </p>
          <h4 style={{ color: "#4CAF50", fontWeight: "bold" }}>£{album.price}</h4>
          <p style={{ fontSize: "1.2rem", color: "#007BFF" }}>
            <strong>Total Playtime:</strong>{" "}
            {album.total_playtime ? formatPlaytime(album.total_playtime) : "N/A"}
          </p>
        </Col>
      </Row>

      {/* Tracklist Section */}
      <Row>
        <Col>
          <Card className="shadow-lg" style={{ borderRadius: "15px", overflow: "hidden" }}>
            <Card.Header className="bg-primary text-white text-center" style={{ fontWeight: "bold" }}>
              Tracklist
            </Card.Header>
            <ListGroup variant="flush">
              {album.songs && album.songs.length > 0 ? (
                album.songs.map((track, index) => (
                  <ListGroup.Item
                    key={index}
                    style={{
                      display: "flex",
                      justifyContent: "space-between",
                      alignItems: "center",
                      padding: "10px 15px",
                    }}
                  >
                    <div>
                      <strong>{index + 1}.</strong> {track.title}
                    </div>
                  </ListGroup.Item>
                ))
              ) : (
                <ListGroup.Item className="text-center">No tracks available</ListGroup.Item>
              )}
            </ListGroup>
          </Card>
        </Col>
      </Row>
    </Container>
  );
}

export default Album;
