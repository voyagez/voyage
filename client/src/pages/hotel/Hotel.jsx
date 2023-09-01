import React, { useState, useEffect, useContext } from "react"
import { useNavigate } from "react-router-dom"
import { SearchContext } from "../../context/SearchContext"
import Navbar from "../../components/navbar/Navbar"
import Header from "../../components/header/Header"
import Footer from "../../components/footer/Footer"
import "./hotel.css"

const Hotels = () => {
    const navigate = useNavigate()
    const { city } = useContext(SearchContext)
    const [hotels, setHotels] = useState([])

    useEffect(() => {
        async function fetchHotels() {
            try {
                const response = await fetch(`/hotels/search?city=${city}&limit=10`)
                const data = await response.json()
                setHotels(data)
            } catch (error) {
                console.error("Error fetching hotels:", error)
            }
        }
        fetchHotels()
    }, [city])

    return (
        <div>
            <Navbar />
            <Header type="list" />
            <div className="hotelsContainer">
                {hotels.map(hotel => (
                    <div key={hotel.id} className="hotelCard" onClick={() => navigate(`/hoteldetails/${hotel.id}`)}>
                        <img src={hotel.thumbnail} alt={hotel.name} />
                        <h2>{hotel.name}</h2>
                        <p>{hotel.shortDescription}</p>
                    </div>
                ))}
            </div>
            <Footer />
        </div>
    )
}

export default Hotels
