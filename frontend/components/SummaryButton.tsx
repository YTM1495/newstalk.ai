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
    const apiUrl = process.env.NEXT_PUBLIC_API_URL;
    if(!apiUrl){
        throw new Error("NEXT_PUBLIC_API_URL is not configured");
    }
    try{
        const response = await fetch(
        `${apiUrl}/news/${articleId}/summary`,
        {
            method:"POST",
        }
    );
    if (!response.ok) {
  const errorDetails = await response.text();

  console.error("Summary API error:", {
    status: response.status,
    details: errorDetails,
  });

  throw new Error(
    `Failed to generate summary: ${response.status}`
  );}
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
