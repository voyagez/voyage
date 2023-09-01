import React, { useState, useEffect } from "react"
import { useLocation } from "react-router-dom"
import Navbar from "../../components/navbar/Navbar"
import Header from "../../components/header/Header"
import Footer from "../../components/footer/Footer"
import "./hotelDetails.css"

const HotelDetails = () => {
    const location = useLocation()
    const hotelId = location.pathname.split("/")[2]
    const [hotelDetails, setHotelDetails] = useState({})

    useEffect(() => {
        async function fetchHotelDetails() {
            try {
                const response = await fetch(`/hotels/detail/${hotelId}`)
                const data = await response.json()
                setHotelDetails(data)
            } catch (error) {
                console.error("Error fetching hotel details:", error)
            }
        }
        fetchHotelDetails()
    }, [hotelId])

    return (
        <div>
            <Navbar />
            <Header type="detail" />
            <div className="hotelDetailsContainer">
                <h1>{hotelDetails.name}</h1>
                <img src={hotelDetails.mainImage} alt={hotelDetails.name} />
                <p>{hotelDetails.description}</p>
                {/* */}
            </div>
            <Footer />
        </div>
    );
}

export default HotelDetails
