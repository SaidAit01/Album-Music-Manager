import React from "react";
import { Link } from "react-router-dom";
import { useQuery } from "react-query";
import { API } from "../constants";
import { Container, Row, Col, Card, Spinner, Alert } from "react-bootstrap";

function Home() {
  const fetchAlbums = async () => {
    const response = await fetch(`${API}albums`);
    if (!response.ok) throw new Error("Failed to fetch albums");
    return response.json();
  };

  const { data: albums, isLoading, error } = useQuery("albums", fetchAlbums);

  if (isLoading) return <Spinner animation="border" />;
  if (error) return <Alert variant="danger">{error.message}</Alert>;

  return (
    <Container>
      <Row>
        {albums.map((album) => (
          <Col md={4} sm={6} xs={12} key={album.id}>
            <Card className="mb-3">
              <Card.Img variant="top" src={album.coverUrl} alt={album.title} />
              <Card.Body>
                <Card.Title>
                  <Link to={`/albums/${album.id}`}>{album.title}</Link>
                </Card.Title>
                <Card.Text>
                  <small>{album.artist}</small>
                  <br />
                  <small>£{album.price} ({album.format})</small>
                </Card.Text>
              </Card.Body>
            </Card>
          </Col>
        ))}
      </Row>
    </Container>
  );
}

export default Home;
