import React, { useState } from "react";
import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Album from "./pages/Album";
import Navbar from "./components/Navbar"; // Import your Navbar component
import Hero from "./components/Hero"; // Import your Hero component
import SearchBar from "./components/SearchBar"; // Import your SearchBar component

function App() {
  const [searchQuery, setSearchQuery] = useState(""); // State for search query

  return (
    <>
      {/* Navbar is always displayed */}
      <Navbar />
      
      <Routes>
        <Route
          path="/"
          element={
            <>
              {/* Hero and SearchBar displayed only on the home page */}
              <Hero />
              <SearchBar onSearch={(query) => setSearchQuery(query)} />
              <Home searchQuery={searchQuery} />
            </>
          }
        />
        <Route path="/albums/:id" element={<Album />} />
      </Routes>
    </>
  );
  
}

export default App;
