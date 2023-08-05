import React from "react";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from "./components/Header";
import Homepage from "./components/Homepage";
import Listings from "./components/Listings";
import ListingDetails from "./components/ListingDetails";
import Signup from "./components/Signup";
import Login from "./components/Login";
import Footer from "./components/Footer";
import './App.css'
import Search from "./components/Search";
import Tenantsignup from "./components/Tenantsignup";
import Ownersignup from "./components/Ownersignup";
import PropertyDetails from "./components/PropertyDetails";
import Properties from "./components/Properties";


function App() {
  return (
    <div className="app-container">
      <Header />
      <div className="main-content">
        <Routes>
          <Route path="/" element={<Homepage />} />
          <Route path="/listings" element={<Listings />} />
          <Route path="/ListingDetails/:id" element={<ListingDetails />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/login" element={<Login />} />
          <Route path="/search" element={<Search />} />
          <Route path="/properties" element={<Properties />} />
          <Route path="/propertyDetails/:id" element={<PropertyDetails />} />
          <Route path="/Tenantsignup" element={<Tenantsignup />} />
          <Route path="/Ownersignup" element={<Ownersignup />} />
        </Routes>
      </div>
      <Footer />
    </div>
  );
}

export default App;