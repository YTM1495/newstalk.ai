import NewsCard from "../components/NewsCard";
import Link from "next/link";
type NewsArticle = {
          id:number;
          title:string;
          category:string;
          source:string;
          published_at:string;
        };

export default async function Home(){
        const apiUrl = process.env.NEXT_PUBLIC_API_URL;
        if(!apiUrl){
          throw new Error("NEXT_PUBLIC_API_URL is not configured");
            }
        let response: Response;
        try {
          response = await fetch(`${apiUrl}/news`);
        } catch (error) {
          console.error("Backend connection failed:", {
            apiUrl,
            error,
          });
          throw error;
        }
        if(!response.ok){
            throw new Error("Failed to fetch news");
        }
        const news: NewsArticle[] = await response.json();
        return (
          <>
          <main className = "max-w-3xl mx-auto p-8">
            <h1 className = "text-4xl font-bold mb-8 text-center">NewsTalk AI</h1>
           {news.map((article) => (
            <NewsCard key = {article.id}
                      id = {article.id}
                      title = {article.title}
                      category = {article.category}
                      source = {article.source}
                      date = {article.published_at}/>

           ))}
          </main>
          </>
        );

}
