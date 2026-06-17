"use client";

import { useState } from "react";

export default function InstantPage(){
    const [selectedTime, setSelectedTime] = useState(5);
    const [articles, setArticles] = useState<string[]>([]);

    async function generateDigest(){
        const response = await fetch(`http://localhost:8000/instant-news/${selectedTime}`);

        const data = await response.json();

        setArticles(data.articles);
    }


    return(
        <main className = "max-w-3xl mx-auto p-8">
            <h1 className = "text-3xl font-bold mb-6">
                Instant News
            </h1>
            <p className="mb-4">
                Selected Time: {selectedTime} minutes
            </p>

            <div className = "flex gap-4">
                <button onClick = {() => setSelectedTime(2)}
                    className = "border px-4 py-2 rounded">
                        2 min
                    </button>
                <button onClick =  {() => setSelectedTime(5)}
                    className = "border px-4 py-2 rounded">
                        5 min
                    </button>
                <button onClick =  {() => setSelectedTime(10)}
                    className = "border px-4 py-2 rounded">
                        10 min
                    </button>
                <button onClick =  {() => setSelectedTime(15)}
                    className = "border px-4 py-2 rounded">
                       15 min
                    </button>
            </div>
            <button onClick = {generateDigest}
                    className = "border px-4 py-2 rounded">
                        Generate Digest
                        </button>
            {articles.length > 0 && (
                <div className="mt-6">
                    <h2 className = "text-xl font-bold mb-3">
                        Your Digest
                    </h2>
                    {articles.map((article,index) => (
                        <p key={index}>
                            •{article}
                        </p>
                    ))}
                </div>
            )}
        </main>
    );
}