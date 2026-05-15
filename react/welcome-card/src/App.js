import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import myImage from "./images/sample.jpg";

function App() {
  // variable for name
  const userName = "Friend";

  // console message
  console.log("React app started");

  return (
    // container for centering content
    <div className="container d-flex justify-content-center align-items-center vh-100">
      
      {/* card layout */}
      <div className="card text-center p-4 shadow" style={{ width: "22rem" }}>
        
        {/* heading */}
        <h2 style={{ color: "#0d6efd", fontWeight: "bold" }}>
          Welcome to React Learning, {userName}
        </h2>

        {/* internal image */}
        <img
          src={myImage}
          alt="Internal"
          className="img-fluid mx-auto my-3"
          style={{ width: "200px" }}
        />

        {/* external image */}
        <img
          src="https://images.unsplash.com/photo-1518770660439-4636190af475"
          alt="External"
          className="img-fluid mx-auto my-3"
        />

        {/* description */}
        <p className="text-muted">
          This is your first card with images and styles!
        </p>

      </div>
    </div>
  );
}

export default App;