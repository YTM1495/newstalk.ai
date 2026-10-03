"use client";
import NewsCard from "@/components/NewsCard";
import { useEffect,useState } from "react";

type NewsArticle = {
    id:number;
    title:string;
    content:string| null;
    category:string;
     source: string;
  published_at: string;
  summary: string | null;
  url: string;
  description: string;
};

export default function ForYouPage(){
    const [news,setNews] = useState<NewsArticle[]>([]);
    const [loading,setLoading] = useState(true);

    useEffect(() => {
        async function fetchForYouNews(){
            try{
                const response = await fetch(
                    "http://127.0.0.1:8000/feed/for-you?user_id=1"
                );

                if(!response.ok){
                    throw new Error("Failed to fetch personalized news");
                }

                const data = await response.json();
                setNews(data);
            }catch(error){
                console.error(error);
            }finally{
                setLoading(false);
            }
        }
        fetchForYouNews();
    },[]);
    if (loading){
        return <p>Loading your news...</p>;
    }
    return (
        <main className="p-6">
            <h1 className="text-3xl font-bold mb-6">
                For You
            </h1>

            {news.length == 0 ? (
                <p>No personalized news available.</p>
            ):(
                news.map((article) => (
                    <NewsCard
                    key={article.id}
                    id={article.id}
                     title={article.title}
                    category={article.category}
                    source={article.source}
                    date={article.published_at}
                    />
                ))
            )}
        </main>
    );
}
