

async function fetchAPI(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Request failed with status ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('API request error:', error);
        return null;
    }
}

async function fetchAndDisplayLocationInfo(locationId) {
    const locationUrl = `https://api.tripadvisor.com/api/partner/2.0/location/${locationId}?key=${TRIPADVISOR_AUTH_TOKEN}`;
    const reviewsUrl = `https://api.content.tripadvisor.com/api/v1/location/${locationId}/reviews?key=${TRIPADVISOR_AUTH_TOKEN}`;
    const photosUrl = `https://api.content.tripadvisor.com/api/v1/location/${locationId}/photos?key=${TRIPADVISOR_AUTH_TOKEN}`;

    const [locationData, reviewsData, photosData] = await Promise.all([
        fetchAPI(locationUrl),
        fetchAPI(reviewsUrl),
        fetchAPI(photosUrl)
    ]);

    if (locationData && reviewsData && photosData) {
        const name = locationData.name;
        const description = locationData.description;
        const address = locationData.address_obj.address_string;
        const rating = locationData.rating;
        const ratingImageUrl = locationData.rating_image_url;
        const phone = locationData.phone;
        const website = locationData.website;

        const infoContainer = document.createElement('div');
        infoContainer.innerHTML = `
            <h2>${name}</h2>
            <p>${description}</p>
            <p>Address: ${address}</p>
            <p>Rating: ${rating}</p>
            <img src="${ratingImageUrl}" alt="Rating">
            <p>Phone: ${phone}</p>
            <p>Website: <a href="${website}" target="_blank">${website}</a></p>
        `;
        document.body.appendChild(infoContainer);

        console.log('Location Reviews:', reviewsData);
        console.log('Location Photos:', photosData);
    }
}

async function getUserLocation() {
    try {
        const position = await new Promise((resolve, reject) => {
            navigator.geolocation.getCurrentPosition(resolve, reject);
        });

        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;

        return { latitude, longitude };
    } catch (error) {
        console.error('Error getting user location:', error);
        return null;
    }
}

async function fetchAndDisplayNearbyLocations(propertyType) {
    const userLocation = await getUserLocation();
    if (userLocation) {
        const nearbyLocations = await fetchNearbyLocations(userLocation.latitude, userLocation.longitude, propertyType);
        nearbyLocations.forEach(async location => {
            const locationId = location.location_id;
            await fetchAndDisplayLocationInfo(locationId);
            console.log('------------------------------------------------------');
        });
    }
}

