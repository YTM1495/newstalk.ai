import NewsCard from "../components/NewsCard";
type NewsArticle = {
          id:number;
          title:string;
          category:string;
          source:string;
          date:string;
        };

export default async function Home(){
      
        const response = await fetch("http://localhost:8000/news");
        const news: NewsArticle[] = await response.json();

        return (
          <>
          <main className = "max-w-3xl mx-auto p-8">
            <h1 className = "text-4xl font-bold mb-8 text-center">NewsTalk AI</h1>
           {news.map((article) => (
            <NewsCard key = {article.id}
                      title = {article.title}
                      category = {article.category}
                      source = {article.source}
                      date = {article.date}/>
           ))}
          </main>
          </>
        );

}