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
      
        const response = await fetch("http://localhost:8000/news");
        if(!response.ok){
          throw new Error("Failed to feth news");
        }
        const news: NewsArticle[] = await response.json();


        return (
          <>
          <main className = "max-w-3xl mx-auto p-8">
            <h1 className = "text-4xl font-bold mb-8 text-center">NewsTalk AI</h1>
           {news.map((article) => (
            <Link
            key = {article.id}
            href = {`/news/${article.id}`}
            >
            <NewsCard key = {article.id}
                      id = {article.id}
                      title = {article.title}
                      category = {article.category}
                      source = {article.source}
                      date = {article.published_at}/>
                      </Link>
           ))}
          </main>
          </>
        );

}