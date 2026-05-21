'use client';
import React, { useState } from "react";
export default function Botton() {
    const [randomValue, setRandomValue] = useState<number | null>(null);
    const [loading, setLoading] = useState(false);
    const handleFetchRandom = async () => {
        setLoading(true);
        try {
            // Make sure this URL matches your local FastAPI server address
            const response = await fetch("http://localhost:8000/random");
            
            if (!response.ok) throw new Error("Network response was not ok");
            
            const data = await response.json();
            setRandomValue(data.value); // Update the state with the new value
        } catch (error) {
            console.error("Failed to fetch data:", error);
        } finally {
            setLoading(false);
        }
    };
    return (
        <>
            <button className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600" onClick={() => handleFetchRandom()} disabled={loading}>
                {loading ? "Fetching..." : "Get Random Value"}
            </button>
            {/* Display the value once it's fetched */}
            {randomValue !== null && (
                <div className="mt-2 text-lg font-semibold">
                    Returned Value: {randomValue}
                </div>
            )}
         </>
    );
}
