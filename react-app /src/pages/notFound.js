import { Col, Container, Row } from 'react-bootstrap';

function NotFound() {
	return (
		<Container fluid className="vh-100 d-flex justify-content-center align-items-center">
			<Row>
				<Col className="text-center">
					<h1>404</h1>
					<h2>Page Not Found</h2>
					<p>Sorry, the page you are looking for does not exist.</p>
				</Col>
			</Row>
		</Container>
	);
}

export default NotFound;