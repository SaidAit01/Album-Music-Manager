import React from "react";
import { useParams } from "react-router-dom";
import { useQuery } from "react-query";
import { API } from "../constants";
import { Container, Card, ListGroup, Spinner, Alert, Breadcrumb } from "react-bootstrap";

function Album() {
  const { id } = useParams();

  const fetchAlbumDetails = async () => {
    const response = await fetch(`${API}albums/${id}`);
    if (!response.ok) throw new Error("Failed to fetch album details");
    return response.json();
  };

  const { data: album, isLoading, error } = useQuery(["album", id], fetchAlbumDetails);

  if (isLoading) return <Spinner animation="border" />;
  if (error) return <Alert variant="danger">{error.message}</Alert>;

  return (
    <Container>
      <Breadcrumb>
        <Breadcrumb.Item href="/">Albums</Breadcrumb.Item>
        <Breadcrumb.Item active>{album.title}</Breadcrumb.Item>
      </Breadcrumb>
      <Card>
        <Card.Img variant="top" src={album.cover_image} alt={album.title} />
        <Card.Body>
          <Card.Title>{album.title}</Card.Title>
          <Card.Text>
            <strong>£{album.price}</strong>
            <br />
            {album.artist} ({album.release_year})
            <br />
            {album.short_description}
          </Card.Text>
        </Card.Body>
        <ListGroup variant="flush">
          <ListGroup.Item><strong>Tracklist:</strong></ListGroup.Item>
          {album.songs && album.songs.length > 0 ? (
            album.songs.map((track, index) => (
              <ListGroup.Item key={index}>
                {index + 1}. {track.title} - {track.length}s
              </ListGroup.Item>
            ))
          ) : (
            <ListGroup.Item>No tracks available</ListGroup.Item>
          )}
        </ListGroup>
      </Card>
    </Container>
  );
}

export default Album;
