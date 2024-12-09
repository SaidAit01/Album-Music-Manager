import React from "react";
import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Album from "./pages/Album";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/albums/:id" element={<Album />} />
    </Routes>
  );
}

export default App;
