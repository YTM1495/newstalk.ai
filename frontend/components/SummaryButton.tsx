"use client"

import {useState} from "react";

type SummaryButtonProps = {
    articleId: number;
};

export default function SummaryButton({
    articleId,
}:SummaryButtonProps){
  const[summary,setSummary] = useState("");
const [loading,setLoading] = useState(false);

async function generateSummary(){
    setLoading(true);
    try{
        const response = await fetch(
        `http://localhost:8000/news/${articleId}/summary`,
        {
            method:"POST",
        }
    );
    if (!response.ok){
        throw new Error("Filed to generate summary");
    }
    const data = await response.json();
    setSummary(data.summary);
    }
    catch(error){
        console.error(error);
    }
    finally{
        setLoading(false);
    }  
}
return (
        <>
        <button
        onClick={generateSummary}
        disabled = {loading}
        className = "..."
        >
            {loading ? "Generating...":"Generate AI Summary"}
            </button>
        {summary &&(
            <div className = "mt-4 rounded-lg border p-4">
                <h3 className="font-semibold">AI Summary</h3>
                <p>{summary}</p>
                </div>
        )}
        </>
    );
}
