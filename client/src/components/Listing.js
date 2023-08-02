import React, { useEffect, useState } from 'react';
import '../CSS/Listing.css'; // Import your custom CSS file


function Listing() {
  const [listings, setListings] = useState([]);

  useEffect(() => {
    // Function to fetch the listings using the token
    const fetchListings = async () => {
      const token = localStorage.getItem('access_token');
      if (!token) {
        console.error('Token not found. User is not authenticated.');
        return;
      }

      try {
        const response = await fetch('/listings', {
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',
          },
        });

        if (!response.ok) {
          throw new Error('Failed to fetch listings.');
        }

        const data = await response.json();
        setListings(data); // Updating the 'listings' state with the fetched data
        console.log(data); // Logging the fetched data to the console
      } catch (error) {
        console.error('Error fetching listings:', error);
      }
    };

    fetchListings();
  }, []);


  return (
    <div className="custom-listings-container">
      <h2>Listings</h2>
      <div className="custom-row">
        {listings.map(listing => (
          <div key={listing.id} className="custom-col-md-6 custom-col-lg-4 custom-mb-4">
            <div className="custom-card custom-listing-card">
              <img src={listing.media} className="custom-card-img-top custom-property-img" alt="Property" />
              <div className="custom-card-body">
                <h5 className="custom-card-title">{listing.title}</h5>
                <p className="custom-card-text">{listing.description}</p>
                <p className="custom-card-text">Rent: {listing.rent}</p>
                <p className="custom-card-text">Location: {listing.place}</p>
                <p className="custom-card-text">Utilities: {listing.utilities}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Listing;
