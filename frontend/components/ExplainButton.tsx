'use client'
import { useState } from "react";

type ExplainButtonProps = {
    articleId: number;
};
const audiences = [
    {
        value:"child",
        label:"child",
    },
     {
        value:"student",
        label:"student",
    },
    {
        value:"professional",
        label:"professional",
    },
];

export default function ExplainButton({
    articleId,    
}:ExplainButtonProps){

    const[audience,setAudience] = useState("student");
    const [explanation,setExplanation] = useState("");
    const[loading, setLoading] = useState(false);

    async function generateExplanation(){
        setLoading(true);

        try{
            const response = await fetch(
                `http://localhost:8000/news/${articleId}/explanation`,
                {
                    method:"POST",
                    headers:{
                        "Content-Type":"application/json"
                    },
                    body: JSON.stringify({
                        audience:audience,
                    }),

                }
            );
            if(!response.ok){
                throw new Error("Failed to generate explanation");
            }
            const data = await response.json();

            setExplanation(data.explanation);
        }catch(error){
            console.log(error);
        }finally{
            setLoading(false);
        }
    }
    return (
        <div className="mt-8">
        <h2 className="text-xl font-semibold mb-3">
                Explain this news
            </h2>
            <div className="flex gap-2 mb-4">
                {audiences.map((item) => (
                    <button
                    key = {item.value}
                    onClick={() => setAudience(item.value)}
                    className="border rounded +-lg px-4 py-2">
                        {item.label}
                    </button>
                ))}
            </div>
            <button
            onClick={generateExplanation}
            disabled={loading}
            className="border rounded +-lg px-4 py-2"
            >
            {loading
            ?"Generating..."
            :"Generate Explanation"}
            </button>
            {explanation && (
                <div className="mt-4 rounded-lg border p-5">
                    <h3 className="font-semibold mb-3">
                        AI Explanation
                    </h3>
                    <p>{explanation}</p>
                </div>
            )}
            </div>
    );
}