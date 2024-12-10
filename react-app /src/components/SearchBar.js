import React, { useState } from "react";
import { Form, FormControl, Button } from "react-bootstrap";

function SearchBar({ onSearch }) {
  const [query, setQuery] = useState("");

  const handleSearch = (e) => {
    e.preventDefault();
    onSearch(query);
  };

  return (
    <Form
      onSubmit={handleSearch}
      className="d-flex align-items-center p-2 search-bar"
    >
      <FormControl
        type="text"
        placeholder="Search..."
        className="me-2"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        style={{
          borderRadius: "15px",
          width: "200px",
          boxShadow: "0px 4px 6px rgba(0, 0, 0, 0.1)",
        }}
      />
      <Button
        type="submit"
        variant="primary"
        style={{
          borderRadius: "15px",
          background: "linear-gradient(45deg, #6b9ac4, #264de4)",
          border: "none",
          padding: "5px 15px",
          boxShadow: "0px 4px 6px rgba(0, 0, 0, 0.1)",
        }}
      >
        Go
      </Button>
    </Form>
  );
}

export default SearchBar;
