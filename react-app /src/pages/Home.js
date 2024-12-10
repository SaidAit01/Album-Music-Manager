import React from "react";
import { useQuery } from "react-query";
import { API } from "../constants";
import { Container, Row, Col, Spinner, Alert } from "react-bootstrap";
import AlbumCard from "../components/AlbumCard";

function Home({ searchQuery }) {
  const fetchAlbums = async () => {
    const response = await fetch(`${API}albums`);
    if (!response.ok) throw new Error("Failed to fetch albums");
    return response.json();
  };

  const { data: albums, isLoading, error } = useQuery("albums", fetchAlbums);

  // Filter albums based on the search query
  const filteredAlbums = albums
    ? albums.filter((album) =>
        album.title.toLowerCase().includes(searchQuery?.toLowerCase() || "")
      )
    : [];

  if (isLoading)
    return (
      <div className="d-flex justify-content-center align-items-center" style={{ height: "50vh" }}>
        <Spinner animation="border" role="status">
          <span className="sr-only">Loading...</span>
        </Spinner>
      </div>
    );

  if (error)
    return (
      <Alert variant="danger" className="text-center">
        {error.message}
      </Alert>
    );

  if (filteredAlbums.length === 0) {
    return (
      <Container className="text-center py-5">
        <p>No albums found. Try adjusting your search.</p>
      </Container>
    );
  }

  return (
    <Container className="py-4">
      <Row className="g-3">
        {filteredAlbums.map((album) => (
          <Col md={4} sm={6} xs={12} key={album.id}>
            <AlbumCard album={album} />
          </Col>
        ))}
      </Row>
    </Container>
  );
}

export default Home;
