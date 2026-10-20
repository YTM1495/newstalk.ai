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
    const [error, setError] = useState(false);

    useEffect(() => {
        async function fetchForYouNews(){
            const apiUrl = process.env.NEXT_PUBLIC_API_URL;
            if(!apiUrl){
                throw new Error("NEXT_PUBLIC_API_URL is not configured");
            }
            try{
                const response = await fetch(
                    `${apiUrl}/feed/for-you?user_id=1`
                );

                if(!response.ok){
                    throw new Error("Failed to fetch personalized news");
                }

                const data = await response.json();
                setNews(data);
            }catch (error) {
            console.error(error);
            setError(true);
                } finally {
            setLoading(false);
            }
            if (error) {
    return (
        <main className="max-w-3xl mx-auto p-8 text-center">
            <h1 className="text-2xl font-bold mb-4">
                Unable to load your news
            </h1>

            <p className="text-gray-600 mb-6">
                We couldn't load your personalized feed.
                Please try again.
            </p>

            <button
                type="button"
                onClick={() => window.location.reload()}
                className="cursor-pointer rounded-lg bg-black px-6 py-3 text-white"
            >
                Try again
            </button>
        </main>
    );
    }
        }
        fetchForYouNews();
    },[]);
    if (loading){
        return <p>Loading your news...</p>;
    }

    if (error) {
    return (
        <main className="max-w-3xl mx-auto p-8 text-center">
            <h1 className="text-2xl font-bold mb-4">
                Unable to load your news
            </h1>

            <p className="text-gray-600 mb-6">
                We couldn't load your personalized feed.
                Please try again.
            </p>

            <button
                type="button"
                onClick={() => window.location.reload()}
                className="cursor-pointer rounded-lg bg-black px-6 py-3 text-white"
            >
                Try again
            </button>
        </main>
    );
        }
    return (
        <main className="p-6">
            <h1 className="text-3xl font-bold mb-6">
                For You
            </h1>

            {news.length === 0 ? (
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
